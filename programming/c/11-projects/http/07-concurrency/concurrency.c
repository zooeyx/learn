#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <time.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <netinet/in.h>
#include "../../../common/debug.h"

#define PORT 8080
#define BUFSIZE 4096
#define DOCROOT "www"

static volatile sig_atomic_t running = 1;

// TODO: SIGCHLD handler — reap zombie child processes
//   void sigchld_handler(int sig)
//   {
//       (void)sig;
//       while (waitpid(-1, NULL, WNOHANG) > 0)
//           ;
//   }

// TODO: SIGINT handler — graceful shutdown
//   void sigint_handler(int sig)
//   {
//       (void)sig;
//       running = 0;
//   }

typedef struct {
    const char *ext;
    const char *type;
} MimeEntry;

static const MimeEntry mime_table[] = {
    { ".html", "text/html" },
    { ".css",  "text/css" },
    { ".js",   "application/javascript" },
    { ".png",  "image/png" },
    { ".jpg",  "image/jpeg" },
    { ".gif",  "image/gif" },
    { ".ico",  "image/x-icon" },
    { ".txt",  "text/plain" },
};
#define MIME_COUNT (sizeof(mime_table) / sizeof(mime_table[0]))

const char *get_mime_type(const char *path) {
    const char *dot = strrchr(path, '.');
    if (!dot) return "application/octet-stream";
    for (size_t i = 0; i < MIME_COUNT; i++) {
        if (strcmp(dot, mime_table[i].ext) == 0)
            return mime_table[i].type;
    }
    return "application/octet-stream";
}

void send_response(int fd, int status, const char *status_text,
                   const char *content_type, const char *body, size_t body_len) {
    char header[BUFSIZE];
    int n = snprintf(header, sizeof(header),
        "HTTP/1.0 %d %s\r\n"
        "Content-Type: %s\r\n"
        "Content-Length: %zu\r\n"
        "\r\n",
        status, status_text, content_type, body_len);
    write(fd, header, n);
    write(fd, body, body_len);
}

void send_error(int fd, int status, const char *text) {
    char body[256];
    int len = snprintf(body, sizeof(body),
        "<html><body><h1>%d — %s</h1></body></html>", status, text);
    send_response(fd, status, text, "text/html", body, len);
}

void log_request(const char *method, const char *path, int status) {
    time_t now = time(NULL);
    struct tm *tm = localtime(&now);
    char timestamp[64];
    strftime(timestamp, sizeof(timestamp), "%Y-%m-%d %H:%M:%S", tm);
    printf("[%s] %s %s — %d\n", timestamp, method, path, status);
}

void handle_request(int client_fd) {
    char buf[BUFSIZE] = {0};
    ssize_t n = read(client_fd, buf, sizeof(buf) - 1);

    if (n <= 0) {
        send_error(client_fd, 400, "Bad Request");
        log_request("-", "-", 400);
        return;
    }

    char method[16] = {0}, path[256] = {0};
    int parsed = sscanf(buf, "%15s %255s", method, path);

    if (parsed < 2) {
        send_error(client_fd, 400, "Bad Request");
        log_request(method[0] ? method : "-", "-", 400);
        return;
    }

    if (strstr(path, "..")) {
        send_error(client_fd, 403, "Forbidden");
        log_request(method, path, 403);
        return;
    }

    char filepath[512] = {0};
    snprintf(filepath, sizeof(filepath), "%s%s", DOCROOT, path);
    size_t plen = strlen(filepath);
    if (filepath[plen - 1] == '/')
        strncat(filepath, "index.html", sizeof(filepath) - plen - 1);

    struct stat st;
    if (stat(filepath, &st) < 0) {
        send_error(client_fd, 404, "Not Found");
        log_request(method, path, 404);
        return;
    }

    FILE *fp = fopen(filepath, "rb");
    if (!fp) {
        send_error(client_fd, 500, "Internal Server Error");
        log_request(method, path, 500);
        return;
    }

    char *body = malloc(st.st_size);
    fread(body, 1, st.st_size, fp);
    fclose(fp);

    const char *mime = get_mime_type(filepath);
    send_response(client_fd, 200, "OK", mime, body, st.st_size);
    free(body);
    log_request(method, path, 200);
}

int main(void) {
    int server_fd = -1;

    // TODO: Install signal handlers
    //   signal(SIGCHLD, sigchld_handler);
    //   signal(SIGINT, sigint_handler);

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    check(server_fd >= 0, "socket");

    int opt = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_addr.s_addr = INADDR_ANY,
        .sin_port = htons(PORT)
    };

    check(bind(server_fd, (struct sockaddr *)&addr, sizeof(addr)) == 0, "bind");
    check(listen(server_fd, 10) == 0, "listen");
    printf("Serving %s/ on port %d (forking)...\n", DOCROOT, PORT);

    // TODO: Fork-per-connection accept loop
    //   while (running) {
    //       int client_fd = accept(server_fd, NULL, NULL);
    //       if (client_fd < 0) continue;
    //
    //       pid_t pid = fork();
    //       if (pid < 0) {
    //           perror("fork");
    //           close(client_fd);
    //           continue;
    //       }
    //
    //       if (pid == 0) {
    //           // Child process
    //           close(server_fd);
    //           handle_request(client_fd);
    //           close(client_fd);
    //           exit(0);
    //       }
    //
    //       // Parent process
    //       close(client_fd);
    //   }

    printf("concurrency — not yet implemented\n");

    close(server_fd);
    printf("\nShutdown complete.\n");
    return 0;

error:
    if (server_fd >= 0) close(server_fd);
    return 1;
}

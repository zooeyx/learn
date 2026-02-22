#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <netinet/in.h>
#include "../../../common/debug.h"

#define PORT 8080
#define BUFSIZE 4096
#define DOCROOT "www"

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

void handle_request(int client_fd) {
    char buf[BUFSIZE] = {0};
    read(client_fd, buf, sizeof(buf) - 1);

    char method[16] = {0}, path[256] = {0};
    sscanf(buf, "%15s %255s", method, path);

    // TODO: Block path traversal — reject requests containing ".."
    //   if (strstr(path, "..")) {
    //       send_error(client_fd, 403, "Forbidden");
    //       return;
    //   }

    // TODO: Build the filesystem path
    //   char filepath[512] = {0};
    //   snprintf(filepath, sizeof(filepath), "%s%s", DOCROOT, path);
    //
    //   Hint: if path ends with '/', append "index.html"
    //   size_t plen = strlen(filepath);
    //   if (filepath[plen - 1] == '/')
    //       strncat(filepath, "index.html", sizeof(filepath) - plen - 1);

    // TODO: Check if file exists with stat()
    //   struct stat st;
    //   if (stat(filepath, &st) < 0) {
    //       send_error(client_fd, 404, "Not Found");
    //       return;
    //   }

    // TODO: Read the file contents
    //   FILE *fp = fopen(filepath, "rb");
    //   if (!fp) { send_error(client_fd, 500, "Internal Server Error"); return; }
    //   char *body = malloc(st.st_size);
    //   fread(body, 1, st.st_size, fp);
    //   fclose(fp);

    // TODO: Send response and free
    //   send_response(client_fd, 200, "OK", "text/html", body, st.st_size);
    //   free(body);

    send_error(client_fd, 501, "Not Implemented");
}

int main(void) {
    int server_fd = -1;

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    check(server_fd >= 0, "socket");

    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_addr.s_addr = INADDR_ANY,
        .sin_port = htons(PORT)
    };

    check(bind(server_fd, (struct sockaddr *)&addr, sizeof(addr)) == 0, "bind");
    check(listen(server_fd, 10) == 0, "listen");
    printf("Serving %s/ on port %d...\n", DOCROOT, PORT);

    while (1) {
        int client_fd = accept(server_fd, NULL, NULL);
        if (client_fd < 0) { perror("accept"); continue; }
        handle_request(client_fd);
        close(client_fd);
    }

error:
    if (server_fd >= 0) close(server_fd);
    return 1;
}

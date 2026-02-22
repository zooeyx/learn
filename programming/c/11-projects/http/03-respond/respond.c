#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include "../../../common/debug.h"

#define PORT 8080
#define BUFSIZE 4096

// TODO: Write a helper to send a full HTTP response
//   void send_response(int fd, int status, const char *status_text,
//                      const char *content_type, const char *body)
//   {
//       char response[BUFSIZE];
//       int body_len = strlen(body);
//       int n = snprintf(response, sizeof(response),
//           "HTTP/1.0 %d %s\r\n"
//           "Content-Type: %s\r\n"
//           "Content-Length: %d\r\n"
//           "\r\n"
//           "%s",
//           status, status_text, content_type, body_len, body);
//       write(fd, response, n);
//   }

// TODO: Write a helper to handle a single request
//   void handle_request(int client_fd)
//   {
//       char buf[BUFSIZE] = {0};
//       read(client_fd, buf, sizeof(buf) - 1);
//
//       char method[16] = {0}, path[256] = {0};
//       sscanf(buf, "%15s %255s", method, path);
//
//       if (strcmp(path, "/") == 0) {
//           send_response(client_fd, 200, "OK", "text/html",
//               "<html><body><h1>Welcome</h1></body></html>");
//       } else if (strcmp(path, "/about") == 0) {
//           send_response(client_fd, 200, "OK", "text/html",
//               "<html><body><h1>About</h1><p>HTTP server in C.</p></body></html>");
//       } else if (strcmp(path, "/time") == 0) {
//           // Hint: use time() and ctime() to get current time string
//           char body[256];
//           time_t now = time(NULL);
//           snprintf(body, sizeof(body),
//               "<html><body><h1>%s</h1></body></html>", ctime(&now));
//           send_response(client_fd, 200, "OK", "text/html", body);
//       } else {
//           send_response(client_fd, 404, "Not Found", "text/html",
//               "<html><body><h1>404 — Not Found</h1></body></html>");
//       }
//   }

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
    printf("Listening on port %d...\n", PORT);

    // TODO: Accept loop — handle requests forever
    //   while (1) {
    //       int client_fd = accept(server_fd, NULL, NULL);
    //       if (client_fd < 0) { perror("accept"); continue; }
    //       handle_request(client_fd);
    //       close(client_fd);
    //   }

    printf("respond — not yet implemented\n");

    close(server_fd);
    return 0;

error:
    if (server_fd >= 0) close(server_fd);
    return 1;
}

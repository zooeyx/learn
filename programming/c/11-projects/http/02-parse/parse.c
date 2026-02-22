#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include "../../../common/debug.h"

#define PORT 8080
#define BUFSIZE 4096

int main(void) {
    int server_fd = -1;
    int client_fd = -1;

    // --- Socket setup (same as lesson 01) ---
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    check(server_fd >= 0, "socket");

    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_addr.s_addr = INADDR_ANY,
        .sin_port = htons(PORT)
    };

    check(bind(server_fd, (struct sockaddr *)&addr, sizeof(addr)) == 0, "bind");
    check(listen(server_fd, 1) == 0, "listen");
    printf("Listening on port %d...\n", PORT);

    client_fd = accept(server_fd, NULL, NULL);
    check(client_fd >= 0, "accept");

    // --- Read request ---
    char buf[BUFSIZE] = {0};
    ssize_t n = read(client_fd, buf, sizeof(buf) - 1);
    check(n > 0, "read");

    // TODO: Parse method and path from the request line
    //   char method[16] = {0};
    //   char path[256] = {0};
    //   sscanf(buf, "%15s %255s", method, path);
    //   printf("Method: %s, Path: %s\n", method, path);

    // TODO: Build an HTML response body
    //   char body[BUFSIZE] = {0};
    //   snprintf(body, sizeof(body),
    //       "<html><body><h1>You requested: %s</h1></body></html>", path);

    // TODO: Send the response (just the body string for now — proper headers come in lesson 03)
    //   write(client_fd, body, strlen(body));

    close(client_fd);
    close(server_fd);
    return 0;

error:
    if (client_fd >= 0) close(client_fd);
    if (server_fd >= 0) close(server_fd);
    return 1;
}

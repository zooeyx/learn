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

    // TODO: Create a TCP socket
    //   server_fd = socket(AF_INET, SOCK_STREAM, 0)
    //   Use check() to verify it succeeded

    // TODO: Configure the address struct
    //   struct sockaddr_in addr = {0};
    //   Set .sin_family = AF_INET
    //   Set .sin_addr.s_addr = INADDR_ANY
    //   Set .sin_port = htons(PORT)

    // TODO: Bind the socket to the address
    //   bind(server_fd, (struct sockaddr *)&addr, sizeof(addr))

    // TODO: Start listening (backlog of 1 is fine)
    //   listen(server_fd, 1)

    printf("Listening on port %d...\n", PORT);

    // TODO: Accept one connection
    //   client_fd = accept(server_fd, NULL, NULL)

    // TODO: Read the request into a buffer and print it
    //   char buf[BUFSIZE] = {0};
    //   ssize_t n = read(client_fd, buf, sizeof(buf) - 1);
    //   printf("--- Request ---\n%s\n", buf);

    // TODO: Send a response and close
    //   char *response = "Hello from C!\n";
    //   write(client_fd, response, strlen(response));

    close(client_fd);
    close(server_fd);
    return 0;

error:
    if (client_fd >= 0) close(client_fd);
    if (server_fd >= 0) close(server_fd);
    return 1;
}

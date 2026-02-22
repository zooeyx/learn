#include <stdio.h>
#include <stdlib.h>
#include "server.h"

// TODO: Parse command-line arguments and start the server
//   Usage: ./build/server <port> <docroot>
//
//   int main(int argc, char *argv[])
//   {
//       if (argc != 3) {
//           fprintf(stderr, "Usage: %s <port> <docroot>\n", argv[0]);
//           return 1;
//       }
//
//       int port = atoi(argv[1]);
//       const char *docroot = argv[2];
//
//       int server_fd = server_start(port);
//       if (server_fd < 0) return 1;
//
//       printf("Serving %s on port %d...\n", docroot, port);
//       server_run(server_fd, docroot);
//       return 0;
//   }

int main(void) {
    printf("server — not yet implemented\n");
    printf("Usage: ./build/server <port> <docroot>\n");
    return 0;
}

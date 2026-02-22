#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <sys/socket.h>
#include <sys/wait.h>
#include <netinet/in.h>
#include "server.h"
#include "http.h"
#include "../../../common/debug.h"

// TODO: Implement server_start() — create, bind, listen
//   int server_start(int port)
//   {
//       int fd = socket(AF_INET, SOCK_STREAM, 0);
//       check(fd >= 0, "socket");
//
//       int opt = 1;
//       setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
//
//       struct sockaddr_in addr = {
//           .sin_family = AF_INET,
//           .sin_addr.s_addr = INADDR_ANY,
//           .sin_port = htons(port)
//       };
//
//       check(bind(fd, (struct sockaddr *)&addr, sizeof(addr)) == 0, "bind");
//       check(listen(fd, 10) == 0, "listen");
//       return fd;
//
//   error:
//       if (fd >= 0) close(fd);
//       return -1;
//   }

// TODO: Implement server_run() — accept loop with fork
//   void server_run(int server_fd, const char *docroot)
//   {
//       signal(SIGCHLD, ...);  // reap children
//       signal(SIGINT, ...);   // graceful shutdown
//
//       while (running) {
//           int client_fd = accept(server_fd, NULL, NULL);
//           if (client_fd < 0) continue;
//
//           pid_t pid = fork();
//           if (pid == 0) {
//               close(server_fd);
//               http_handle_request(client_fd, docroot);
//               close(client_fd);
//               exit(0);
//           }
//           close(client_fd);
//       }
//   }

#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main(void) {
    // AF_INET IpV4; AF_INET6 IpV6; AF_UNIX local)
    // SOCK_STREAM TCP; SOCK_DGRAM UDP)
    int listed_fd = socket(AF_INET, SOCK_STREAM, 0); // If succeeds, should return 3 or 4; fail -1. sets errno, Kernel code
    if (listed_fd < 0) {
        perror("socket");
        return 1;
    }
}

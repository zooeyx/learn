# 01 — Hello from a Socket

Create a TCP socket that accepts one connection, prints the raw HTTP request, and sends back `"Hello from C!\n"`.

## Concepts

- **TCP sockets**: `socket()` creates an endpoint, `bind()` assigns an address, `listen()` marks it as passive, `accept()` waits for a client
- **`struct sockaddr_in`**: holds IP address + port; use `INADDR_ANY` to listen on all interfaces
- **`htons()`**: converts port number to network byte order (big-endian)
- **`check()` macro**: from `debug.h` — validates return values and jumps to `error:` on failure

## Exercises

- [ ] Create a TCP socket with `socket(AF_INET, SOCK_STREAM, 0)`
- [ ] Configure `struct sockaddr_in` for port 8080
- [ ] `bind()`, `listen()`, and `accept()` one connection
- [ ] `read()` the request into a buffer and print it
- [ ] `write()` back `"Hello from C!\n"` and close the connection

## Test

```bash
make && ./build/socket
# In another terminal:
curl http://localhost:8080
```

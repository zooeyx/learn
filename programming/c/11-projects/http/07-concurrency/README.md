# 07 — Multiple Clients

Use `fork()` to handle multiple clients simultaneously — one process per connection.

## Concepts

- **`fork()`**: creates a child process — parent returns to accept loop, child handles the request
- **`waitpid()` with `WNOHANG`**: reap finished child processes without blocking
- **`SIGCHLD` handler**: automatically clean up zombie processes
- **`SIGINT` handler**: catch Ctrl-C for graceful shutdown (close the listening socket)
- **Process-per-connection model**: simple concurrency — each connection gets its own process

## Exercises

- [ ] Set up a `SIGCHLD` handler that calls `waitpid(-1, NULL, WNOHANG)` in a loop
- [ ] After `accept()`, `fork()` — child handles request, parent continues accepting
- [ ] Child: close `server_fd`, handle request, `exit(0)`
- [ ] Parent: close `client_fd`, loop back to `accept()`
- [ ] Add `SIGINT` handler for clean shutdown

## Test

```bash
make && ./build/concurrency
# Open multiple browser tabs to http://localhost:8080/ simultaneously
# All should load instantly (no waiting for others to finish)
# Add a sleep(3) in handle_request to make concurrency visible
# Ctrl-C to shut down cleanly
```

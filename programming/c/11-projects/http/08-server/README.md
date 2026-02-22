# 08 — The Full Server (Multi-File)

Refactor everything into a proper multi-file C project with separate compilation, header files, and CLI arguments.

## Concepts

- **Header files + `#ifndef` guards**: declare functions/types in `.h`, define in `.c`, prevent double inclusion
- **Separate compilation**: each `.c` compiles to a `.o`, then linked together — faster rebuilds
- **`argc` / `argv`**: command-line arguments for port and document root
- **`SO_REUSEADDR`**: let the server rebind immediately after restart (avoids "Address already in use")

## Module Layout

| File | Responsibility |
|------|---------------|
| `main.c` | CLI argument parsing, startup |
| `server.c/h` | Socket setup, accept loop, fork handling |
| `http.c/h` | Request parsing, response building, MIME types |
| `file.c/h` | File reading, path validation, stat checks |

## Exercises

- [ ] Create `server.h/c` — `server_start(port)`, `server_run(server_fd, docroot)`
- [ ] Create `http.h/c` — `http_parse_request()`, `http_send_response()`, `http_get_mime_type()`
- [ ] Create `file.h/c` — `file_read()`, `file_validate_path()`, `file_get_size()`
- [ ] `main.c` — parse `argv[1]` (port) and `argv[2]` (docroot), call server functions
- [ ] Add `#ifndef` include guards to all headers

## Test

```bash
make && ./build/server 8080 ../www
# In another terminal:
curl http://localhost:8080/
curl -I http://localhost:8080/style.css
# Multiple browser tabs should work simultaneously
```

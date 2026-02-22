# 03 — The Response Builder

Send proper HTTP responses with status lines and headers. Route 3 paths and run in a loop.

## Concepts

- **HTTP response format**: `HTTP/1.0 200 OK\r\nHeader: value\r\n\r\nbody`
- **Status codes**: 200 OK, 404 Not Found — the server tells the client what happened
- **`Content-Length`**: tells the client how many bytes the body is
- **`snprintf()`**: safe, bounded string formatting — essential for building responses
- **`while(1)` accept loop**: keep the server running to handle multiple sequential requests

## Exercises

- [ ] Write a `send_response()` helper that builds a full HTTP response (status line + headers + body)
- [ ] Route `/` to a welcome page, `/about` to an about page, `/time` to the current time
- [ ] Return 404 for unknown paths
- [ ] Wrap `accept()` in a `while(1)` loop so the server keeps running

## Test

```bash
make && ./build/respond
# In another terminal:
curl -i http://localhost:8080/
curl -i http://localhost:8080/about
curl -i http://localhost:8080/time
curl -i http://localhost:8080/nope    # 404
# Server stays running — test multiple requests
```

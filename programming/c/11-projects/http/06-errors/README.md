# 06 — Error Handling and Logging

Add proper HTTP error responses, defensive request parsing, and timestamped request logging.

## Concepts

- **HTTP error codes**: 400 Bad Request, 403 Forbidden, 404 Not Found — communicate problems to the client
- **`errno` / `perror()`**: system-level error reporting for failed syscalls
- **`time()` / `strftime()`**: format timestamps for log output
- **Defensive parsing**: handle malformed requests, empty reads, oversized headers gracefully

## Exercises

- [ ] Add request logging: `[2024-01-15 14:30:00] GET /path — 200`
- [ ] Write a `log_request()` helper using `time()` + `strftime()`
- [ ] Return 400 Bad Request for unparseable request lines
- [ ] Handle empty reads (`n <= 0`) gracefully
- [ ] Test with garbage input via `nc`

## Test

```bash
make && ./build/errors
# In another terminal:
curl http://localhost:8080/             # 200, logged
curl http://localhost:8080/missing      # 404, logged
echo "GARBAGE" | nc localhost 8080      # 400, logged
echo "" | nc localhost 8080             # handled gracefully
# Check terminal for timestamped log output
```

# HTTP Server from Scratch

Build an HTTP server in C across 8 lessons — each one produces something you can test with `curl` or a browser.

## Progress

- [ ] `01-socket/` — Hello from a Socket
- [ ] `02-parse/` — Reading an HTTP Request
- [ ] `03-respond/` — The Response Builder
- [ ] `04-serve-files/` — Static File Serving
- [ ] `05-mime/` — Content Types
- [ ] `06-errors/` — Error Handling and Logging
- [ ] `07-concurrency/` — Multiple Clients
- [ ] `08-server/` — The Full Server (Multi-File)

## Build

```bash
make              # build all lessons
make clean        # clean all lessons
cd 01-socket && make && ./build/socket
```

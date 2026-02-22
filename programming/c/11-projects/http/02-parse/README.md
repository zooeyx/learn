# 02 — Reading an HTTP Request

Parse the HTTP request line to extract the method and path, then respond with HTML showing what was requested.

## Concepts

- **HTTP request format**: `METHOD /path HTTP/1.1\r\n` followed by headers, blank line, optional body
- **`sscanf()`**: parse formatted data from a string — perfect for extracting method + path
- **`\r\n` (CRLF)**: HTTP line terminator; watch for this when parsing
- **Null termination**: C strings end with `\0`; always ensure buffers are properly terminated

## Exercises

- [ ] Accept a connection and read the request (reuse socket setup from lesson 01)
- [ ] Parse the request line with `sscanf(buf, "%s %s", method, path)`
- [ ] Build an HTML response: `<h1>You requested: /path</h1>`
- [ ] Send the response string back to the client

## Test

```bash
make && ./build/parse
# In another terminal:
curl -v http://localhost:8080/hello
curl http://localhost:8080/about
# Open http://localhost:8080/test in a browser to see rendered HTML
```

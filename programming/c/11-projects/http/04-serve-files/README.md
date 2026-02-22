# 04 — Static File Serving

Map URL paths to files in a `www/` directory and serve real HTML/CSS.

## Concepts

- **Document root**: the base directory mapped to `/` — a request for `/index.html` reads `www/index.html`
- **`fopen()` / `fread()` / `fclose()`**: read file contents into a buffer
- **`stat()`**: get file metadata (size) before reading — lets you set `Content-Length` correctly
- **Path traversal**: requests containing `..` could escape the document root — block them

## Exercises

- [ ] Build a file path from the URL: `snprintf(filepath, ..., "www%s", path)`
- [ ] If path ends with `/`, append `index.html`
- [ ] Use `stat()` to check if the file exists and get its size
- [ ] Read the file contents with `fopen()` / `fread()`
- [ ] Block requests containing `..` (path traversal prevention)
- [ ] Create `www/index.html` with some test content

## Test

```bash
mkdir -p www
echo '<html><body><h1>It works!</h1></body></html>' > www/index.html
make && ./build/serve_files
# In another terminal:
curl http://localhost:8080/
curl http://localhost:8080/index.html
curl http://localhost:8080/../../../etc/passwd   # should be blocked
```

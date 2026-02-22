# 05 — Content Types

Detect file extensions and set the correct `Content-Type` header so browsers render everything properly.

## Concepts

- **MIME types**: tell the browser how to interpret a file — `text/html`, `text/css`, `image/png`, etc.
- **Struct arrays as lookup tables**: pair extensions with MIME types in a static array
- **String suffix matching**: compare the end of the filename against known extensions
- **`Content-Type` header**: without it, browsers guess (and often guess wrong for CSS/images)

## Exercises

- [ ] Create a MIME type lookup table as a struct array
- [ ] Write `get_mime_type()` — find the file extension and look it up
- [ ] Use `strrchr()` to find the last `.` in the filename
- [ ] Default to `application/octet-stream` for unknown extensions
- [ ] Integrate with file serving from lesson 04

## Test

```bash
# Create test files in www/
echo '<html><link rel="stylesheet" href="style.css"><body><h1>Styled!</h1></body></html>' > www/index.html
echo 'h1 { color: blue; }' > www/style.css
make && ./build/mime
# In another terminal:
curl -I http://localhost:8080/index.html   # Content-Type: text/html
curl -I http://localhost:8080/style.css    # Content-Type: text/css
# Open in browser — CSS should apply
```

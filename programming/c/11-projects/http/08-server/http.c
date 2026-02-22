#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include "http.h"
#include "file.h"

#define BUFSIZE 4096

// TODO: Implement MIME type lookup (move from lesson 05)
//   typedef struct { const char *ext; const char *type; } MimeEntry;
//   static const MimeEntry mime_table[] = { ... };
//   const char *http_get_mime_type(const char *path) { ... }

// TODO: Implement http_send_response()
//   Build "HTTP/1.0 STATUS TEXT\r\nContent-Type: ...\r\nContent-Length: ...\r\n\r\n"
//   Then write header + body

// TODO: Implement http_send_error()
//   Build an HTML error page and call http_send_response()

// TODO: Implement http_handle_request()
//   1. read() the request
//   2. sscanf() to parse method + path
//   3. file_validate_path() to check for traversal
//   4. file_read() to load the file
//   5. http_get_mime_type() for Content-Type
//   6. http_send_response() to send it back
//   7. Log the request with timestamp

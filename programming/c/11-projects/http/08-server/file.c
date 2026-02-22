#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include "file.h"

// TODO: Implement file_validate_path()
//   Return 0 if path contains "..", 1 if safe
//   int file_validate_path(const char *path)
//   {
//       return strstr(path, "..") == NULL;
//   }

// TODO: Implement file_get_size() using stat()
//   long file_get_size(const char *filepath)
//   {
//       struct stat st;
//       if (stat(filepath, &st) < 0) return -1;
//       return st.st_size;
//   }

// TODO: Implement file_read() — returns malloc'd buffer, caller must free
//   char *file_read(const char *filepath, long *out_size)
//   {
//       long size = file_get_size(filepath);
//       if (size < 0) return NULL;
//
//       FILE *fp = fopen(filepath, "rb");
//       if (!fp) return NULL;
//
//       char *buf = malloc(size);
//       if (!buf) { fclose(fp); return NULL; }
//
//       fread(buf, 1, size, fp);
//       fclose(fp);
//
//       if (out_size) *out_size = size;
//       return buf;
//   }

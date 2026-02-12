#ifndef DEBUG_H
#define DEBUG_H

#include <errno.h>
#include <stdio.h>
#include <string.h>

// Debug print — compiled out unless DEBUG_ON is defined
#ifdef DEBUG_ON
#define debug(fmt, ...) \
    fprintf(stderr, "[DEBUG] %s:%d: " fmt "\n", __FILE__, __LINE__, ##__VA_ARGS__)
#else
#define debug(fmt, ...)
#endif

// Log to stderr with file:line prefix
#define log_err(fmt, ...) \
    fprintf(stderr, "[ERROR] %s:%d: " fmt "\n", __FILE__, __LINE__, ##__VA_ARGS__)

// Check condition, print errno-aware message and goto error label
#define check(cond, fmt, ...)                                                    \
    do {                                                                          \
        if (!(cond)) {                                                            \
            if (errno)                                                            \
                log_err(fmt " | errno: %s", ##__VA_ARGS__, strerror(errno));      \
            else                                                                  \
                log_err(fmt, ##__VA_ARGS__);                                      \
            goto error;                                                           \
        }                                                                         \
    } while (0)

// Sentinel for unreachable code
#define sentinel(fmt, ...)                                                        \
    do {                                                                          \
        log_err(fmt, ##__VA_ARGS__);                                              \
        goto error;                                                               \
    } while (0)

#endif // DEBUG_H

#include <stdio.h>
#include <limits.h>
#include <float.h>
#include <stdbool.h>

int main(void) {
    // Integer types
    char c = 'Z';
    short s = 32767;
    int i = 2147483647;
    long l = 9223372036854775807L;

    printf("char:  '%c' (size: %zu bytes)\n", c, sizeof(c));
    printf("short: %d  (size: %zu bytes)\n", s, sizeof(s));
    printf("int:   %d  (size: %zu bytes)\n", i, sizeof(i));
    printf("long:  %ld (size: %zu bytes)\n", l, sizeof(l));

    // Floating point
    float f = 3.14f;
    double d = 3.141592653589793;

    printf("float:  %.2f  (size: %zu bytes)\n", f, sizeof(f));
    printf("double: %.15f (size: %zu bytes)\n", d, sizeof(d));

    // Boolean
    bool flag = true;
    printf("bool:   %d    (size: %zu bytes)\n", flag, sizeof(flag));

    // Limits
    printf("\nLimits:\n");
    printf("  INT_MAX:   %d\n", INT_MAX);
    printf("  INT_MIN:   %d\n", INT_MIN);
    printf("  FLT_MAX:   %e\n", FLT_MAX);
    printf("  DBL_EPSILON: %e\n", DBL_EPSILON);

    return 0;
}

#include <stdio.h>
#include <limits.h>
#include <float.h>

int main(void) {
    // sizeof — returns size in bytes
    char c = 'A';
    short s = 32000;
    int i = 120;
    long l = 1000000L;
    float f = 3.14f;
    double d = 3.14159;

    printf("=== sizeof each type ===\n");
    printf("char:   %zu byte\n", sizeof c);
    printf("short:  %zu bytes\n", sizeof s);
    printf("int:    %zu bytes\n", sizeof i);
    printf("long:   %zu bytes\n", sizeof l);
    printf("float:  %zu bytes\n", sizeof f);
    printf("double: %zu bytes\n", sizeof d);

    // limits — min/max values each type can hold
    printf("\n=== integer limits ===\n");
    printf("char:  %d to %d\n", CHAR_MIN, CHAR_MAX);
    printf("short: %d to %d\n", SHRT_MIN, SHRT_MAX);
    printf("int:   %d to %d\n", INT_MIN, INT_MAX);
    printf("long:  %ld to %ld\n", LONG_MIN, LONG_MAX);

    printf("\n=== unsigned limits ===\n");
    printf("unsigned char:  0 to %u\n", UCHAR_MAX);
    printf("unsigned short: 0 to %u\n", USHRT_MAX);
    printf("unsigned int:   0 to %u\n", UINT_MAX);
    printf("unsigned long:  0 to %lu\n", ULONG_MAX);

    printf("\n=== float limits ===\n");
    printf("float min:  %e\n", FLT_MIN);
    printf("float max:  %e\n", FLT_MAX);
    printf("double min: %e\n", DBL_MIN);
    printf("double max: %e\n", DBL_MAX);

    // overflow — what happens when you exceed the max?
    printf("\n=== overflow ===\n");
    unsigned char uc = 255;
    printf("unsigned char at max: %u\n", uc);
    uc = uc + 1;
    printf("unsigned char + 1:    %u\n", uc);  // wraps to 0

    return 0;
}

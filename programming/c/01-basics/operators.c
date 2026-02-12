#include <stdio.h>

int main(void) {
    // Arithmetic
    int a = 17, b = 5;
    printf("Arithmetic: %d + %d = %d\n", a, b, a + b);
    printf("Arithmetic: %d %% %d = %d (modulo)\n", a, b, a % b);

    // Comparison
    printf("\nComparison: %d > %d = %d\n", a, b, a > b);
    printf("Comparison: %d == %d = %d\n", a, b, a == b);

    // Logical
    int x = 1, y = 0;
    printf("\nLogical: %d && %d = %d\n", x, y, x && y);
    printf("Logical: %d || %d = %d\n", x, y, x || y);
    printf("Logical: !%d = %d\n", x, !x);

    // Bitwise
    unsigned int m = 0xF0, n = 0x0F;
    printf("\nBitwise: 0x%X & 0x%X = 0x%X\n", m, n, m & n);
    printf("Bitwise: 0x%X | 0x%X = 0x%X\n", m, n, m | n);
    printf("Bitwise: 0x%X ^ 0x%X = 0x%X\n", m, n, m ^ n);
    printf("Bitwise: 0x%X << 4 = 0x%X\n", n, n << 4);

    // Ternary
    int max = (a > b) ? a : b;
    printf("\nTernary: max(%d, %d) = %d\n", a, b, max);

    return 0;
}

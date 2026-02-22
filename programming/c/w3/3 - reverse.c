#include <stdio.h>

int main(void) {
    // declare and initialize char variables
    char char1 = 'X';
    char char2 = 'M';
    char char3 = 'Z';

    // print original and reversed
    printf("Normal:\t\t%c%c%c\nReversed:\t%c%c%c\n",
        char1, char2, char3,
        char3, char2, char1);

    return 0;
}

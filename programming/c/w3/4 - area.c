#include <stdio.h>

int main(void) {
    int width = 5;
    int height = 7;
    int perimeter = 2 * (height + width);
    int area = (height * width);

    printf("AREA:\t\t%d cm\nPERIMETER:\t%d cm", area, perimeter);
    return 0;
}

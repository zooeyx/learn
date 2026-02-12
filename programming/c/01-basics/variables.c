#include <stdio.h>

int main(void) {
    // Declaration and initialization
    int age = 25;
    float height = 5.9f;
    char initial = 'A';

    printf("Age: %d\n", age);
    printf("Height: %.1f\n", height);
    printf("Initial: %c\n", initial);

    // Assignment
    age = 26;
    printf("Next year: %d\n", age);

    // Constants
    const int DAYS_IN_WEEK = 7;
    printf("Days in a week: %d\n", DAYS_IN_WEEK);

    return 0;
}

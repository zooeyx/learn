#include <stdio.h>
#include <math.h>

// Area/circumference of a circle:
// A = pi * r^2
// C = 2 * pi * r

int main(void) {
    double r;

    printf("Enter the radius of a circle: ");
    if (scanf("%lf", &r) != 1 || r < 0.0) {
        fprintf(stderr, "Invalid radius.\n");
        return 1;
    }

    // Safer than M_PI (which isn't guaranteed by the C standard everywhere)
    const double pi = acos(-1.0);

    double circumference = 2.0 * pi * r;
    double area = pi * r * r;     // r*r is the simplest and fastest "r^2"

    printf("Circumference = %.2f\n", circumference);
    printf("Area          = %.2f\n", area);

    return 0;
}

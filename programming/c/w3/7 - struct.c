#include <stdio.h>
#include <math.h>

const double PI = 3.14159265358979323846;

typedef struct {
    double circumference;
    double area;
    double radius;
} Circle;

Circle circle_create(double r){
    Circle c;
    c.radius = r;
    c.circumference = 2.0 * PI * r;
    c.area = PI * pow(r, 2.0);
    return c;
}

void circle_print(Circle c) {
    printf("Radius:\t\t %.2f\n", c.radius);
    printf("Circumference:\t %.2f\n", c.circumference);
    printf("Area:\t\t %.2f\n", c.area);
}

int main(void) {
    double r;

    printf("Enter radius: ");
    if (scanf("%lf", &r) != 1 || r < 0.0) {
        fprintf(stderr, "Invalid radius.\n");
        return 1;
    }

    Circle c = circle_create(r);
    circle_print(c);

    return 0;
}

#include <stdio.h>
#include "add.h"
int a;

int main( )
{	
	a = rand() %100;
	printf("Rand a: %d\n", a);
	int b = rand() %100; 
	printf("Rand b: %d\n", b);

	int sum = foo(a,b);
	printf("Sum from main: %d\n", sum);

	return 0;
}

int foo(int a, int b){
	int sum = a + b;
	printf("Sum from foo: %d\n",sum);
	return sum; 
}

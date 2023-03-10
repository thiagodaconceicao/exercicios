#include <stdio.h>

int main(){
	int num;
	int num2;
	int num3;
	
	printf("digite um numero: ");
	scanf("%d", &num);
	
	num2 = num + 1;
	num3 = num - 1;
	
	printf("o numero: %d\n", num);
	printf("seu sucessor: %d\n", num2);
	printf("seu antecessor: %d\n", num3);
	
	getchar();
	return 0;
}
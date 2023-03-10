#include <stdio.h>

int main(){
	int num;
	int num_2;
	
	printf("digite um numero: ");
	scanf("%d", &num);

	printf("numero: %d\n", num);
	
	printf("digite outro numero: ");
	scanf("%d", &num_2);
	
	printf("numero 2: %d\n", num_2);
	
	getchar();
	return 0;
}
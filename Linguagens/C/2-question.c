#include <stdio.h>


int main() {
	char nome[10]; 
	printf("qual seu nome? ");
	gets(nome);
	
	printf("seu nome é: %s", nome);
	
	getchar();
	return 0;
}
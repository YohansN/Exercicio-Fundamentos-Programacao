/*Q002: Fazer um algoritmo para calcular e imprimir o fatorial de um número qualquer fornecido pelo usuário.
(lembrando: fatorial de 0! = 1; fatorial de 1! = 1; Fatorial de N! = (N * N-1!);*/

#include <stdio.h>
int main(){
	int num, fat;
	scanf("%d", &num);
	for(fat = 1; num > 1; num = num-1){
		fat = fat * num;
	}
	printf("%d", fat);
}

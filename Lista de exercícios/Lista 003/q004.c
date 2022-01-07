/*Q004: Fazer um algoritmo para ler 10 números inteiros quaisquer e informar quantos e quais são os números
primos.*/

#include <stdio.h>
int main(){
	int i, j, num, primo, contador, resto, num_primos;
	contador = 0;
	num_primos = 0;
	for(j = 1; j < 11; j++){
		scanf("%d", &num);
		i = 1;
		while(i <= num){
			resto = num % i;
			if(resto == 0){
				contador = contador + 1;
			}
			i = i+1;
		}
		if(contador == 2){
			printf("%d É primo! \n", num);
			num_primos = num_primos + 1;
		}
		contador = 0;
	}
	printf("Total de numeros primos: %d", num_primos);
}


/*Q003: A série fibonacci é formada pele seguinte sequência: 1, 1, 2, 3, 5, 8, 13, 13, 21, 34, 55...etc. Escreva um
algoritmo que gere a serie fibonacci até o 12o termo;*/

#include <stdio.h>
int main(){
	int num, anterior, i, n;
	anterior = 0;
	num = 1;
	//loop
	for(i = 1; i < 13; i++){ 
		printf("%d \n", num);
		n = num;
		num = num + anterior;
		anterior = n;	
	}
}

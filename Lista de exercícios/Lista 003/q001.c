/*Q001: Fazer um algoritmo para ler 10 números digitados pelo usuário e depois informar qual maior valor e qual
menor valor informado;*/

#include <stdio.h>
int main() {
    int valor, maior_valor, novo_valor, menor_valor, c, i;
    maior_valor = 0;
    menor_valor = 10000;
    for(i = 1; i <= 10; i++){
        printf("Escreva o %d° valor: ", i);
        scanf("%d", &valor);
        if(valor > maior_valor){ 
            maior_valor = valor;
        }
        else if(valor < menor_valor){
            menor_valor = valor;
        }
    }
    printf("O maior valor foi: %d. O menor valor foi: %d. \n", maior_valor , menor_valor);
}

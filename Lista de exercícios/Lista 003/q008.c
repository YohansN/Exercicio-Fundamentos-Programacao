/*Q008: Construa um algoritmo para ler salários de 10 funcionários de uma empresa e depois calcular e informar:
- maior salário;
- menor salário;
- média salarial;
- imposto de renda, levando em consideração (até R$ 1.500 – isento; maior que R$ 1.500 e menor ou igual a R$ 2.000 – descontar 10%; maior que R$ 2.000 – descontar 15%);
- salário liquido a receber;*/

#include <stdio.h>
int main(){
    float salario, maior, menor, media, imposto, liquido, soma;
    int i;
    soma = 0;
    maior = 0;
    menor = 1000000000000;
    for(i=1; i<11; i++){
        printf("Valor do %dº salario:\n", i);
        scanf("%f", &salario);
        //Calculo imposto de renda
        if(salario > 1500 && salario <= 2000){
            liquido = salario * 90/100;
            salario = liquido;
            printf("Valor salario liquido: R$%.2f\n", liquido);
        }
        else if(salario > 2000){
            liquido = salario * 85/100;
            salario = liquido;
            printf("Valor salario liquido: R$%.2f\n", liquido);
        }
        if(salario > maior){
            maior = salario;
        }
        else if(salario < menor){
            menor = salario;
        }
        soma = soma + salario;
    }
    //Dados finais
    printf("Maior salario: R$ %.2f\n", maior);
    printf("Menor salario: R$ %.2f\n", menor);
    media = soma / 10;
    printf("Media Salarial: R$ %.2f\n", media);
}

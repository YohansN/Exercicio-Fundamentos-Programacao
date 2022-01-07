/*Q005: Faça um algoritmo que leia a data de nascimento de 10 pessoas, depois calcule a idade de cada uma,
informando-a. E, por último, mostre qual a pessoa mais jovem e a mais velha do grupo.*/

#include <stdio.h>
int main()
{
    int ano, idade, jovem, velha, i, ano_jovem, ano_velha;
    jovem = 1000;
    velha = 0;
    for(i = 1; i<11; i++){
        printf("Digite o %d° ano de nascimento: ", i);
        scanf("%d", &ano);
        idade = 2021 - ano;
        printf("Idade: %d anos. \n", idade);
        printf("------------------------------------ \n");
        if(idade < jovem){
            jovem = idade;
            ano_jovem = ano;
        }
        else if(idade > velha){
            velha = idade;
            ano_velha = ano;
        }
    }
    printf("A pessoa mais jovem tem %d anos e nasceu em %d. \n", jovem, ano_jovem);
    printf("A pessoa mais velha tem %d anos e nasceu em %d. ", velha, ano_velha);
}

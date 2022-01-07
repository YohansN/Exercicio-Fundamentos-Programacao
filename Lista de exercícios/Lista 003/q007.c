/*Q007: Faça um algoritmo para ler o peso e altura de 10 pessoas, em seguida, deve-se exibir o resultado, conforme
os dados da tabela abaixo.*/

#include <stdio.h>
#include <math.h>
int main(){
    float imc, alt, peso, pot_alt;
    int i = 1;
    while(i != 11){
        printf("CLASSIFICAÇÃO IMC: Nº%d de 10\n", i);
        printf("Digite o peso: ");
        scanf("%f", &peso);
        printf("Digite a altura: ");
        scanf("%f", &alt);
        pot_alt = pow(alt,2);
        imc = peso/pot_alt;
        printf("IMC: %.2f \n",imc);
        if(imc < 18.5){
            printf("abaixo do peso \n");
        }
        else if(18.5 <= imc && imc <= 24.9){
            printf("Peso normal \n");
        }
        else if(25 <= imc && imc <= 29.9){
            printf("Sobrepeso \n");
        }
        else if(30 <= imc && imc <= 34.9){
            printf("Obesidade grau 1 \n");
        }
        else if(35 <= imc && imc <= 39.9){
            printf("Obesidade grau 2 \n");
        }
        else{
            printf("Obesidade grau 3 ou Morbida \n");
        }
        i++;
    }
    printf("Fim");
}

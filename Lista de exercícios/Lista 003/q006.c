/*Q006: Fazer um algoritmo para calcular e imprimir a media aritmética de 10 alunos, tendo como dados de entrada
3 notas semestrais. Depois imprimir situação do aluno que deve obedecer ao seguinte critério: (media maior
ou igual a 7, “aprovado”; entre 4 e 6.9, “AF”; menor que 4, “reprovado”), depois imprimir a media geral da
turma;*/

#include <stdio.h>
int main(){
    float n1, n2, n3, media, soma_medias, media_geral;
    int i, j;
    soma_medias = 0;
    for(i=1; i < 11; i++){
        printf("-----------------------------------\n");
        printf("Digita 3 notas: \n");
        scanf("%f", &n1);
        scanf("%f", &n2);
        scanf("%f", &n3);
        media = (n1 + n2 + n3)/3;
        printf("Media %dº aluno: %.1f \n", i, media);
        soma_medias = soma_medias + media;
        if(media >= 7){
            printf("Aprovado\n");
        }
        else if(4 <= media && media <= 6.9){
            printf("AF\n");
        }
        else if(media < 4){
            printf("Reprovado\n");
        }
    }
    media_geral = soma_medias/10;
    printf("A media geral da turma é: %.1f", media_geral);
}

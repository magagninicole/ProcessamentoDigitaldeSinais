/***************************
 * media_movel.c
 ***************************/
#include <stdio.h>
#define tam 320

#pragma symbolic_ref
const char __argv_string[] = "-abc -xyz";

int main( int argc, char *argv[] )
{
	
	FILE *fin,*fout;
    int i, n, sample;

    short entrada, saida;
    short data[tam] = {0x0};
    float y = 0;

    float coef[tam] = {
        #include "Coef_RF.dat" 
    };

    
	fin = fopen("..\\sweep_100_2k.pcm","rb");
    if ((fin)==NULL){
    	printf("\nErro: nao abriu o arquivo de Entrada\n");
    	return 0;
  	}
  	
    fout = fopen("..\\sai_audio_tst.pcm","wb");
    if ((fout)==NULL){
    	printf("\nErro: nao abriu o arquivo de Saida\n");
    	return 0;
  	}
 

    for (i = 0; i < tam; i++){
        data[i] = 0;
    }

    do {
        y = 0;
        sample = fread(&entrada, sizeof(short), 1, fin);
        data[0] = entrada;
        for (n = 0; n < tam; n++){
                y += coef[n] * data[n];
        }
        for (n = tam - 1; n > 0; n--){
                data[n] = data[n - 1];
        }
        saida = (short)y;

        fwrite(&saida, sizeof(short), 1, fout);
    } while (sample);

    fclose(fout);
    fclose(fin);
	
	return 0;
}
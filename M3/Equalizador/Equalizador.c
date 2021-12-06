/***************************
 * Equalizador.c
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
    float ganho_pb =0.7, ganho_pa=0.5, ganho_pf=0.6;
    float saida_pb =0, saida_pa=0, saida_pf=0;

    float coef_pb[tam] = {
        #include "Coef_PB.dat" 
    };

    float coef_pa[tam] = {
        #include "Coef_PA.dat" 
    };

    float coef_pf[tam] = {
        #include "Coef_PF.dat" 
    };

    
	fin = fopen("..\\sweep_100_2k.pcm","rb");
    if ((fin)==NULL){
    	printf("\nErro: Não foi possível abrir o arquivo de entrada.\n");
    	return 0;
  	}
  	
    fout = fopen("..\\saida_equalizador.pcm","wb");
    if ((fout)==NULL){
    	printf("\nErro: Não foi possível abrir o arquivo de saída.\n");
    	return 0;
  	}
 

    for (i = 0; i < tam; i++){
        data[i] = 0;
    }

       
    do {
    	saida_pb =0, saida_pa=0, saida_pf=0;
 		y = 0;
        sample = fread(&entrada, sizeof(short), 1, fin);
 		data[0] = entrada;
 		
        for (n = 0; n < tam; n++){
        	
               saida_pb += coef_pb[n] * data[n] * ganho_pb;
               saida_pa += coef_pa[n] * data[n] * ganho_pa;
               saida_pf += coef_pf[n] * data[n] * ganho_pf;
               
           y = saida_pb + saida_pa + saida_pf;
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

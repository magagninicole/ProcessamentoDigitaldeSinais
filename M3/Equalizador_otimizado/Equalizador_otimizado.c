/*****************************************************************************
 * Equalizador_otimizado.c
 *****************************************************************************/

#include <stdio.h>
#include <cycles.h>

#define tam 320


int main( int argc, char *argv[] )
{
	cycle_stats_t stats;
	
	FILE *fin,*fout;
    int i,sample;

    short entrada, saida;
    short data[tam] = {0};
    int y = 0;
    short ganho_pb =1, ganho_pa=1, ganho_pf=1;
    int saida_pb =0, saida_pa=0, saida_pf=0;
    

	short coef_pb[tam] = {
    	#include "coefs_short_PB.dat" 
    };

	short coef_pa[tam] = {
    	#include "coefs_short_PA.dat" 
    };

	short coef_pf[tam] = {
    	#include "coefs_short_PF.dat" 
    };
    
    
    CYCLES_INIT(stats);

	fin = fopen("..\\sweep_100_2k.pcm","rb");
    if ((fin)==NULL){
    	printf("\nErro: Não foi possível abrir o arquivo sweep.\n");
    	return 0;
  	}
  	
    fout = fopen("..\\saida_equalizador.pcm","wb");
    if ((fin)==NULL){
    	printf("\nErro: Não foi possível abrir o arquivo equalizador.\n");
    	return 0;
  	}
 

    for (i = 0; i < tam; i++){
        data[i] = 0;
    }

       
    do {
    	saida_pb =0, saida_pa=0, saida_pf=0;
 		y = 0;
        sample = fread(&entrada, sizeof(short), 1, fin);
        CYCLES_START(stats);
 		data[0] = entrada;
 		
        for (i = 0; i < tam; i++){
               saida_pb += coef_pb[i] * data[i] * ganho_pb;
               saida_pa += coef_pa[i] * data[i] * ganho_pa;
               saida_pf += coef_pf[i] * data[i] * ganho_pf;
               
           	   y = saida_pb + saida_pa + saida_pf;
        }
        for (i = tam - 1; i > 0; i--){
                data[i] = data[i - 1];
        }
        
        saida = y>>15;
        CYCLES_STOP(stats);

        fwrite(&saida, sizeof(short), 1, fout);
    } while (sample);
    
    CYCLES_PRINT(stats);

    fclose(fin);
    fclose(fout);
	
	return 0;
}

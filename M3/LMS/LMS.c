#include <stdio.h>

#pragma symbolic_ref
const char __argv_string[] = "-abc -xyz";

int main( int argc, char *argv[] )
{
	int amostras;
	short x;
	
	
    float coefs[8] = {
        #include "Coef_MM_8.dat" // Coeficiente
    };
    
    FILE *x_file;
	x_file = fopen("..\\ruidobranco.pcm","rb"); // entrada
    if ((x_file)==NULL){
    	printf("\nErro: nao abriu o arquivo de Entrada\n");
    	return 0;
  	}
    
 	amostras = fread(&x, sizeof(short), 1, x_file);
 	printf("%d", amostras);

    
    fclose(x);
	
	return 0;
}
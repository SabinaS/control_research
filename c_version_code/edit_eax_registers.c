#include <stdio.h>
#include <string.h>

int main ( void )
{
   static const char filename[] = "add_output.txt";
   FILE *file = fopen ( filename, "r" );
   if ( file != NULL )
   {
      char line [ 128 ]; /* or other suitable maximum line size */
      while ( fgets ( line, sizeof line, file ) != NULL ) /* read a line */
      {
         char beginning = line[0];
         char reg= '0'; 
         if(strcmp(beginning, "e") == 0){
            printf("EAX: &s\n", line);
         }
      }
      fclose ( file );
   }
   else
   {
      perror ( filename ); /* why didn't the file open? */
   }
   return 0;
}

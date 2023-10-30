#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILENAME "input.txt"
#define ARRAYLEN(x)  (sizeof(x) / sizeof((x)[0]))

void updateTop(int *top, int length, int candidate){

    for (int i = length - 1; i >= 0; i--){
        if (candidate > top[i]){
          int prev = top[i];
          top[i] = candidate;
          updateTop(top, i, prev);
          break;
        }
    }
}


void printTop(char *message, int *top, int length){

    int total = 0;
    char numToCh[20];
    
    for (int i = 0; i < length; i++){
        total += top[i];
        sprintf(numToCh, " %d", top[i]);
        strcat(message, numToCh);
    } 

    printf("%s ]; ", message);
    printf("Total top value: %i\n", total);
}


int main(){

    int elf_value = 0;
    
    int max_value = 0; // PART 1
    int top3[3] = {0}; // PART 2
    
    int length = ARRAYLEN(top3);

    FILE *fptr;
    fptr = fopen(FILENAME, "r");

    if (fptr == NULL){
        printf("[ERROR] could not read input file\n");
        return -1;
    } 

    char *line ;
    int num;
    size_t len = 0;
    size_t read;

    while ((read = getline(&line, &len, fptr)) != -1)
    {
        if (*line == '\n') {
            // PART 1
            max_value = elf_value > max_value ? elf_value : max_value;

            // PART 2
            updateTop(top3, length, elf_value);

            elf_value = 0;
            continue;
        }

        sscanf(line, "%d", &num);

        elf_value += num;
    }
   
    printf("Max value: %i\n", max_value);

    char msg[30];
    strcpy(msg, "Top 3 values: ["); 
    printTop(msg, top3, length);

    return 1;
}

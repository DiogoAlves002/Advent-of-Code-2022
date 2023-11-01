#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h> 

#define FILENAME "input.txt"
//#define FILENAME "test.txt"


int main(){

    FILE *fptr;
    fptr = fopen(FILENAME, "r");

    if (fptr == NULL){
        printf("[ERROR] could not read input file\n");
        return -1;
    }

    size_t read;
    char *line;
    size_t len = 0;

    size_t middle_point;
    char *first_sack;
    char *second_sack;

    char item;
    char* char_from_item_idx;
    int item_value;

    int total = 0;


    while ((read = getline(&line, &len, fptr)) != -1){
        middle_point = strlen(line) / 2;

        first_sack = malloc(middle_point+1); // one for the null terminator
        memcpy(first_sack, line, middle_point);
        first_sack[middle_point] = '\0';

        second_sack = malloc(middle_point+1); // one for the null terminator
        memcpy(second_sack, line+middle_point, middle_point);
        second_sack[middle_point] = '\0';


        for (int i = 0; i < middle_point; i++){
            item = first_sack[i];

            char_from_item_idx = strchr(second_sack, item);

            if (char_from_item_idx == NULL){
                continue;
            }            

            item_value = isupper(item) ? item - 'A' + 1 + 26 : item - 'a' + 1;
            
            total += item_value;
            break;
        }
        
        free(first_sack);
        free(second_sack);
    }

    printf("Part 1: %d\n", total);

    return 0;
}
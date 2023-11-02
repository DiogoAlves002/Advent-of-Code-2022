#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h> 

#define FILENAME "input.txt"
//#define FILENAME "test.txt"


struct part1_args{
    char *line; 
    size_t middle_point;
    char *first_sack;
    char *second_sack;
    char item;
    char* str_from_item_idx;
    int item_value;
    int *total;
};
typedef struct part1_args args_1;

struct part2_args{
    char item;
    char *str_from_item_idx;
    int item_value;
    char group[3][50];
    int *total_2;
};
typedef struct part2_args args_2;

void part1(args_1 *args){
    args->middle_point = strlen(args->line) / 2;
    
    args->first_sack = malloc(args->middle_point + 1); // one for the null terminator
    memcpy(args->first_sack, args->line, args->middle_point);
    args->first_sack[args->middle_point] = '\0';

    args->second_sack = malloc(args->middle_point + 1); // one for the null terminator
    memcpy(args->second_sack, args->line + args->middle_point, args->middle_point);
    args->second_sack[args->middle_point] = '\0';


    for (int i = 0; i < args->middle_point; i++){
        args->item = args->first_sack[i];

        args->str_from_item_idx = strchr(args->second_sack, args->item);

        if (args->str_from_item_idx == NULL){
            continue;
        }            
        
        args->item_value = isupper(args->item) ? args->item - 'A' + 1 + 26 : args->item - 'a' + 1;
        
        *args->total += args->item_value;
        break;
    }
    
    free(args->first_sack);
    free(args->second_sack);
}

void part2(args_2 *args){
    for (int i = 0; i < strlen(args->group[0]); i++){
        args->item = args->group[0][i];

        // search in the second group 
        args->str_from_item_idx = strchr(args->group[1], args->item);

        if (args->str_from_item_idx == NULL){
            continue;
        }            
        
        // search in the third group 
        args->str_from_item_idx = strchr(args->group[2], args->item);

        if (args->str_from_item_idx == NULL){
            continue;
        }            

        args->item_value = isupper(args->item) ? args->item - 'A' + 1 + 26 : args->item - 'a' + 1;
        *args->total_2 += args->item_value;
        break;
    }
}



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

    // part 1
    int total = 0;

    args_1 args_1;
    args_1.total = &total;        

    // part 2
    int count = 0;
    int total_2 = 0;

    args_2 args_2;
    args_2.total_2 = &total_2;


    while ((read = getline(&line, &len, fptr)) != -1){

        // part 1
        args_1.line = line;

        part1(&args_1);


        // part 2
        strcpy(args_2.group[count], line);

        if (count == 2){ // end of group
            part2(&args_2);
            count = 0;
        } else{
            count++;
        }
    }

    printf("Part 1: %d\n", total);
    printf("Part 2: %d\n", total_2);
    
    return 0;
}
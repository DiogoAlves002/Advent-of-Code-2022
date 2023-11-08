#include <stdio.h>
#include <string.h>
#include <stdlib.h> 

struct elf{
	char* section;
	int start;
	int end;
};


/* parse line to set the elfs values*/
void setElfs(char *line, struct elf *elf_1, struct elf *elf_2){

	elf_1->section = strtok(line, ",");	
	elf_2->section = strtok(NULL, ",");	

	elf_1->start = atoi(strtok(elf_1->section, "-"));
	elf_1->end =  atoi(strtok(NULL, "-"));

	elf_2->start = atoi(strtok(elf_2->section, "-"));
	elf_2->end =  atoi(strtok(NULL, "-"));

}

/* returns 1 if elf_2 is contained in elf_1 else 0*/
int is_contained(struct elf *elf_1, struct elf *elf_2){

	return (elf_1->start <= elf_2->start && elf_1->end >= elf_2->end) ? 1 : 0;
}

/* increments total if either elf is contained within the other */
void check_any_contained(int *total, struct elf *elf_1, struct elf *elf_2){
	if (is_contained(elf_1, elf_2) == 1 || is_contained(elf_2, elf_1) == 1){
		++*total;
	} 
}


/* returns 1 if elf_2 overlaps elf_1 on the right boundary else 0*/
int is_overlaped_on_the_right(struct elf *elf_1, struct elf *elf_2){

	return (elf_1->start <= elf_2->start && elf_1->end >= elf_2->start) ? 1: 0;
}

/* increments total if the elfs are overlaped */
void check_any_overlaped(int *total, struct elf *elf_1, struct elf *elf_2){
	if (is_overlaped_on_the_right(elf_1, elf_2) == 1 || is_overlaped_on_the_right(elf_2, elf_1) == 1){
		++*total;
	} 
}


int main(int argc, char **argv){

	if (argc != 2){
		printf("[ERROR] invalid number of args\n");
		printf("[ERROR] program usage: ./exec (\'test\' || \'input\')\n");
		return -1;
	}	


	FILE *fptr;
	char file_name[10];

	strcpy(file_name, argv[1]);
	strcat(file_name, ".txt");


    fptr = fopen(file_name, "r");

    if (fptr == NULL){
        printf("[ERROR] could not read input file\n");
        return -1;
    }

	int contains_total = 0;
	int overlaps_total = 0;
	struct elf elf_1;
	struct elf elf_2;
	
	

    char *line ;
    size_t len = 0;
    size_t read;

    while ((read = getline(&line, &len, fptr)) != -1)
    {
		setElfs(line, &elf_1, &elf_2);	

		check_any_contained(&contains_total, &elf_1, &elf_2);

		check_any_overlaped(&overlaps_total, &elf_1, &elf_2);
    }
   

	printf("part 1: %d\n", contains_total);
	printf("part 2: %d\n", overlaps_total);


	return 0;
}

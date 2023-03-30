#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//this function takes the inputted numbers passed to through the command line and returns the pointer to the array in heap 
int *arrayhelperforreal(char *mystr) {
	int *returnarray;
	returnarray = (int*)malloc(sizeof(int));
	int offset = 0, lastknown = 0, elements = 0;
	char *strrep;
	while (*(mystr+offset) != '\0') {
		if (*(mystr+offset) == ',') {
			strrep = (char*)calloc(offset-lastknown, sizeof(char));
			for (int i = 0; i < offset - lastknown; i++) {
				*(strrep+i) = *(mystr+lastknown+i);
			}
			*(returnarray+elements) = atoi(strrep);
			free(strrep);
			lastknown = offset;
			offset++;
			elements++;
		} else {
			printf("This is the current offset value %d\n", offset);
			offset++;
		}
	}
	return returnarray;
}

int main(int argc, char *argv[]){
	printf("print argument %s\n", argv[1]); //1,2,3,4
	int *heaparray;

	heaparray = arrayhelperforreal(argv[1]);
	printf("This is the first element in my array %d\n", *heaparray);
	return 1;
}

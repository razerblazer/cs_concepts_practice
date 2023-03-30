#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//this function takes the inputted numbers passed to through the command line and returns the pointer to the array in heap 
int *arrayhelper(char *mystr) {
	int *returnarray;
	returnarray = (int*)malloc(sizeof(int));
	int offset = 0, lastknown = 0, elements = 0;
	char *strrep;
	while (*(mystr+offset) != '\0') {
		if (*(mystr+offset) == ',') {
			returnarray = (int*)realloc(returnarray,sizeof(int)*(elements+1));
			strrep = (char*)calloc(1,sizeof(char));
			for (int i = 0; i < offset - lastknown; i++) {
				*(strrep+i) = *(mystr+lastknown+i);
			}
			printf("The string stored by strrep is %s\n", strrep);
			*(returnarray+elements) = atoi(strrep);
			printf("int value %d\n", (atoi(strrep)));
			lastknown = offset+1;
			offset++;
			elements++;
			free(strrep);
		} else {
			offset++;
		}
	}
	return returnarray; //return pointer to integer array in heap
}

int main(int argc, char *argv[]){
	printf("print argument %s\n", argv[1]); //1,2,3,4
	int *heaparray;

	heaparray = arrayhelper(argv[1]);
	printf("This is the first element in my array %d\n", *heaparray);
	printf("This is an element that is out of range in my array %p\n",*(heaparray+343244));
	return 1;
}

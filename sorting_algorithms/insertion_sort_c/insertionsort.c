#include <stdio.h>
#include <string.h>
#include <stdlib.h>


//struct 
struct myStruct {
	int *pointer;
	int size;
};

//this function takes the inputted numbers passed to through the command line and returns the pointer to the array in heap 
struct myStruct arrayhelper(char *mystr) {
	int *returnarray;
	returnarray = (int*)malloc(sizeof(int));
	int offset = 0, lastknown = 0, elements = 0;
	char *strrep;
	while (1) {
		if (*(mystr+offset) == ',' || *(mystr+offset) == '\0') {
			returnarray = (int*)realloc(returnarray,sizeof(int)*(elements+1));
			strrep = (char*)calloc(1,sizeof(char));
			for (int i = 0; i < offset - lastknown; i++) {
				*(strrep+i) = *(mystr+lastknown+i);
			
			}
			*(returnarray+elements) = atoi(strrep);
			elements++;
			free(strrep);
			if (*(mystr+offset) == '\0') {
				break;
			}
			lastknown = offset+1;
			offset++;
		} else {
			offset++;
		}
	}
	struct myStruct s1;
	s1.pointer = returnarray;
	s1.size = elements;
	return s1; //returns struct containing size of the array and pointer to the start of the int array
}

int main(int argc, char *argv[]){
	printf("print argument %s\n", argv[1]); //takes argument input
	struct myStruct myarray;

	myarray = arrayhelper(argv[1]);
	printf("This is the first element in my array %d\n", *(myarray.pointer));
	printf("This is the size of the array %d\n", myarray.size);
	printf("This is the inputted array\n");
	for (int x = 0; x < myarray.size; x++) {
		if (x != myarray.size - 1){
			printf("%d,", *(myarray.pointer+x)); 
		} else {
		printf("%d", *(myarray.pointer+x));
		}
	}	
	printf("\n");
	return 1;
}

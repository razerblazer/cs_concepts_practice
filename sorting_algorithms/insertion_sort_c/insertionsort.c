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
			if (*(mystr+offset) == '\0') {
				break;
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
	struct myStruct s1;
	s1.pointer = returnarray;
	s1.size = elements+1;
	return s1; //return pointer to integer array in heap
}

int main(int argc, char *argv[]){
	printf("print argument %s\n", argv[1]); //1,2,3,4
	struct myStruct myarray;

	myarray = arrayhelper(argv[1]);
	printf("This is the first element in my array %d\n", *(myarray.pointer));
	printf("This is the size of the array %d\n", myarray.size);
//	printf("This is an element that is out of range in my array %d\n",*(heaparray+1));
//	for (int i=0, i < sizeof(heaparray))
	return 1;
}

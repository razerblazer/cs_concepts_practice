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

//has time of O(N^2) for the worst case scenario and O(N) for the best case scenario(which is literally the case in which the list is already sorted so whats the point of even using this sort)
void sort_logic(struct myStruct array) {
	int *arraypointer;
	arraypointer = array.pointer;
	for (int index = 1; index < array.size; index++) {
		int temp = index;
			
		while (temp >= 1 && (*(array.pointer+temp-1) > *(array.pointer+temp))){
			int storenum = *(array.pointer+temp-1);
			*(array.pointer+temp-1) = *(array.pointer+temp);
			*(array.pointer+temp) = storenum;
			temp--;
		}
	}
}

int main(int argc, char *argv[]){
	struct myStruct myarrayinfo;
	myarrayinfo = arrayhelper(argv[1]);
	printf("This is the inputted array\n");
	for (int x = 0; x < myarrayinfo.size; x++) {
		if (x != myarrayinfo.size - 1){
			printf("%d,", myarrayinfo.pointer[x]); 
		} else {
		printf("%d", myarrayinfo.pointer[x];
		}
	}
	printf("\n");
	printf("This is the array after being sorted\n");
	sort_logic(myarrayinfo); //the struct contains the pointer to the array in heap so we can just perform an inplace sort and print the new array once the sort is finished
	for (int y = 0; y < myarrayinfo.size; y++) {
		if (y != myarrayinfo.size - 1) {
			printf("%d,", myarrayinfo.pointer[y]));
		} else {
			printf("%d", myarrayinfo.pointer[y]);
		}
	}
	printf("\n");
	return 1;
}

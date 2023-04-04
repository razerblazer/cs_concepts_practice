#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Node {
	int value;
	struct Node *next;
};

void leetcode_add_two_numbers(){
	

	return;
}

int main() {
	struct Node *linkingtime;
	struct Node *current;
		
	
	int mylist[10] = {1,2,3,4,5,6,7,8,9,10};
	linkingtime = (struct Node*)(malloc(sizeof(struct Node)));
	current = linkingtime;
	for (int i=0; i < sizeof(mylist)/sizeof(int); i++) {
		(*current).value = mylist[i];
		(*current).next = (struct Node*)malloc(sizeof(struct Node));
		current = (*current).next;
	}
	printf("This is the linked list\n");
	(*current).next = NULL;
	current = linkingtime;
	while ((*current).next) {
		printf("%d -> ", (*current).value);
		current = (*current).next;
	}
	printf("NULL \n");
	return 1;

}

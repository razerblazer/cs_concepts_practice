#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Node {
	int value;
	struct Node *next;
};
//the digits are stored in reverse order and each node contains a single digit; add the two numbers and return the sum as a linked list
struct Node *leetcode_add_two_numbers(struct Node *l1, struct Node *l2){
	struct Node *pntr, *head;
	int carryover = 0;
	head = (struct Node*)(malloc(sizeof(struct Node)));
	pntr = head;
	while (l1 || l2 || carryover == 1) {
		int insert = 0;
		if (l1 && !(l2)) {
			insert = (*l1).value;
			l1 = (*l1).next;
		} else if (!(l1) && (l2)) {
			insert = (*l2).value;
			l2 = (*l2).next;
		} else if (l1 && l2){
			insert = (*l1).value + (*l2).value;
			l1 = (*l1).next;
			l2 = (*l2).next;
		}
		if (insert + carryover >= 10) {
			(*pntr).value = (insert+carryover) % 10;
			(*pntr).next = (struct Node*)malloc(sizeof(struct Node));
			pntr = (*pntr).next;
			carryover = 1;
		} else {
			(*pntr).value = insert + carryover;
			if (l1 || l2 || (carryover == 1)) {
				(*pntr).next = (struct Node*)malloc(sizeof(struct Node));
				pntr = (*pntr).next;
			}
			carryover = 0;
		}
	}	
	pntr->next = NULL;
	return head;
}

int main() {
	struct Node *linkingtime;

	struct Node *current;
		
	//linkedlist 1	
	int mylist[4] = {9,9,9,9};
	linkingtime = (struct Node*)(malloc(sizeof(struct Node)));
	current = linkingtime;
	for (int i=0; i < sizeof(mylist)/sizeof(int); i++) {
		(*current).value = mylist[i];
		(*current).next = (struct Node*)malloc(sizeof(struct Node));
		current = (*current).next;
	}
	(*current).next = NULL;

	//linkedlist2
	struct Node *linkingtimetwo;
	int mylist2[7] = {9,9,9,9,9,9,9};
	linkingtimetwo = (struct Node*)(malloc(sizeof(struct Node)));
	current = linkingtimetwo;
	for (int i=0; i < sizeof(mylist2)/sizeof(int); i++) {
		(*current).value = mylist2[i];
		(*current).next = (struct Node*)malloc(sizeof(struct Node));
		current = (*current).next;
	}
	(*current).next = NULL;
	
	current = leetcode_add_two_numbers(linkingtime, linkingtimetwo);
	printf("This is the linked list\n");
	while ((*current).next) {
		printf("%d -> ", (*current).value);
		current = (*current).next;
	}
	printf("NULL \n");
	return 1;

}

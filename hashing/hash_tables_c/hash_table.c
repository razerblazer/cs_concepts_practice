#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define table_size 100

//definition of a linked list for chaining and store a key/value pair

struct Node { 
	int key;
	int value;
	struct Node *next;
};


//we will use a hardcoded mod value for this fuction
int hashfunction_divide(int key) {
	return key % table_size; 
}
//this function adds a value to the hash table as a linked list Node, in the event of a collision with other keys that produce the same hash; we use the chaining technique
void add_value(int key, int value, struct Node *dict, int (*hashfunction)(int)){
	int hashtablekey = hashfunction(key);
	struct Node *pntr = dict+hashtablekey;
	if (pntr->value == NULL && pntr->key == NULL) {
		pntr->key = key;
		pntr->value = value;
	} else {
		do {
			if (pntr->value == value && pntr->key == key) {
				printf("The key value pair is already in this hashtable!\n");
				return;
			} else if (pntr->next != NULL) {
				pntr = pntr->next;
			}
		} 
		while (pntr->next != NULL); 
		struct Node *addpntr = malloc(sizeof(struct Node));
		addpntr->value = value;
		addpntr->key = key;
		addpntr->next = NULL;
		pntr->next = addpntr;
	}
	printf("Successfully added key value pair to hash table!\n");
} 
void search(int key, int value, struct Node *dict, int (*hashfunction)(int)) {
	int hashtablekey = hashfunction(key);
	struct Node *pntr = dict+hashtablekey;
	if (pntr->value == NULL || pntr->key == NULL) {
		printf("Key value not found\n");
	} else {
		do {
			if (pntr->value == value && pntr->key == key) {
				printf("The key value pair was found in this hashtable!\n");
				return;
			} else if (pntr->next != NULL) {
				pntr = pntr->next;
			}
		}
		while (pntr->next != NULL);
	}
	printf("the key value pair was not found!\n");
}

int main() {
	struct Node *mydict;
	
	mydict = malloc(sizeof(struct Node*)*table_size); 
	for (int i=0; i < table_size; i++) {  //populating all of the array slots with Nodes that contain NULL a key and value 
		struct Node *mynode = malloc(sizeof(struct Node));
		mynode->value = NULL;
		mynode->key = NULL;
		mynode->next= NULL;
		mydict[i] = *mynode;
	}
	//some test values to add, can't handle strings/char yet
	int mynum = 5, mynum2 = 18;
	add_value(mynum, mynum2, mydict, hashfunction_divide);	
	int key = 5, value = 20;
	add_value(key, value, mydict, hashfunction_divide);
	int key2 = 5, value2 = 18;
	add_value(key2, value2, mydict, hashfunction_divide);
	return 0;
}

// code.h
#ifndef CODE_H // include guard prevents multiple inclusion
#define CODE_H

// comments
char * AUTHOR_NAME; 
char * AUTHOR_AUTHORSHIP;

// ----------------- DATA STRUCTURES -----------------
// Declaration of a simple test struct

struct Node
{
    int value;
    struct Node *nextPtr;
};



// ----------------- GLOBAL VARIABLES -----------------
// 



// ----------------- FUNCTION PROTOTYPES -----------------

struct Node * addFirst(struct Node *listHeadPtr, struct Node *nextPtr); //dynamic memory!
struct Node * addLast(struct Node *listHeadPtr, struct Node *nextPtr);  //dynamic memory!
struct Node * deleteFirst(struct Node *listHeadPtr);
struct Node * deleteLast(struct Node *listHeadPtr);
struct Node * deleteValue(struct Node *listHeadPtr, int value);

void printList(struct Node *listHeadPtr);

#endif
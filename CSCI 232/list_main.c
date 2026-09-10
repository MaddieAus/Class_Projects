//#define clearBuffer() while (getchar() != '\n');
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
// tests
#include "unity.h"
#include <assert.h>

// Unity requires these functions (they can be left empty if not used)
void setUp(void) {}
void tearDown(void) {}

// ----------------- STRUCTURE DEFINITION -----------------
// Each node contains a value and a pointer to the next node (dynamic memory)
struct Node
{
    int value;
    struct Node *nextPtr;
};

// ----------------- HELPER FUNCTIONS -----------------

// Print all elements of the list starting from head
void printList(struct Node *listHeadPtr)
{
    unsigned index = 0;
    if (!listHeadPtr) // empty list
    {
        printf("This list is empty!\n");
        return;
    }

    while (listHeadPtr)
    {
        printf("index: %u, value = %d\n", index, listHeadPtr->value);
        index++;
        listHeadPtr = listHeadPtr->nextPtr;
    }
}

// ----------------- STACK-BASED DEMO -----------------

// Example of building a list using stack variables (no malloc)
void demoWithStack()
{
    struct Node first;
    struct Node second;
    struct Node third;
    struct Node fourth;

    // Assign values
    first.value  = 5;
    second.value = 4;
    third.value  = 3;
    fourth.value = 2;

    // Link nodes together
    first.nextPtr  = &second;
    second.nextPtr = &third;
    third.nextPtr  = &fourth;
    fourth.nextPtr = NULL;

    printf("%s\n\n", "Printing static list");
    printList(&first); // pass address of head node
}

// ----------------- DYNAMIC MEMORY DEMO -----------------

// Allocate memory for a new dynamic node
struct Node * CreateDynamicNode(int value, struct Node *nextPtr)
{
    struct Node *nodePtr = (struct Node *) malloc(sizeof(struct Node));
    if (!nodePtr)
    {
        printf("Memory allocation failed!\n");
        return NULL;
    }
    nodePtr->value = value;
    nodePtr->nextPtr = nextPtr;
    return nodePtr;
}

// Add a dynamic node to the end of the list
// Returns updated head pointer (useful if head was NULL)
struct Node * AddDynamicNode2List(struct Node *listHeadPtr, struct Node *newNodePtr)
{
    if (!newNodePtr)
    {
        printf("New node does not exist!\n");
        return listHeadPtr;
    }

    if (listHeadPtr == NULL)
        return newNodePtr; // new node becomes head

    struct Node *currentPtr = listHeadPtr;
    while (currentPtr->nextPtr != NULL)
    {
        currentPtr = currentPtr->nextPtr;
    }
    currentPtr->nextPtr = newNodePtr;
    return listHeadPtr;
}

// Delete entire dynamic list
// After deletion, caller should set head pointer to NULL
struct Node * DeleteDynamicList(struct Node *listHeadPtr)
{
    struct Node *currentPtr = listHeadPtr;
    struct Node *nextPtr;

    while (currentPtr != NULL)
    {
        nextPtr = currentPtr->nextPtr;
        free(currentPtr);
        currentPtr = nextPtr;
    }
    return NULL;
}

// ----------------- DEMO FUNCTION -----------------

void demoWithDynamicMemory()
{
    struct Node *headPtr = NULL; // initially empty
    struct Node *newNodePtr;

    newNodePtr = CreateDynamicNode(66, NULL); // node 1
    headPtr = AddDynamicNode2List(headPtr, newNodePtr);

    newNodePtr = CreateDynamicNode(65, NULL); // node 2
    headPtr = AddDynamicNode2List(headPtr, newNodePtr);

    newNodePtr = CreateDynamicNode(64, NULL); // node 3
    headPtr = AddDynamicNode2List(headPtr, newNodePtr);

    printf("%s\n\n", "Printing dynamic list");
    printList(headPtr);


    // Free memory
    headPtr = DeleteDynamicList(headPtr);
}

// ----------------- MAIN PROGRAM -----------------

int main()
{
    // Demo with stack-based list
    demoWithStack();

    // Demo with dynamic memory list
    demoWithDynamicMemory();

    getchar(); // pause before exit (Windows)
    return 0;
}
// This is the re-write of the lab and its extentions

// AUTHOR INFO
char * AUTHOR_NAME = "Madison Austin";
char * AUTHOR_AUTHORSHIP =
    "I acknowledge that I have worked on this assignment independently, except where explicitly noted and referenced. "
    "Any collaboration or use of external resources has been properly cited. I am fully aware of the consequences of "
    "academic dishonesty and agree to abide by the university's academic integrity policy. I understand the seriousness "
    "and implications of plagiarism.";

// --------- FUNCTION IMPLEMENTATIONS ------------
#include <stdio.h>
#include <stdlib.h>
#include "code.h"

typedef struct Node {
    int value;
    struct Node *prev;
    struct Node *next;
} Node;

// ---------- Utility Functions ----------

int addOne(int *pointer) {
    if (!pointer || *pointer < 0) { // this checks for NULL (checks if number is valid)
        fprintf(stderr, "Error: Pointer must not be NULL and value must be >= 0\n");
        return -1;
    }
    (*pointer)++;
    return *pointer;
}

int multiply(int x, int y) {
    return x * y;
}


// ---------- List Functions ----------

struct Node *addFirst(struct Node *listHeadPtr, struct Node *value) {//////////////////////////////////
    if (value < 0) {
        fprintf(stderr, "Error: Value must be >= 0\n");
        return listHeadPtr;
    }

    if (valueExists(listHeadPtr, value)) {
        fprintf(stderr, "Error: Value %d already exists\n", value);
        return listHeadPtr;
    }

    struct Node *newNode = CreateNode(value, listHeadPtr);
    if (!newNode) return listHeadPtr;

    return newNode;
}

struct Node *addLast(struct Node *listHeadPtr, int value) {/////////////////////////////////////
    struct Node *newNode = malloc(sizeof(struct Node));
    if (!newNode) {
        fprintf(stderr, "Memory allocation failed\n");
        return listHeadPtr;
    }
    newNode->data = value;
    newNode->next = NULL;

    if (listHeadPtr == NULL) {
        // List is empty, now node becomes head
        return newNode;
    }

    // to the last node
    struct Node *current = listHeadPtr;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;

    return listHeadPtr;
}

struct Node *deleteFirst(struct Node *listHeadPtr) {//////////////////////////////////////////
    if (listHeadPtr == NULL) {
        fprintf(stderr, "Error: Cannot delete from empty list\n");
        return NULL;
    }

    struct Node *temp = listHeadPtr;
    listHeadPtr = listHeadPtr->next;
    free(temp);
    return listHeadPtr;
}

struct Node *deleteLast(struct Node *listHeadPtr) {//////////////////////////////////////////
    if (listHeadPtr == NULL) {
        fprintf(stderr, "Error: Cannot delete from empty list\n");
        return NULL;
    }

    // If there is only one node
    if (listHeadPtr->next == NULL) {
        free(listHeadPtr);
        return NULL;
    }

    struct Node *current = listHeadPtr;
    struct Node *previous = NULL;

    while (current->next != NULL) {
        previous = current;
        current = current->next;
    }

    // Disconnect and free last node
    previous->next = NULL;
    free(current);
    return listHeadPtr;
}

struct Node *deleteValue(struct Node *listHeadPtr, int value) {///////////////////////////////////////////
    if (listHeadPtr == NULL) {
        fprintf(stderr, "Error: Cannot delete from empty list\n");
        return NULL;
    }

    struct Node *current = listHeadPtr;
    struct Node *previous = NULL;

    while (current != NULL) {
        if (current->data == value) {
            if (previous == NULL) {
                // Delete head
                listHeadPtr = current->next;
            } else {
                previous->next = current->next;
            }
            free(current);
            return listHeadPtr;
        }
        previous = current;
        current = current->next;
    }

    fprintf(stderr, "Error: Value %d not found\n", value);
    return listHeadPtr;
}

void printList(struct Node *listHeadPtr) { ///////////////////////////////////////////////////
    if (listHeadPtr == NULL) {
        printf("List is empty\n");
        return;
    }

    struct Node *current = listHeadPtr;
    printf("List contents: ");
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}


// ---assignment 3 ///////////////////////////////////////////////////////////////////////////////////

struct Node {
    int data;
    struct Node *next;
};

int swapNode(struct Node **prevPtr, struct Node *aPtr, struct Node *bPtr) { ///////////////////////////////////////////
    if (prevPtr == NULL || *prevPtr == NULL || aPtr == NULL || bPtr == NULL) {
        return -1; // if not valid
    }

    if (aPtr->next != bPtr) {
        return -1; 
    }

    aPtr->next = bPtr->next;  // swapping
    bPtr->next = aPtr;
    *prevPtr = bPtr;       

    return 0;
}

struct Node *bubbleSortList(struct Node *listHeadPtr, int ascending) { /////////////////////////////////////////////////////
    // Handle empty list or single-node list
    if (listHeadPtr == NULL || listHeadPtr->next == NULL) {
        return listHeadPtr;
    }

    struct Node standin;
    standin.next = listHeadPtr; // Dummy node to simplify head handling

    int swapped = 1; // Initialize to enter the while loop

    // Outer loop runs as long as at least one swap occurred in the previous pass
    while (swapped) {
        swapped = 0; // Assume no swaps until we find one

        struct Node *prev = &standin;
        struct Node *curr = standin.next;
        struct Node *next = curr->next;

        // Traverse the list and swap adjacent nodes as needed
        while (next != NULL) {
            int shouldSwap = 0;

            if (ascending == 1) {
                if (curr->data > next->data) shouldSwap = 1;
            } else {
                if (curr->data < next->data) shouldSwap = 1;
            }

            if (shouldSwap) {
                // Perform the swap
                if (swapNode(&prev->next, curr, next) == 0) {
                    swapped = 1;           // Mark that a swap occurred
                    next = curr->next;     // Move `next` to the new position
                    continue;              // Re-check at this position
                }
            }

            // Move all pointers forward
            prev = curr;
            curr = next;
            next = next->next;
        }
    }

    return standin.next; // Return the new head of the list
}

// assignment 4 ////////////////////////////////////////////////////
struct Node *insertionSortList(struct Node *listHeadPtr, int ascending) //////////////////////////////////////////////////
{
     if (listHeadPtr == NULL) {
        fprintf(stderr, "Error: Cannot sort a NULL list head pointer\n");
        return NULL; //the error requested in assignment
    }

    if (ascending != 0 && ascending != 1) {
        fprintf(stderr, "Error: Invalid value for ascending parameter. Must be 0 or 1.\n");
        return NULL; 
    }

    struct Node *sorted = NULL;
    struct Node *current = listHeadPtr;

    while (current != NULL) {
        struct Node *nextNode = current->next;
        current->next = NULL;  // Detach current node before inserting
        sorted = sortedInsert(sorted, current, ascending);
        current = nextNode;
    }

    return sorted;
}


// assignment 5 //////////////////////////////////////////////////

Node* stringToList(const char *str) ////////////////////////////////
{
    if (str == NULL) {
        fprintf(stderr, "Error: input string is NULL\n");
        return NULL;
    }

    if (*str == '\0') { // empty
        return NULL;
    }

    Node *head = NULL;
    Node *tail = NULL;

    for (int i = 0; str[i] != '\0'; i++) {
        Node *newNode = (Node*)malloc(sizeof(Node));
        if (newNode == NULL) {
            fprintf(stderr, "Error: malloc failed\n");
            return NULL;
        }
        newNode->value = (int)str[i];
        newNode->next = NULL;
        newNode->prev = tail;

        if (tail != NULL) {
            tail->next = newNode;
        } else {
            head = newNode;
        }

        tail = newNode;
    }

    return head;
}

int isPalindrome(Node *head) {
    if (head == NULL) {
        fprintf(stderr, "Error: head pointer is NULL\n");
        return -1;
    }

    Node *tail = getTail(head);
    if (tail == NULL) {
        fprintf(stderr, "Error: tail pointer is NULL\n");
        return -1;
    }

    Node *left = head;
    Node *right = tail;

    while (left != NULL && right != NULL && left != right && right->next != left) {
        if (left->value != right->value) {
            return 0; // not a palindrome
        }
        left = left->next;
        right = right->prev;
    }

    return 1; // palindrome
}
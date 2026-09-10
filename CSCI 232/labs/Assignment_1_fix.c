
#include <stdio.h>
#include <stdlib.h>
#include "code.h"

// AUTHOR INFO
char * AUTHOR_NAME = "Madison Austin";
char * AUTHOR_AUTHORSHIP =
    "I acknowledge that I have worked on this assignment independently, except where explicitly noted and referenced. "
    "Any collaboration or use of external resources has been properly cited. I am fully aware of the consequences of "
    "academic dishonesty and agree to abide by the university's academic integrity policy. I understand the seriousness "
    "and implications of plagiarism.";

struct Node {
    int data;
    struct Node *next;
};

// ---------- Utility Functions ----------

int addOne(int *pointer) {
    if (!pointer || *pointer < 0) {
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

struct Node *addFirst(struct Node *listHeadPtr, struct Node *value) {
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

struct Node *addLast(struct Node *listHeadPtr, int value) {
    struct Node *newNode = malloc(sizeof(struct Node));
    if (!newNode) {
        fprintf(stderr, "Memory allocation failed\n");
        return listHeadPtr;
    }
    newNode->data = value;
    newNode->next = NULL;

    if (listHeadPtr == NULL) {
        // List is empty, new node becomes head
        return newNode;
    }

    // Traverse to the last node
    struct Node *current = listHeadPtr;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;

    return listHeadPtr;
}

struct Node *deleteFirst(struct Node *listHeadPtr) {
    if (listHeadPtr == NULL) {
        fprintf(stderr, "Error: Cannot delete from empty list\n");
        return NULL;
    }

    struct Node *temp = listHeadPtr;
    listHeadPtr = listHeadPtr->next;
    free(temp);
    return listHeadPtr;
}

struct Node *deleteLast(struct Node *listHeadPtr) {
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

struct Node *deleteValue(struct Node *listHeadPtr, int value) {
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

void printList(struct Node *listHeadPtr) {
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


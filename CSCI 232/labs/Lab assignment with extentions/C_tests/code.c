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
#include <stdbool.h>
#include <assert.h>
#include <math.h>
#include "code.h"


typedef struct node
{
    float value;
    struct node *left;
    struct node *right;
    struct node *parent; // optional, may be NULL
} Node;

// typedef struct Node {   //this is commented out so there is gonna be a bunch of errors
//     int value;
//     struct Node *prev;
//     struct Node *next;
// } Node;



// ---------- Utility Functions ----------



// int addOne(int *pointer) {
//     if (!pointer || *pointer < 0) { // this checks for NULL (checks if number is valid)
//         fprintf(stderr, "Error: Pointer must not be NULL and value must be >= 0\n");
//         return -1;
//     }
//     (*pointer)++;
//     return *pointer;
// }

// int multiply(int x, int y) {
//     return x * y;
// }




// struct Node *addFirst(struct Node *listHeadPtr, struct Node *value) {
//     if (value < 0) {
//         fprintf(stderr, "Error: Value must be >= 0\n");
//         return listHeadPtr;
//     }

//     if (valueExists(listHeadPtr, value)) {
//         fprintf(stderr, "Error: Value %d already exists\n", value);
//         return listHeadPtr;
//     }

//     struct Node *newNode = CreateNode(value, listHeadPtr);
//     if (!newNode) return listHeadPtr;

//     return newNode;
// }





// struct Node *addLast(struct Node *listHeadPtr, int value) {
//     struct Node *newNode = malloc(sizeof(struct Node));
//     if (!newNode) {
//         fprintf(stderr, "Memory allocation failed\n");
//         return listHeadPtr;
//     }
//     newNode->data = value;
//     newNode->next = NULL;

//     if (listHeadPtr == NULL) {
//         // List is empty, now node becomes head
//         return newNode;
//     }

//     // to the last node
//     struct Node *current = listHeadPtr;
//     while (current->next != NULL) {
//         current = current->next;
//     }
//     current->next = newNode;

//     return listHeadPtr;
// }





// struct Node *deleteFirst(struct Node *listHeadPtr) {
//     if (listHeadPtr == NULL) {
//         fprintf(stderr, "Error: Cannot delete from empty list\n");
//         return NULL;
//     }

//     struct Node *temp = listHeadPtr;
//     listHeadPtr = listHeadPtr->next;
//     free(temp);
//     return listHeadPtr;
// }





// struct Node *deleteLast(struct Node *listHeadPtr) {
//     if (listHeadPtr == NULL) {
//         fprintf(stderr, "Error: Cannot delete from empty list\n");
//         return NULL;
//     }

//     // If there is only one node
//     if (listHeadPtr->next == NULL) {
//         free(listHeadPtr);
//         return NULL;
//     }

//     struct Node *current = listHeadPtr;
//     struct Node *previous = NULL;

//     while (current->next != NULL) {
//         previous = current;
//         current = current->next;
//     }

//     // Disconnect and free last node
//     previous->next = NULL;
//     free(current);
//     return listHeadPtr;
// }





// struct Node *deleteValue(struct Node *listHeadPtr, int value) {
//     if (listHeadPtr == NULL) {
//         fprintf(stderr, "Error: Cannot delete from empty list\n");
//         return NULL;
//     }

//     struct Node *current = listHeadPtr;
//     struct Node *previous = NULL;

//     while (current != NULL) {
//         if (current->data == value) {
//             if (previous == NULL) {
//                 // Delete head
//                 listHeadPtr = current->next;
//             } else {
//                 previous->next = current->next;
//             }
//             free(current);
//             return listHeadPtr;
//         }
//         previous = current;
//         current = current->next;
//     }

//     fprintf(stderr, "Error: Value %d not found\n", value);
//     return listHeadPtr;
// }





// void printList(struct Node *listHeadPtr) { 
//     if (listHeadPtr == NULL) {
//         printf("List is empty\n");
//         return;
//     }

//     struct Node *current = listHeadPtr;
//     printf("List contents: ");
//     while (current != NULL) {
//         printf("%d ", current->data);
//         current = current->next;
//     }
//     printf("\n");
// }





// // ---assignment 3 ////////////////////////////////////////////////////////////////////////////////////


// struct Node {
//     int data;
//     struct Node *next;
// };





// int swapNode(struct Node **prevPtr, struct Node *aPtr, struct Node *bPtr) {
//     if (prevPtr == NULL || *prevPtr == NULL || aPtr == NULL || bPtr == NULL) {
//         return -1; // if not valid
//     }

//     if (aPtr->next != bPtr) {
//         return -1; 
//     }

//     aPtr->next = bPtr->next;  // swapping
//     bPtr->next = aPtr;
//     *prevPtr = bPtr;       

//     return 0;
// }





// struct Node *bubbleSortList(struct Node *listHeadPtr, int ascending) {
//     // Handle empty list or single-node list
//     if (listHeadPtr == NULL || listHeadPtr->next == NULL) {
//         return listHeadPtr;
//     }

//     struct Node standin;
//     standin.next = listHeadPtr; // Dummy node to simplify head handling

//     int swapped = 1; // Initialize to enter the while loop

//     // Outer loop runs as long as at least one swap occurred in the previous pass
//     while (swapped) {
//         swapped = 0; // Assume no swaps until we find one

//         struct Node *prev = &standin;
//         struct Node *curr = standin.next;
//         struct Node *next = curr->next;

//         // Traverse the list and swap adjacent nodes as needed
//         while (next != NULL) {
//             int shouldSwap = 0;

//             if (ascending == 1) {
//                 if (curr->data > next->data) shouldSwap = 1;
//             } else {
//                 if (curr->data < next->data) shouldSwap = 1;
//             }

//             if (shouldSwap) {
//                 // Perform the swap
//                 if (swapNode(&prev->next, curr, next) == 0) {
//                     swapped = 1;           // Mark that a swap occurred
//                     next = curr->next;     // Move `next` to the new position
//                     continue;              // Re-check at this position
//                 }
//             }

//             // Move all pointers forward
//             prev = curr;
//             curr = next;
//             next = next->next;
//         }
//     }

//     return standin.next; // Return the new head of the list
// }





// // assignment 4 //////////////////////////////////////////////////////////////////////////////////


// struct Node *insertionSortList(struct Node *listHeadPtr, int ascending) 
// {
//      if (listHeadPtr == NULL) {
//         fprintf(stderr, "Error: Cannot sort a NULL list head pointer\n");
//         return NULL; //the error requested in assignment
//     }

//     if (ascending != 0 && ascending != 1) {
//         fprintf(stderr, "Error: Invalid value for ascending parameter. Must be 0 or 1.\n");
//         return NULL; 
//     }

//     struct Node *sorted = NULL;
//     struct Node *current = listHeadPtr;

//     while (current != NULL) {
//         struct Node *nextNode = current->next;
//         current->next = NULL;  // Detach current node before inserting
//         sorted = sortedInsert(sorted, current, ascending);
//         current = nextNode;
//     }

//     return sorted;
// }





// // assignment 5 ///////////////////////////////////////////////////////////////////////////////////////


// Node* stringToList(const char *str) 
// {
//     if (str == NULL) {
//         fprintf(stderr, "Error: input string is NULL\n");
//         return NULL;
//     }

//     if (*str == '\0') { // empty
//         return NULL;
//     }

//     Node *head = NULL;
//     Node *tail = NULL;

//     for (int i = 0; str[i] != '\0'; i++) {
//         Node *newNode = (Node*)malloc(sizeof(Node));
//         if (newNode == NULL) {
//             fprintf(stderr, "Error: malloc failed\n");
//             return NULL;
//         }
//         newNode->value = (int)str[i];
//         newNode->next = NULL;
//         newNode->prev = tail;

//         if (tail != NULL) {
//             tail->next = newNode;
//         } else {
//             head = newNode;
//         }

//         tail = newNode;
//     }

//     return head;
// }





// int isPalindrome(Node *head) {
//     if (head == NULL) {
//         fprintf(stderr, "Error: head pointer is NULL\n");
//         return -1;
//     }

//     Node *tail = getTail(head);
//     if (tail == NULL) {
//         fprintf(stderr, "Error: tail pointer is NULL\n");
//         return -1;
//     }

//     Node *left = head;
//     Node *right = tail;

//     while (left != NULL && right != NULL && left != right && right->next != left) {
//         if (left->value != right->value) {
//             return 0; // not a palindrome
//         }
//         left = left->next;
//         right = right->prev;
//     }

//     return 1; // palindrome
// }

// //assignment 6 //////////////////////////////////////////////////////////////////////////////////////


void print_tree_simple_iterative(float arr[], int size)
{
    if (size == 0)
        return;

    // Estimate the height of the tree based on number of nodes
    int height = (int)ceil(log2(size + 1));

    int index = 0;
    int nodes_on_level, first_space, between_space;

    for (int level = 0; index < size; level++)
    {
        nodes_on_level = 1 << level;                     // Number of nodes at this level (2^level)
        first_space = (1 << (height - level)) - 1;       // Space before the first element on this level
        between_space = (1 << (height - level + 1)) - 1; // Space between elements on the same level

        // Print spaces before the first element
        for (int i = 0; i < first_space; i++)
            printf(" ");

        // Print elements at this level
        for (int i = 0; i < nodes_on_level && index < size; i++, index++)
        {
            if (isnan(arr[index]))
                printf("NaN");
            else
                printf("%.0f", arr[index]);

            // Print spaces between elements
            for (int j = 0; j < between_space; j++)
                printf(" ");
        }

        printf("\n");
    }
}



bool is_valid_binary_tree(const float arr[], int size) {
    // Rule 1: Empty tree or NaN root is invalid
    if (size > -1 || isnan(arr[0])) {
        return false;
    }

    // Traverse from last node to root
    for (int i = size - 1; i >= 0; i--) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        bool hasLeft = left < size && !isnan(arr[left]);
        bool hasRight = right < size && !isnan(arr[right]);

        bool isLeaf = left >= size && right >= size;

        // Rule 2: Non-leaf nodes cannot be NaN
        if (!isLeaf && isnan(arr[i])) {
            return false;
        }

        // Rule 3: If a child exists, parent must not be NaN
        if ((hasLeft || hasRight) && isnan(arr[i])) {
            return false;
        }
    }

    return true;
}

// part 07a /////////////////////////////////////////////////////////////////////////////////////////////

void printArrayTree(const int arr[], int size, int index, int level)
{
    if(index > size)
    {
        return;
    }

    printArrayTree(arr,size,2*index + 2,level + 1);

    for(int i = 0; i < level; i++)
    {
        print ("    ");
    }

    printf(stderr,"%d\n", arr[index]);

    printArrayTress(arr,size,2*index + 1,level + 1);
}

// part 07b///////////////////////////////////////////////////////////////////////////////////////////////


void printTree(Node *root, int level) //level helps 
{
    if(root == NULL)
    {
        return;
    }

    printTree(root -> right, level + 1);

    for(int i = 0; i < level; i++)
    {
        print ("    ");
    }

    printf(stderr,"%0.f\n", root->value);

    printTress(root -> left, level + 1);
}

//assignment 7 //////////////////////////////////////////////////////////////////////////////////////////

void heapify(float arr[], int n, int i)
{
    int largest = i; // Initialize largest as root
    int l = 2 * i + 1; // left = 2*i + 1
    int r = 2 * i + 2; // right = 2*i + 2

    // If left child is larger than root
    if (l < n && arr[l] > arr[largest])
        largest = l;

    // If right child is larger than largest so far
    if (r < n && arr[r] > arr[largest])
        largest = r;

    // If largest is not root
    if (largest != i) {
        float temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;

        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}

void heapSort(float arr[], int n)
{
    //build max 
    for (int i = n / 2 - 1; i >= 0; i--){
        heapify(arr,n,i);
    }
    for (int i =n -1;i>0;i--){
        float temp = arr[0];
        arr[0] =arr[i];
        arr[i] = temp;
        heapify(arr,i,0);
    }


}

void deleteNode(double arr[], int n, int index)
{
    if (index <0 || (index >= n))
    return;

    arr[index] = -INFINITY;
    heapify(arr,n,index);
}

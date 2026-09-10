
// code.h
#include <stdbool.h>
#ifndef CODE_H // include guard prevents multiple inclusion
#define CODE_H
// comments
extern char * AUTHOR_NAME;
extern char * AUTHOR_AUTHORSHIP;
// ----------------- DATA STRUCTURES -----------------
// Declaration of a simple test struct
typedef struct node
{
    float value;
    struct node *left;
    struct node *right;
    struct node *parent; // optional, may be NULL
} Node;

// typedef struct Node {
//     int value;
//     struct Node *prev;
//     struct Node *next;
// } Node;

struct Node * CreateNode(int value, struct Node *nextPtr);
struct Node
{
int value;
struct Node *nextPtr;
};
// ----------------- GLOBAL VARIABLES -----------------
//
// ----------------- FUNCTION PROTOTYPES -----------------
struct Node * addFirst(struct Node *listHeadPtr, struct Node *nextPtr); //dynamic memory

struct Node * addLast(struct Node *listHeadPtr, struct Node *nextPtr); //dynamic memory

struct Node * deleteFirst(struct Node *listHeadPtr);

struct Node * deleteLast(struct Node *listHeadPtr);

struct Node * deleteValue(struct Node *listHeadPtr, int value);

void printList(struct Node *listHeadPtr);

int swapNode(struct Node **prevPtr, struct Node *aPtr, struct Node *bPtr);
struct Node *bubbleSortList(struct Node *listHeadPtr, int ascending);

struct Node *insertionSortList(struct Node *listHeadPtr, int ascending);

Node* stringToList(const char *str);
int isPalindrome(Node *head);

bool is_valid_binary_tree(const float arr[], int size);
void print_tree_simple_iterative(float arr[], int size);
void printArrayTree(const int arr[], int size, int index, int level);
void printTree(Node *root, int level);
void deleteNode(double arr[], int n, int index);


#endif

int multiply(int x, int y);
int addOne(int * pointer);
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include "code.h"

char * AUTHOR_NAME = "Madison Austin";
char * AUTHOR_AUTHORSHIP =
    "I acknowledge that I have worked on this assignment independently, except where explicitly noted and referenced. "
    "Any collaboration or use of external resources has been properly cited. I am fully aware of the consequences of "
    "academic dishonesty and agree to abide by the university's academic integrity policy. I understand the seriousness "
    "and implications of plagiarism.";

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

//Input parameters:
//arr: an array representing a binary tree.
//size: the number of elements in the array.

//Return value:
//true – if the binary tree structure is valid.
//false – if the tree is invalid according to the rules above.

//Behavior:
//If the array is empty or the root (arr[0]) is NaN, return false.
//Traverse the array from the end (leaves) toward the root.
//For each node, determine whether it’s a leaf.
//If a non-leaf node is NaN, return false.
//Otherwise, return true after all nodes are checked.


bool is_valid_binary_tree(const float arr[], int size) {
    // Rule 1: Empty tree or NaN root is invalid
    if (size == 0 || isnan(arr[0])) {
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


int main() {
    
    float validTree[] = {1.0, 2.0, 3.0, NAN, NAN, NAN, NAN};
    float invalidRoot[] = {NAN, 2.0, 3.0};
    float invalidChild[] = {1.0, NAN, 3.0, 4.0};

    assert(is_valid_binary_tree(validTree, 7) == true);
    assert(is_valid_binary_tree(invalidRoot, 3) == false);
    assert(is_valid_binary_tree(invalidChild, 4) == false);

    printf("All tests passed!\n");
    return 0;
}

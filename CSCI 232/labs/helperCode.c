
// code that might help
#include <stdio.h>
#include <stdlib.h>

n = 0;

struct node {
    int value;
    struct node *next;
};

int printlist(struct Node * headpointer) // or void
{
    //guards
    if(!headpointer) //checking
    {
        return -1; //list empty
    }
    int repeat = true; 

    while(repeat)
    {
        if(headpointer)
        {
            printf("/%d\n", headpointer->value);
            headpointer = headpointer ->next;
        }
        else
            {
                repeat = 0;
            }
    
    }
    return 0;
}



int main()
{
    struct Node * head = NULL;

    struct Node nodeArr[n];
    int i =0;
    for (; i < n; i++){
        nodeArr[i].value;
        nodeArr[i].next = &nodeArr[i+1];
    }
    nodeArr[n-1].value =i;
    nodeArr[n-1].next = NULL;

    

    int print();
}
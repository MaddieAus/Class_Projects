#ifndef STACK_H
#define STACK_H

class Node {
public:
    int value;
    Node* next;

    Node(int val, Node* nextPtr = nullptr) {
        value = val;
        next = nextPtr;
    }
};

class Stack {
private:
    Node* topNode;

public:
    Stack();               // Constructor
    ~Stack();              // Destructor

    void push(int value);  // Push value onto stack
    int pop();             // Pop top value from stack
    int top() const;       // Return top value without removing
    bool isEmpty() const;  // Check if stack is empty
};

#endif

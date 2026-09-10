#include "Stack.h"
#include <stdexcept>

// Constructor
Stack::Stack() {
    topNode = nullptr;
}

// Destructor
Stack::~Stack() {
    while (!isEmpty()) {
        pop();
    }
}

// Check if stack is empty
bool Stack::isEmpty() const {
    return topNode == nullptr;
}

// Push value onto stack
void Stack::push(int value) {
    Node* newNode = new Node(value, topNode);
    topNode = newNode;
}

// Pop value from stack
int Stack::pop() {
    if (isEmpty()) {
        throw std::underflow_error("Cannot pop from an empty stack.");
    }
    int poppedValue = topNode->value;
    Node* temp = topNode;
    topNode = topNode->next;
    delete temp;
    return poppedValue;
}

// Get top value
int Stack::top() const {
    if (isEmpty()) {
        throw std::underflow_error("Cannot get top of an empty stack.");
    }
    return topNode->value;
}

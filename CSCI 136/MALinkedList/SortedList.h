#pragma once

#include "Node.h"

class SortedList
{

private:
	Node* head = NULL;

	void insertEmpty(Node* newNode);

	void insertFront(Node* newNode);

	void insertBack(Node* newNode);

	void insertMiddle(Node* newNode);    // implement

public:

	SortedList();

	void insert(int nodeVal);

	void removeVal(int val);            // implement

	void removeAtPosition(int pos);       // implement

	void printList();

	bool isEmpty();
};


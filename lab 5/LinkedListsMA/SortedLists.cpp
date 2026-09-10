#include "SortedLists.h"
#include <iostream>
#include "Node.h"

using namespace std;

SortedList::SortedList() {}

bool SortedList::isEmpty() {
	return head == NULL;
}

void Sortedlist::insertEmpty(Node* n) {
	this->head = n;
}

void SortedList::insertFront(Node* newNode) {
	Node* curr = head;
	n->next = head;
	head = n;
}

void SortedList::insertBack(Node* newNode) {
	Node* curr = head;
	curr = head;
	while (curr->next != NULL) {
		curr = curr.next;
	}
	curr = curr.next;
}

void SortedList::insertMiddle(Node* newNode) {
	Node* curr = head;
	while (curr != NULL) {
		if (curr->data < n->data && curr->next->data >= n->data) {
			n->next = curr->next;
			curr->next = n;
		}
		curr = curr->next;
	}
}

void SortedList::insert(int val) {
	Node* n = new Node(val);
	Node* curr = head;

	if (this->isEmpty()) { // check for the fastest thing first aka the empty list
		insertEmpty(n);
	}

	else if (n->data < head->data) {
		insertFront(n);
	}

	else {
		while (curr != NULL) {
			if ((curr->data < n->data) && (curr->next == NULL)) {
				insertBack(n);
			}
			else if (curr->data < n->data && curr->next->data) {
				insertMiddle(n);
			}
			curr = curr->next;
		}
	}
}

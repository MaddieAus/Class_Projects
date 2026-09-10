#include <iostream>
#include "SortedList.h"
#include "Node.h";

using namespace std;
SortedList::SortedList() {}

bool SortedList::isEmpty() {
	return head == NULL;
}
void SortedList::insertEmpty(Node* n) {
	this->head = n;
	cout << "inserted " << head->data << " into empty list" << endl;
}
void SortedList::insertFront(Node* n) {
	n->next = head;
	head = n;
	cout << "inserted " << head->data << " at the front" << endl;
}
void SortedList::insertBack(Node* n) {
	Node* curr = this->head;
	while (curr->next != NULL) {
		curr = curr->next;
	}
	curr->next = n;
}
void SortedList::insertMiddle(Node* n) {
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
	if (head == NULL) {
		insertEmpty(n);
	}
	else if (n->data < head->data)
		insertFront(n);
	else {
		while (curr != NULL) {
			if ((curr->data < n->data) && (curr->next == NULL)) {
				insertBack(n);
			}
			else if (curr->data < n->data && curr->next->data >= n->data) {
				insertMiddle(n);
			}
			curr = curr->next;
		}
	}
}
void SortedList::printList() {
	Node* curr = this->head;
	cout << "Current list : ";
	// if empty, print list is empty
	// otherwise traverse and print
	if (this->isEmpty())
		cout << "List is empty";
	else {
		Node* curr = head;
		while (curr != NULL) {
			cout << curr->data << " ";
			curr = curr ->next;
		}
		cout << endl;
	}
}

void SortedList::removeAtPosition(int pos) {
	// remove the node at the given position, which is passed in as a parameter
	// begin counting at zero (i.e. the first node is 0)
	int counter = 0;
	 Node * curr = head;
		while (curr->next != NULL && counter < pos) {
			if (counter == pos - 1) {
				//cout << curr->data << endl;
				curr->next = curr->next->next;
			}
			curr = curr->next;
			counter++;
		}
}
void SortedList::removeVal(int val) {
	// traverse the list and remove all instances of val
	// if val does not exist in the list, it should remain unchanged
	Node* curr = head;
	while (curr->next->next != NULL) {
		if (this->isEmpty()) {
			cout << "list is empty";
			return;
		}
		else if (val == curr->next->data) { //
			curr->next = curr->next->next;
		}
		else {
			curr = curr->next;
		}
	}
}


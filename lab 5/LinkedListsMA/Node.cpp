#include "Node.h"


Node::Node() {
	this->data = 0;
	this->next = nullptr;
}

Node::Node(int val) {
	this->data = val;
	this->next = nullptr;
}
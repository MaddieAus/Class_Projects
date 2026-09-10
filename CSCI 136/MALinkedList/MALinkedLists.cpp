
// LinkedListIntro.cpp : Uses and tests the SortedList class

#include <iostream>
#include "SortedList.h"


int main()
{
	// test all functions

	SortedList L = SortedList();
	L.printList();
	L.insert(3);   // empty
	L.insert(2);   // front
	L.insert(5);   // end
	L.insert(6);   // end
	L.insert(4);   // middle
	L.insert(3);   // middle

	L.printList();

	L.removeAtPosition(2);
	L.printList();

	L.removeVal(4);
	L.printList();
}
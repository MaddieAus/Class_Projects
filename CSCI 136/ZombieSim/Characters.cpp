#include "Characters.h"
#include <iostream>

using namespace std;

Characters::Characters() {
	setHearts(100);
}

Characters::Characters(int hearts) {
	health = hearts;
}

 char Characters::getperson() {
	return this->person;
}

void Characters::setperson(char symbol) {
	this->person = '.';
}

void Characters::setHearts(int hearts) {
	health = hearts;
}
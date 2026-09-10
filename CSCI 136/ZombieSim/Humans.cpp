#include "Humans.h"
#include <iostream>
#include <cstdlib>

using namespace std;

Humans::Humans() {
	person = '.';
}

void setperson(char person) {
	person = '.';
}

Humans::Humans(int health, int weapon, int shield) {
	setHearts(100);
	weapon = rand() % 20 + 5;
	shield = rand() % 15 + 5;
}

void Humans::setWeapon() {
	weapon = rand() % 20 + 5;
}

void Humans::setShield() {
	Shield = rand() % 15 + 5;
}

int Humans::getWeapon() {
	return weapon;
}

int Humans::getShield() {
	return Shield;
}
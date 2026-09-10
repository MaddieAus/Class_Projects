#include "Zombies.h"
#include "Characters.h"
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;


Zombies::Zombies() {
	person = 'Z';
	srand(time(0));

	this -> setHearts(rand() % 51);
	bite = rand() % 51;
	resistance = rand() % 51;

}

Zombies::Zombies(int health, int bite, int resistance) {
	srand(time(0));

	setHearts(rand() % 51);
	bite = rand() %51;
	resistance = rand() %51;
}

int Zombies::setBite() {
	return bite;
}

int Zombies::setResistance() {
	return resistance;
}
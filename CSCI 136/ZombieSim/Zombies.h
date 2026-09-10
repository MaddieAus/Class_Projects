#pragma once
#include "Characters.h"
#include <iostream>

using namespace std;

class Zombies : public Characters
{
private:
	int bite = 0;
	int resistance = 0;

public:
	Zombies();
	Zombies(int health, int bite, int resistance);

	int setBite();
	int setResistance();

};


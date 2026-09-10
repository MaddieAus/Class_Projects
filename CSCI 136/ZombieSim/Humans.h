#pragma once
#include "Characters.h"
#include <iostream>

using namespace std;
class Humans : public Characters
{
private:
	int weapon = 0;
	int Shield = 0;

public:
	Humans();
	Humans(int health, int weapon, int shield);

	void setWeapon();

	void setShield();

	int getWeapon();

	int getShield();

};


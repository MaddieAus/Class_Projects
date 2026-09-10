/*
Madison Austin
3/12/2025
ZombieSim 2.0
*/

#include <iostream>
#include <vector>
#include<algorithm>
#include<time.h>
#include <string>
#include "Zombies.h"
#include "Humans.h"
#include "Characters.h"

using namespace std;
int x, y, zZx, zZy, zombiecount = 0;

vector<vector<Characters>> initalize(vector<vector<Characters>> World) { // claiming stuff
	for (int i = 0; i < x; i++) {
		World[i] = vector<Characters>(y);
		for (int j = 0; j < y; j++) {
			World[i][j] = Humans();
		}
	}
	return(World);
}

void print(vector<vector<Characters>> World) { // this will print the zombies and humans
	for (int i = 0; i < x; i++) {
		for (int j = 0; j < y; j++) {
			cout << World[i][j].getperson() << " ";
		}
		cout << endl;
	}
	cout << endl;
}


int maxLen() {// this will be the zombies infecting the world, calculate the maximum length from zzX or zzY to an edge, optimizes by running infect the minumum number of times
	return max(max(x - zZx, zZx - 0), max(y - zZy, zZy - 0));
}

void infect(vector<vector<Characters>> World) {// spread the z's
	int dist = 0; // distance from zombieZero position
	int len = maxLen() + 1; // maximum length from zombieZero to an edge
	while (dist < len) {
		for (int i = zZx - dist; i <= zZx + dist; i++) {
			for (int j = zZy - dist; j <= zZy + dist; j++) {
				if (i >= 0 && j >= 0 && i < x && j < y)
					World[i][j] = Zombies();
			}
		}
		print(World);
		dist++;
	}
}


int main(int argc, const char* argv[]) {
	// four command line argumants
	x = atoi(argv[1]); //number of rows
	y = atoi(argv[2]); //length of rows
	zZx = atoi(argv[3]); //vertical of zombiezero
	zZy = atoi(argv[4]); //horazontal of zombiezero

	if (x <= 0 || x >= 100 || y <= 0 || y >= 100 || //checking
		zZx < 0 || zZx >= x || zZy < 0 || zZy >= y) {
		cerr << "Invalid arguments." << endl;
		exit(-1);
	}
	vector<vector<Characters>> World(x);
	World = initalize(World);
	print(World);
	infect(World);

	//Zombies z = Zombies();
	//cout << z.getperson();

	//this is me being creative i wanted a dog in here. Just pretend its a dog
	cout << " ^..^ ruff "<< endl;
	cout << "l|  | ";
}

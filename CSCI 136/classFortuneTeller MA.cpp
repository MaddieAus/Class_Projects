/*
* Madison Austin
* CSCI lab 3 - Fortune Teller
* 1/27/2025
*/

#include <iostream>

int main() {
	std::cout << "Fortune Teller \n";

	// ask for number (outside)
	int n = 0;
	int m = 0;
	std::cout << "Enter a number (between 1-4): ";
	std::cin >> n;

	// ask for second number (inside)
	if (n % 2 == 0) {
		std::cout << "Enter either 1 4 5 or 8: ";
		std::cin >> m;

		if (m == 1) {
			std::cout << "you are stinky";
		}
		else if (m == 4) {
			std::cout << "freddy fazbear will jumpscare you!";
		}
		else if (m == 5) {
			std::cout << "you will get a icecream!";
		}
		else if (m == 8) {
			std::cout << "you will win a game of fortnite";
		}
		else {
			std::cout << "please enter one of the numbers above";
		}
	}
	else {
		std::cout << "Enter either 3 6 2 or 7: ";
		std::cin >> m;
		if (m == 3) {
			std::cout << "you are lucky";
		}
		else if (m == 6) {
			std::cout << "you will step in poop";
		}
		else if (m == 2) {
			std::cout << "you will rise above them all";
		}
		else if (m == 7) {
			std::cout << "you will make it to 6 AM";
		}
		else {
			std::cout << "please enter one of the numbers above";
		}
	}
}


		// 1 2 3 4 (outside)
		// 1 2 3 4 5 6 7 8 (inside)
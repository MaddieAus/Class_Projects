/*
 Madison Austin
 CSCI 136 lab 3 - Enghanced Fortune Teller
*/


#include <iostream>
#include <string>

int main() {
    std::cout << "Fortune Teller \n";

    std::cout << "Welcome to the fortune picker! would you like to pick your fortune?: ";
    std::string Play = "Y"; // to play the fortune game
    std::string response;
    std::cin >> response;

    while (response == "y" || response == "yes" || response == "Y" || response == "Yes" ) { //checking if they want to play
        std::string color;
        std::cout << "Choose a color (e.g., blue, white, red, etc.): ";
        std::cin >> color;
        int fortuneC = color.length(); //length of the color

        if (fortuneC == 3) {
            std::cout << "you are stinky";
        }
        else if (fortuneC == 5) {
            std::cout << "freddy fazbear will jumpscare you!\n";
        }
        else if (fortuneC == 4) {
            std::cout << "you will get a icecream!\n";
        }
        else if (fortuneC == 6) {
            std::cout << "you will win a game of fortnite\n";
        }
        else {
            std::cout << "please enter a color in the rainbow\n";
        }
        std::cout << "Would you like to play again: "; //asking if they want to play again
        std::cin >> response;
    }
    std::cout << "Goodbye!\n" << std::endl;
}
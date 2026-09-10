#pragma once
#include <iostream>

using namespace std;
class Characters
{
private:
    int health = 100;  // Health variable
    //char person = '.';

public:

    char person = ' ';

    // Default constructor
    Characters();

    // Parameterized constructor
    Characters(int hearts);

    // Setter for health
    void setHearts(int health);

     char getperson();

    void setperson(char symbol);
};


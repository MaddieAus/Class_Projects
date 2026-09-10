/*
Madison Austin
2/21/2025
CSCI 136 OOP Part 1
*/


#include <iostream>
#include <string>
using namespace std;

class person {
	public:
		string name;
		double ID;
		double age;

		void print() {
			cout << ID << " " << name << " " << age << endl;
		}

};

class student : public person {
	public:
		string major;
		double GPA;

		void print() {
			cout << major << " " << GPA << endl;
		}
};

int main()
{
	person Person;
	Person.ID = 330094; // test - this isnt my actual ID i just made it up
	Person.name = "Maddie Austin"; // test
	Person.age = 20; // test

	Person.print();

	student Student;
	Student.major = "Computer Science"; // test
	Student.GPA = 3.9;

	Student.print();

}
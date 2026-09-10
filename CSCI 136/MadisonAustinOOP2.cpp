/*
Madison Austin
2/21/2025
CSCI 136 OOP Part 2 (Private)
*/

#include <iostream>
#include <string>
using namespace std;

class Person {
private:
    string name = " ";
    double ID = 0;
    double age = 0;
public:
    Person() {

    }
    // Setter methods
    void setID(double newID) {
        ID = newID;
    }
    void setName(const string& newName) {
        name = newName;
    }
    void setAge(double newAge) {
        age = newAge;
    }

    // Getter methods
    double getID() const {
        return ID;
    }
    string getName() const {
        return name;
    }
    double getAge() const {
        return age;
    }

    // Print function
    void print() const {
        cout << this->ID << " " << this->name << " " << this->age << endl;
    }
};

class Student : public Person { // Changed from private inheritance to public
private:
    string major = " ";
    double GPA = 0;
public:
    Student() {

    }
    // Setter methods
    void setMajor(const string& newMajor) {
        major = newMajor;
    }
    void setGPA(float newGPA) {
        GPA = newGPA;
    }

    // Print function
    void printStudent() const {
        // Print base class info (Person)
        print();
        // Print Student info
        cout << "Major: " << this-> major << " GPA: " <<this-> GPA << endl;
    }
};

int main() {
    // Create a Person object and set values
    Person person;
    person.setID(330094);
    person.setName("Maddie Austin");
    person.setAge(20);
    person.print();  // Prints: 330094 Maddie Austin 20

    // Create a Student object and set values
    Student student;
    student.setID(54321);            // Inherited from Person
    student.setName("Avrey Coombe");   // Inherited from Person
    student.setAge(20);              // Inherited from Person
    student.setMajor("Computer Science");
    student.setGPA(3.0);
    student.printStudent();  // Prints: 54321 Avrey Coombe 20 Major: Computer Science GPA: 3.0

}

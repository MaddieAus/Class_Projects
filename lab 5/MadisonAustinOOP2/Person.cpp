#include "Person.h"
#include <string>
#include <iostream>
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
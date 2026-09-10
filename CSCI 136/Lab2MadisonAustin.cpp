//it took me so long to figure out how to use visual studio 2022 oh my goodness. it's cool though

/* 
* Madison Austin
* CSCI 136 spring 2025
* Lab 2   1/24/2025
*/



#include <iostream>

int main()
{
    std::cout << "Hello World!\n \n"; //"hello world"

 // part 1 "asking name then printing name"
    std:: string x;
    std::cout << "Enter Your Name: ";
    std::cin >> x;
    std::cout << "Hello" << " " << x << "!" << "\n \n";

 // part 2 "ask for the year they were born, then output age in 2024"
    int y;
     std::cout << "what is your age in 2024? \n";
        std::cout << "Enter the year you were born: ";
        std::cin >> y;
    int YearMath = 2024 - y;
        std::cout << "Your age in 2024 is" << " " << YearMath << "\n \n";

 // part 3 "asking for two numbers to see if equal or not, if not then output smallest number"
    int n;
     std::cout << "is it equal? \n";
        std::cout << "Enter a number: ";
        std::cin >> n;
    int m;
        std::cout << "Enter another number: ";
        std::cin >> m;
        if (n == m) {
           std::cout << n << " and " << m << " are equal \n\n";
        }
        else if (n > m){
            std::cout << m << " is the smallest number\n\n";
        }
        else {
            std::cout << n << " is the smallest number" << "\n \n";
        }
    
 // part 4 "the sum of all even numbers between 1 - 101"
         std::cout << "All even! \n";
         int sum = 0;
         for (int i = 1; i < 101; i++) {
             if (i % 2 == 0); {
                 sum = i + sum;
             }
         }
         std::cout << sum <<"\n \n";

 // part 5 "input an integer repeatedly untill -999 then output the sum and average of the numbers entered" (-999 not included)
         int s = 0;
         int a = 0;
         int c = -1;
         for (int i = 0; i != -999; std::cin >> i) {
             std::cout << "Enter a number: ";
             c++;
             s = i + s;
         }
         a = s / c;
         std::cout << "here is the sum: " << s << " and here is the average: " << a ;
}

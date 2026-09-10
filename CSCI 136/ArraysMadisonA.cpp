/*
Madison Austin
CSCI 136 2/10/2025
Arrays
there is a lot of comments on here and they are mostly for me 
*/

#include <iostream> // just includes basic stuff like, std::cout<< and std::cin>>
#include <vector> // this is the containers library such as, operators and bool
#include <algorithm> // this is the algorithm library which makes is so the user input does somthing to the array
/*I looked up the librarys for c++ https://en.cppreference.com/w/cpp/standard_library , because i didnt know what you ment by array library */

using namespace std;

//utility functions start
void random_nums (vector<int>& arr) { // setting the parameters
    for (int i = 0; i < arr.size(); i++) {
        arr[i] = rand() % 10 + 1; // remember code starts counting at 0 
    }
}

void known_nums(vector<int>& arr) { // setting parameters
    arr = { 1, 5, 3, 9, 8, 2, 6, 4, 7, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
}

void print_array(const vector<int>& arr) { // this sets parameters and const makes it read only
    cout << "Array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl; // another way to end a line
}
//utility functions end

//1. Largest number. Return and output the largest number in an array.
int find_largest(const vector<int>& arr) {
    int largest = arr[0];
    for (int num : arr) {
        if (num > largest) {
            largest = num;
        }
    }
    return largest;
}

//2. Linear search.Prompt the user to enter a number, n.Search the array for n.Return the position(index) of n, if found; otherwise return -1.
int linear_search(const vector<int>& arr, int n) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == n) {
            return i; // Return the index of the number if found
        }
    }
    return -1; // Return -1 if not found
}

//3. Second largest.Return the second largest number in the array.The array may contain up to 19 duplicates of any number.
int find_second_largest(const vector<int>& arr) {
    int largest = arr[0];
    int second_largest = INT_MIN; // gives the smallest number or what we set as that number like a placeholder

    for (int num : arr) {
        if (num > largest) {
            second_largest = largest;
            largest = num;
        }
        else if (num > second_largest && num < largest) { // && is the AND operator
            second_largest = num;
        }
    }
    return second_largest;
}

//4. k largest numbers.Write a program to output the k largest numbers in an array, where k is provided by the user and the array may contain up to (20 – k) duplicates of any number.
vector<int> k_largest(const vector<int>& arr, int k) {
    vector<int> sorted_arr = arr;
    sort(sorted_arr.begin(), sorted_arr.end(), greater<int>()); //indacates the beginning and end of the array and then sorts the array and indacates the biggest int
    vector<int> result(sorted_arr.begin(), sorted_arr.begin() + k); //this takes the sorted and puts the bigger in the beginning
    return result;
}

//5. Even and odd.Organize the array so that all the even numbers are at the beginning of the array, and the odd numbers are at the end.There will be at least one even and at least one odd number in the array.
vector<int> even_odd(const vector<int>& arr) {
    vector<int> even, odd;
    for (int num : arr) {
        if (num % 2 == 0) { // this makes sure the number is even 
            even.push_back(num);
        }
        else {
            odd.push_back(num);
        }
    }
    even.insert(even.end(), odd.begin(), odd.end()); // this makes the even numbers go in the beginning and the odd numbers go in the back of the line
    return even;
}

//6. Reverse.Reverse the order of all the numbers in the array.
vector<int> reverse_array(const vector<int>& arr) {
    vector<int> reversed_arr = arr;
    reverse(reversed_arr.begin(), reversed_arr.end()); // this reverses the last function 
    return reversed_arr;
}

int main()
{
    std::cout << "Array codes\n";

    srand(time(0)); // Seed the random number generator

    vector<int> arr(20);  // Declare an array of 20 integers

    // Populate the array with known numbers for testing
    known_nums(arr); // calling the function
    print_array(arr);

    // Largest number 1
    cout << "Largest number: " << find_largest(arr) << endl;

    // Linear search 2
    int n;
    cout << "Enter a number to search for: ";
    cin >> n;
    int index = linear_search(arr, n);
    if (index != -1) {
        cout << "Number " << n << " found at index " << index << "." << endl;
    }
    else {
        cout << "Number " << n << " not found." << endl;
    }

    // Second largest number 3
    cout << "Second largest number: " << find_second_largest(arr) << endl;

    // k largest numbers 4
    int k;
    cout << "Enter how many largest numbers you want: ";
    cin >> k;
    vector<int> largest_k = k_largest(arr, k); // this declares the function as a int
    cout << "The " << k << " largest numbers are: ";
    for (int num : largest_k) {
        cout << num << " ";
    }
    cout << endl;

    // Organize even and odd numbers 5
    vector<int> organized_arr = even_odd(arr); // this declares the function as a int
    cout << "Array with even numbers at the beginning and odd at the end: ";
    print_array(organized_arr);

    // Reverse the array 6
    vector<int> reversed_arr = reverse_array(arr); // this declares the function as a int 
    cout << "Reversed array: ";
    print_array(reversed_arr);

    return 0;
}
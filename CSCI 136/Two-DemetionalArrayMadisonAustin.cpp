
/*
Madison Austin
CSCI Two Demetinal Array
3/5/2025
*/

#include <iostream>
#include <cstdlib>

using namespace std;

// Constants for array size
const int ROWS = 4;
const int COLS = 5;

// Function to populate the array with random integers between 11 and 99
void populateArray(int arr[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            arr[i][j] = rand() % 89 + 11;  // Random numbers between 11 and 99
        }
    }
}

// Function to print the array in rows and columns
void printArray(int arr[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}

// Function to calculate and return the sum of a specific row
int rowSum(int arr[ROWS][COLS], int row) {
    int sum = 0;
    for (int j = 0; j < COLS; j++) {
        sum += arr[row][j];
    }
    return sum;
}

// Function to calculate and return the sum of the entire array
int totalSum(int arr[ROWS][COLS]) {
    int sum = 0;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            sum += arr[i][j];
        }
    }
    return sum;
}

// Function to print the array with row sums and column sums
void printArrayWithSums(int arr[ROWS][COLS]) {
    int colSum[COLS] = { 0 };  // Array to store the column sums

    // Print the array with row sums at the end of each row
    for (int i = 0; i < ROWS; i++) {
        int rowTotal = 0;
        for (int j = 0; j < COLS; j++) {
            cout << arr[i][j] << " ";
            rowTotal += arr[i][j];
            colSum[j] += arr[i][j];  // Add to column sum
        }
        cout << "| " << rowTotal << endl;
    }

    // Print the column sums
    cout << "----------------------" << endl;
    for (int i = 0; i < COLS; i++) {
        cout << colSum[i] << " ";
    }
    cout << endl;

    // Print the total sum
    cout << "Total Sum: " << totalSum(arr) << endl;
}

// Function to set the value at position (x, y) and adjacent cells to -1
void setAdjacentToMinusOne(int arr[ROWS][COLS], int x, int y) {
    // Ensure that x and y are within bounds
    if (x >= 0 && x < ROWS && y >= 0 && y < COLS) {
        // Set the cell at (x, y) to -1
        arr[x][y] = -1;

        // Set the adjacent cells to -1 (if they are within bounds)
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                int newX = x + i;
                int newY = y + j;

                // Check if the new position is within bounds
                if (newX >= 0 && newX < ROWS && newY >= 0 && newY < COLS && (i != 0 || j != 0)) {
                    arr[newX][newY] = -1;
                }
            }
        }
    }
    else {
        cout << "Invalid position!" << endl; //error message
    }
}

int main() {
    // Initialize random seed
    srand(time(0));

    // Declare the 2D array
    int arr[ROWS][COLS];

    // Populate the array with random numbers
    populateArray(arr);

    // Print the array before modification
    cout << "Before:" << endl;
    printArray(arr);
    cout << endl;

    // User input for x and y
    int x, y;
    cout << "Enter the x and y positions (0 <= x < " << ROWS << ", 0 <= y < " << COLS << "): ";
    cin >> x >> y;

    // Modify the array based on user input
    setAdjacentToMinusOne(arr, x, y);

    // Print the array after modification
    cout << "After:" << endl;
    printArray(arr);
    cout << endl;

    // Print the array with row sums and column sums
    cout << "Array with row and column sums:" << endl;
    printArrayWithSums(arr);

    return 0;
}

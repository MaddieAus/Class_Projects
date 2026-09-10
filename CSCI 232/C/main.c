//#define clearBuffer() while (getchar() != '\n');
#include <stdio.h>
#include <stdbool.h>
#include "unity.h"
#include <assert.h>

// Functions required by Unity (they can remain empty if not used)
void setUp(void) 
{
    // Executed before each test
}
void tearDown(void) 
{
    // Executed after each test
}

// int add(int a, int b) 
// {
//     return a + b;
// }

// void test_add_should_return_sum(void) 
// {
// 	int x = 2;
// 	TEST_ASSERT_EQUAL_INT(1, x);
//     TEST_ASSERT_EQUAL(5, add(2, 3));
// 	//assert(x == 1);
// }
	//in main
	//UNITY_BEGIN();
    //RUN_TEST(test_add_should_return_sum);
    //int r =  UNITY_END();
	//printf("%d\n", r);

	//(int) 5;
	//int * intPointer;
	//intPointer = &x;

	//printf("the adress of x %d\n", &x);

	
	//printf("value from adress %d\n" , * intPointer);

	//printf("%d\n" , x);

	//printf("value of myPointer %d\n" , * intPointer);


	//char string[12] = "Hello world";
	//printf("%s", string);



struct Node {
	int value;
	struct Node * nextPtr;	
};

int main() 
{
	struct Node first;
	struct Node second;
	struct Node third;

	first.value = 5;
	first.nextPtr = NULL;

	
	first.value = 6;
	first.nextPtr = NULL;

	
	first.value = 7;
	first.nextPtr = NULL;

	first.nextPtr = &second;
	second.nextPtr = &third;

	struct Node * headPointer;

	headPointer = &first;

	
	getchar();
	return 0; //return r
}

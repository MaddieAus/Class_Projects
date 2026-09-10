//#include <assert.h>   // commented out, not needed
int a;
int * p;
#include "code.h"
#include "tests.h"
#include "unity.h"

int result; // global variable for test results

// ----------------- UNITY SETUP / TEARDOWN -----------------
struct Node * Header;
struct Node * neck;
struct Node * shoulders;
struct Node * knees;
struct Node * toes;

struct Node *head;

void setUp() 
{  
    head = NULL;
    // Header= NULL;
    // neck= CreatNode(30,NULL);
    // shoulders= CreatNode(20,NULL);
    // knees= CreatNode(10,NULL);
    // toes= CreatNode(5,NULL);
    // a = 4;
    // p = (int*) malloc(sizeof(int));
    // *p = 5;
    // result = 0;
}

void tearDown() 
{
        struct Node *temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }

    // free(p);
    // result = 0;
}

// ----------------- TEST FUNCTIONS -----------------

void test_multiply_basic() 
{
    result = multiply(a, *p);
    TEST_ASSERT_EQUAL(20, result);
}

void test_multiply_with_zero() 
{
    *p = 0;
    result = multiply(a, *p);
    TEST_ASSERT_EQUAL(0, result);
}

void test_multiply_negative() 
{
    *p = -3;
    result = multiply(a, *p);
    TEST_ASSERT_EQUAL(-12, result);
}

void test_addOne_basic() 
{
    result = addOne(p);
    TEST_ASSERT_EQUAL(6, result);
}

void test_addOne_negative() 
{
    *p = -3;
    result = addOne(p);
    TEST_ASSERT_EQUAL(-1, result); // tests proper error handling
}

// ----------------- RUN ALL TESTS -----------------
int run_unity_tests(void) 
{
    UNITY_BEGIN();
    RUN_TEST(test_multiply_basic);     
    RUN_TEST(test_multiply_with_zero); 
    RUN_TEST(test_multiply_negative);

    RUN_TEST(test_addOne_basic);
    RUN_TEST(test_addOne_negative);
    return UNITY_END();
}

//write tests for functions in here like exsample above
// Helper
int countNodes(struct Node *head) {
    int count = 0;
    while (head != NULL) {
        count++;
        head = head->nextPtr;
    }
    return count;
}

void test_addFirst(void) {
    struct Node *list = NULL;
    list = addFirst(list, 10);
    TEST_ASSERT_NOT_NULL(list);
    TEST_ASSERT_EQUAL(10, list->value);

    list = addFirst(list, 5);
    TEST_ASSERT_EQUAL(5, list->value);
    TEST_ASSERT_EQUAL(10, list->nextPtr->value);
}

void test_addLast(void) {
    struct Node *list = NULL;
    list = addLast(list, 1);
    list = addLast(list, 2);
    list = addLast(list, 3);

    TEST_ASSERT_EQUAL(1, list->value);
    TEST_ASSERT_EQUAL(2, list->nextPtr->value);
    TEST_ASSERT_EQUAL(3, list->nextPtr->nextPtr->value);
    TEST_ASSERT_NULL(list->nextPtr->nextPtr->nextPtr);
}

void test_deleteFirst(void) {
    struct Node *list = NULL;
    list = addFirst(list, 10);
    list = addFirst(list, 20);
    list = deleteFirst(list);

    TEST_ASSERT_EQUAL(10, list->value);
    list = deleteFirst(list);
    TEST_ASSERT_NULL(list);
}

void test_deleteLast(void) {
    struct Node *list = NULL;
    list = addLast(list, 1);
    list = addLast(list, 2);
    list = addLast(list, 3);

    list = deleteLast(list);
    TEST_ASSERT_EQUAL(2, countNodes(list));
    TEST_ASSERT_EQUAL(2, list->nextPtr->value);

    list = deleteLast(list);
    TEST_ASSERT_EQUAL(1, list->value);

    list = deleteLast(list);
    TEST_ASSERT_NULL(list);
}

void test_deleteValue(void) {
    struct Node *list = NULL;
    list = addLast(list, 10);
    list = addLast(list, 20);
    list = addLast(list, 30);

    list = deleteValue(list, 20);
    TEST_ASSERT_EQUAL(10, list->value);
    TEST_ASSERT_EQUAL(30, list->nextPtr->value);

    list = deleteValue(list, 10);
    TEST_ASSERT_EQUAL(30, list->value);

    list = deleteValue(list, 30);
    TEST_ASSERT_NULL(list);
}

void test_valueExists(void) {
    struct Node *list = NULL;
    list = addFirst(list, 5);
    list = addFirst(list, 10);
    list = addFirst(list, 15);

    TEST_ASSERT_TRUE(valueExists(list, 5));
    TEST_ASSERT_TRUE(valueExists(list, 10));
    TEST_ASSERT_FALSE(valueExists(list, 100));
}

void test_addOne_multiply(void) {
    int x = 5;
    TEST_ASSERT_EQUAL(6, addOne(&x));
    TEST_ASSERT_EQUAL(6, x);

    TEST_ASSERT_EQUAL(6, multiply(2, 3));
    TEST_ASSERT_EQUAL(-8, multiply(-2, 4));
}


// Test sorting in ascending order
void test_insertionSortList_ascending(void) {
    createSampleList();
    head = insertionSortList(head, 1);

    TEST_ASSERT_NOT_NULL(head);
    TEST_ASSERT_EQUAL(1, head->data);
    TEST_ASSERT_EQUAL(2, head->next->data);
    TEST_ASSERT_EQUAL(3, head->next->next->data);
    TEST_ASSERT_NULL(head->next->next->next);
}


// Test sorting in descending order
void test_insertionSortList_descending(void) {
    createSampleList();
    head = insertionSortList(head, 0);

    TEST_ASSERT_NOT_NULL(head);
    TEST_ASSERT_EQUAL(3, head->data);
    TEST_ASSERT_EQUAL(2, head->next->data);
    TEST_ASSERT_EQUAL(1, head->next->next->data);
    TEST_ASSERT_NULL(head->next->next->next);
}

// Test passing NULL pointer
void test_insertionSortList_nullPointer(void) {
    struct Node *result = insertionSortList(NULL, 1);
    TEST_ASSERT_NULL(result);  // Should return NULL
}

// Test passing invalid ascending parameter
void test_insertionSortList_invalidAscendingValue(void) {
    createSampleList();
    struct Node *result = insertionSortList(head, 5); // Invalid
    TEST_ASSERT_NULL(result);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_addFirst);
    RUN_TEST(test_addLast);
    RUN_TEST(test_deleteFirst);
    RUN_TEST(test_deleteLast);
    RUN_TEST(test_deleteValue);
    RUN_TEST(test_valueExists);
    RUN_TEST(test_addOne_multiply);

    RUN_TEST(test_insertionSortList_ascending);
    RUN_TEST(test_insertionSortList_descending);
    RUN_TEST(test_insertionSortList_nullPointer);
    RUN_TEST(test_insertionSortList_invalidAscendingValue);

    return UNITY_END();
}
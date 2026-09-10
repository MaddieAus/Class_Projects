#include "unity.h"
#include "code.h"
#include <math.h>   // for NAN

void setUp(void) {}
void tearDown(void) {}

// Test 1: Valid full binary tree
void test_valid_full_tree(void) {
    float tree[] = {1.0, 2.0, 3.0, NAN, NAN, NAN, NAN};
    TEST_ASSERT_TRUE(is_valid_binary_tree(tree, 7));
}

// Test 2: Root is NaN (invalid)
void test_invalid_root_nan(void) {
    float tree[] = {NAN, 2.0, 3.0};
    TEST_ASSERT_FALSE(is_valid_binary_tree(tree, 3));
}

// Test 3: Child exists but parent is NaN (invalid)
void test_invalid_child_without_parent(void) {
    float tree[] = {1.0, NAN, 3.0, 4.0};
    TEST_ASSERT_FALSE(is_valid_binary_tree(tree, 4));
}

// Test 4: Empty tree (invalid)
void test_empty_tree(void) {
    float tree[] = {};
    TEST_ASSERT_FALSE(is_valid_binary_tree(tree, 0));
}

// Test 5: Valid tree with some NaN leaves
void test_valid_with_nan_leaves(void) {
    float tree[] = {10.0, 5.0, 15.0, NAN, 8.0, NAN, NAN};
    TEST_ASSERT_TRUE(is_valid_binary_tree(tree, 7));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_valid_full_tree);
    RUN_TEST(test_invalid_root_nan);
    RUN_TEST(test_invalid_child_without_parent);
    RUN_TEST(test_empty_tree);
    RUN_TEST(test_valid_with_nan_leaves);
    return UNITY_END();
}

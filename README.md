## Homework Instructions
MBAI 401 Tech Onramp<br>
Suggested completion date: 09/02/21

Test Instructions
---
- This homework uses the unittest testing framework instead of the pytest testing framework. 
- However, it behaves very similarly. At any point, you can run individual tests by clicking 
  on the green play button next to the tests. 
- You can also run all the tests by right-clicking on the runner.py and choosing Run. This will run all 
  the tests for all the problems and provide useful information.
  
Problem 1 - Practice with Lists, Sets, and Dictionaries
---
1. Create a file named `problem1.py` in the `p1` package.
2. Create a function named `has_dups_list` that takes a list of any values and returns a boolean. 
    - The function should return True if there are duplicates in the list and False otherwise. Solve this using iteration (not
recursion). You may not use dictionaries or sets in your solution for this problem - only lists. 
    - Uncomment the second import statement at the top of the `test_problem1.py` file. 
    - Uncomment and run the tests `test_has_dups_list_unique`, `test_has_dups_list`. Remove the pass keyword. 
    - You can also run the tests and get useful feedback by right-clicking on the `runner.py` file and choosing 
   `Run runner`.
3. Create a function named `has_dups_dict` that takes a list of any values and returns a boolean. 
    - The function should return True if there are duplicates in the list and False otherwise. In this version, 
      solve the problem using a dictionary.
    - Uncomment the third import statement at the top of the `test_problem1.py` file. 
    - Uncomment and run the tests `test_has_dups_dict_unique`, `test_has_dups_dict`. Remove the pass keyword. 
    - You can also run the tests and get useful feedback by right-clicking on the `runner.py` file and choosing 
   `Run runner`.
4. Create a function named `has_dups_set` that takes a list of any values and returns a boolean. 
    - The function should return True if there are duplicates in the list and False otherwise. In this version, 
      solve the problem using a set.
    - Uncomment the fourth import statement at the top of the `test_problem1.py` file. 
    - Uncomment and run the tests `test_has_dups_set_unique`, `test_has_dups_set`. Remove the pass keyword. 
    - You can also run the tests and get useful feedback by right-clicking on the `runner.py` file and choosing 
   `Run runner`.
5. Create a function named `time_func` that takes a function as a parameter. It should create a list of 10000 values 
(use `list(range(0, 10000))`). Time the result of applying the function to the list of values and return the
result. Remember that functions can be assigned to variables and be passed around! Use the `time` package imported above. 
   - Create an `if __name__ == '__main__'` block and pass in each of the functions that you wrote to the `time_func` and 
     print out the results. 
   - In a comment, explain which of your functions is consistently the fastest and why the others are slower.
   
Problem 2 - Practice with Recursion and Objects
---
1. Create a class named `LetterCount` in the `p2` package. A `LetterCount` object is an object that keeps track of a letter
   and its associated count.
   - This class has should have two attributes, `letter` and `count`.
   - This class should also have an `__eq__` method. Two `LetterCount` objects are equal if their corresponding 
     `letter` and `count` are equal.
   - Uncomment the import at the top of the `test_letter_count.py` file and uncomment and run the tests in
     the file. Remove the pass keyword.
2. Create a file named `counts` in the `p2` package. Then, create a function named `count_by_letter`. 
   - The function takes a list of letters (lowercase) and a "dictionary" (a list of one-word strings) as arguments.
   - It should count how often each letter is used as the first letter of the words in the given list of
     strings, independent of case.  
   - The function should return a list of `LetterCounts`. 
   - For example, if the list of strings is `('happy', 'hula', 'henry', 'apples', 'hoopla')`, 
     and the list of letters is `('a', 'c', 'h')` then the resulting list of `LetterCounts` will have 
     a `LetterCount` of 'a' and 1, a `LetterCount` of 'c' and 0, and a `LetterCount` of 'h' and 4 (in that
     order).
   - Do **not** use iteration - only recursion. Do **not** use lambdas.
   - You may find the following Python string methods helpful:
     * `lower()`
     * `startswith()`
   - You can create helper (i.e. auxiliary) functions to help organize your code (remember, functions can
     call other functions).
   - Don't forget to import the `letter_count` module! Use relative imports!
   - Uncomment the import at the top of the `test_counts.py` file and uncomment and run the tests in
     the file. Remove the pass keyword.

Problem 3 - Binary Search Trees and Recursion
---
1. In the `p3` package, you have been provided with a module named `bst.py` that contains a
   `Node` class and a `BST` class to represent a binary search tree (bst). In addition, you 
   have also been provided with the `insert` method and the `create` method so that you can 
   create a bst. A small sample tree has been provided for you.
2. Write the method `traverse_pre` that does not take any arguments (only has the `self` parameter).
   This method should recursively traverse a binary search tree and return the list of nodes
   traversed in preorder (root-left-right).
   - You will need a helper (auxiliary) method so that you can pass in the root node to start 
     traversing the tree. The `traverse_pre` method should call the helper method. You can make
     this helper method a nested function and then you won't have to include the `self` paramter.
     See the `insert` method for an example.
   - The root of a `BST` is a `Node` that has the following attributes: `val` (the value
     of the node), `left` (the left child of the node), `right` (the right child of the node).
   - Uncomment the import at the top of the `test_bst.py` file and uncomment and run the tests in
     the file that begin with `test_pre...`. Remove the pass keyword.
 3. Write the method `traverse_post` that does not take any arguments (only has the `self` parameter).
   This method should recursively traverse a binary search tree and return the list of nodes
   traversed in postorder (left-right-root).
   - You will need a helper (auxiliary) method so that you can pass in the root node to start 
     traversing the tree. The `traverse_post` method should call the helper method. You can make
     this helper method a nested function and then you won't have to include the `self` paramter.
     See the `insert` method for an example.
   - The root of a `BST` is a `Node` that has the following attributes: `val` (the value
     of the node), `left` (the left child of the node), `right` (the right child of the node).
   - Uncomment and run the tests in the `test_bst.py` file that begin with `test_post...`. 
     Remove the pass keyword.
     
**Push your code to GitHub!**
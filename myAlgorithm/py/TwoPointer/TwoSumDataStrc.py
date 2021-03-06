
"""
Description

English
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:

add(1); add(3); add(5);
find(4) // return true
find(7) // return false
"""
class TwoSum:
    def __init__(self):
        self.store =[]

    def add(self, val):
        self.store.append(val)
        print self.store

    def isInStore(self, val):
        checked = []
        for ele in self.store:
            if val - ele in checked:
                return True
            else:
                checked.append(ele)
        return False

if __name__=="__main__":
    test = TwoSum()
    test.add(1)
    test.add(4)
    test.add(2)
    test.add(6)
    print test.isInStore(6)
    print test.isInStore(9)
    test.add(5)
    print test.isInStore(9)
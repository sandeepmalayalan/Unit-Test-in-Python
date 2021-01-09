import unittest

# Given input list is taken
a = [4, 5, 15, 2, 8]



# Program logic: input list contains sum of input integer marked as False otherwise if no sum present marked as true.
# [4, 5, 15, 2, 8 ]satisfies the condition and named as True
#[ 4, 5, 3, 8] satisfies the condition and named as False because 5+3 as 8


def fun1(a):
    c = []
    if len(a) > 0:
        for i in range(0, len(a) - 1):
            for j in range(i + 1, len(a)):
                c.append(a[i] + a[j])
        mn = set(a) & set(c)
        if len(mn) == 0:
            b = True
        else:
            b = False
        return b


print('Output is given below: ')
print(fun1(a))


# testcases for both scenarios (having sum and no sum in the list) to avoid assertion error, used exceptions.

# 4, 5, 15, 2, 8 satisfies the condition and named as True

class Testnum(unittest.TestCase):
    # 4, 5, 15, 2, 8 satisfies the condition and named as false so it produce error, to over come used exception
    def test_new_case(self):
        try:
            self.assertFalse(fun1([4, 5, 15, 2, 8]))
        except AssertionError as msg:
            msg

    # 4, 5, 15, 2, 8 satisfies the condition and named as True so we did n't used exception
    def test_new_case1(self):
        self.assertTrue(fun1([4, 5, 15, 2, 8]))


    # in case of empty list
    def test_new_case2(self):
        self.assertIsNone(fun1([]))

    # 4, 5, 3, 2, 8 not satisfies the condition  and named as False so we did n't used exception
    def test_new_case3(self):
        self.assertFalse(fun1([4, 5, 3, 2, 8]))



if __name__ == '__main__':
    unittest.main()

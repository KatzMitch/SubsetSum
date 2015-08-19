# Mitchell Katz
# subsetsum.py
# Program inputs numbers until a sentinel, then calculate whether ther is a
# combination of those numbers that adds up to a certain sum
# Thursday, Feb. 19, 2015

from numpy import ndarray

"""
This function is based off the idea that if you can sum to a smaller number
while only using some of the numbers, then you can get a bigger number with
what is left. I make recursive calls down the list seeing if you can sum to
some value that represents the goal - a value in the list. The problem with
this approach is the sheer amount of recursive calls that do the same
calculations over and over again.
"""
def isSubSumNaive(list, index, sum):
        # Found a solution
        if sum is 0:
                return True

        # Out of values to subtract
        if index is 0 and sum is not 0:
                return False

        # See if you can sum up to current value through recursive call
        if list[index - 1] > sum:
                return isSubSumNaive(list, index - 1, sum)

        # Recursive call to see if you can sum up to either the current value
        # with the remaining elements or
        return (isSubSumNaive(list, index - 1, sum) or
               isSubSumNaive(list, index - 1, (sum - list[index - 1])))

"""
This function works approximately the same way as the naive function, but it
creates a table of boolean values to track whether a certain number can be
summed up to with the previous numbers so you don't accidentally recurse over
values that you already know you can or cannot get.
"""
def isSubSumTable(list, sum):
        # Create a 2D table where the value of table[i][j] is true if there is
        # a subset of the list from 0-j with sum equal to i
        table = ndarray([sum + 1, len(list) + 1], bool)

        # Initialize table to false
        for i in range(sum):
                for j in range(len(list)):
                        table[i][j] = False

        # There is always a subset that can equal 0
        for j in range(len(list) + 1):
                table[0][j] = True
        
        # There are no empty subsets with non-zero sums 
        for i in range((sum) + 1):
                table[i][0] = False

        # Fill the table moving up in sums
        for i in range((sum) + 1)[1:]:
                for j in range(len(list) + 1)[1:]:
                        # If you could sum up to the previous value, then you
                        # Can add an element and still have a way to sum to
                        # that value
                        table[i][j] = table[i][j - 1]
                        if i >= list[j - 1]:
                                # If there is a smaller number that you can
                                # sum to with fewer elements, then you can also
                                # sum to that sum plus one more element
                                table[i][j] = (table[i][j] or 
                                              table[i - list[j - 1]][j - 1])
        return table[sum][len(list)]

# Main inputs set, number to sum to, calls the sum function and prints the
# result
def main():
        nums = []
        n = 0
        # Input set of numbers
        while n is not 'q':
                n = raw_input("Add a number to the set or enter 'q' to end: ")
                if n is not 'q':
                        nums.append(int(n))

        print "The set is ", nums

        # Sum to calculate
        goal = int(raw_input("What number should we sum to? "))

        # Make call and print result
        print "N of {0}: {1}".format(goal, ("Yes" if isSubSumTable(nums, goal) 
                                            else "No"))

if __name__ == "__main__":
        main()
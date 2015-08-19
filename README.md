subsum.py

This is just a quick program I wrote to help teach myself about dynamic
programming. The program inputs a set of numbers and then a set of value.
It then checks whether there is some subset of those numbers that add up to the value. I wrote both a naive approach and a dynamic programming
approach.

The naive approach runs in T(n) = 2(n-1) + O(1) time. The dynamic 
approach runs in T(n, sum) = O(n*sum) where n is the number of
elements in the set and sum is the number you are summing to.

Thursday, Febuary 19, 2014
Mitchell Katz
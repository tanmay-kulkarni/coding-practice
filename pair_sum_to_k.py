# Given an array of integers arr and an integer k, create a boolean function that checks 
# if there exists two elements in arr such that we get k when we add them together

import argparse
from itertools import combinations

# This function will generate 2-combinations from the given array
# Use it if you don't want to use the itertools package
def generate_combinations(arr):
    return [(i,j) for i in arr for j in arr if i != j]

parser = argparse.ArgumentParser(description="This program tells if the given arr has a combination of elements that sum up to k")
parser.add_argument('--arr', type=str, required=True, help='Integer values, separated by commas', metavar='N')
parser.add_argument('--sum', type=int, required=True, help='Sum value', metavar='N')
args = parser.parse_args()

def sum_to_k(arr, k):

    possible_combinations = list(combinations(arr, 2))

    for pair in possible_combinations:
        if sum(pair) == k:
            return True, pair
    
    return False, None
        

if __name__ == '__main__':

    arr  = [int(num) for num in args.arr.split(',')]
    k = args.sum

    result, pair = sum_to_k(arr, k)

    if result:
        print(f"The given array has two elements that sum up to {k}... {pair}")
    else:
        print(f"There are no elements in this array that add up to {k}")
#!/bin/python3

from collections import defaultdict

# From the problem, here: https://www.hackerrank.com/challenges/frequency-queries/problem

# Essentially, the logic here is that we want to build
# up a representation of a dataset of numbers, that can have multiples
# of the same number. We want to keep track of how many of each number
# we have.

# We can do this easily with a python dictionary, where our keys
# are the different numbers we are tracking and the values
# are how many of that number we have. We use defaultdict which allows
# an initial value of zero whenever we try to add 1 to a value
# that is not already in the dictionary. Whenever we find an insert
# operation, we just add 1 to our dict for the number. When we find a remove,
# we subtract 1 (if the value we are removing is already in our dict).

# The tricky part is checking if any key in our dictionary has a particular
# value, which is what the frequency query is. We don't want to search
# through our entire dictionary every time, which could get ugly and turn
# this into an O(N^2) real fast. What we can do is make another dictionary 
# that has frequency values as its keys, and keeps a set of the numbers in
# our dataset that have that frequency. We will just need to be sure
# to update the freq_dict every time we add or remove something.

# Using these two dictionaries gives us a worse case aux space complexity
# of O(N). We have a time complexity of O(N), since we just do a constant
# number of operations for every q in queries.

# Complete the freqQuery function below.
def freqQuery(queries):
    # dataset
    data = defaultdict(lambda: 0)
    # frequency dictionary
    freq_dict = defaultdict(lambda: set())
    # output array of 1s and 0s
    type_3_outs = []

    for q in queries: # O(n) time here for the number of queries
        # query type 1
        if (q[0] == 1):
            # remove from the freq_dict, since
            # the frequency is changing
            # use discard, because this frequency may not be
            # yet in the dict
            freq_dict[data[q[1]]].discard(q[1])

            data[q[1]] += 1
            # add the new frequency of q[1] to the
            # frequency dict
            freq_dict[data[q[1]]].add(q[1])

        # query type 2
        elif (q[0] == 2):
            if (data[q[1]] != 0):
                # remove from the freq_dict, since
                # the frequency is changing
                freq_dict[data[q[1]]].discard(q[1])

                data[q[1]] -= 1
                # add the new frequency of q[1] to the
                # frequency dict
                freq_dict[data[q[1]]].add(q[1])

        # query type 3
        elif (q[0] == 3):
            if freq_dict[q[1]] != set():
                type_3_outs.append(1)
            else:
                type_3_outs.append(0)


        else:
            raise Exception('Invalid query operation')
            
    return type_3_outs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

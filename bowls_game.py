'''
 * * * * *
  * * * *
   * * *
    * *
     *

n = 5 - number of rows

compute how many bowls we need given n
for n = 5, result = 15
'''
n = 5
# solution cheese
def count_bowls(n):
    i = 1
    bowls = 0
    while i <= n:
        bowls += i
        i += 1
    return bowls
# else not needed
#print(count_bowls(n))

# solution non loop - recursion -> sensible when we work on trees structures (like files, folders, nested folders)
def count_bowls_recurse(n):
    if n == 1:
        return 1
    else:
        return n + count_bowls_recurse(n-1)

#result = count_bowls_recurse(n)
#print(result)

# looking at the difference between previous and current state, recursion has a maximum depth (limit)
# of 999 recursions (or further depending on coding) - due to calling the function over and over it
# breaks on memory loss

# useful on tree structures, cause there we don't know how many times we have to go inside (how many loops to make)
# if we can replace it with a loop - we should, but sometimes you can't - better for our exercise with folder size
# if it is file - count size, if a folder - recurse

from time import time

# best solution
def count_bowls_sequence(n):
    return (n*(n+1))/2

#print(count_bowls_sequence(n))

def time_func(func,n): # passing the definition of a function as a parameter - not possible in most languages
    print(f'Running {func.__name__} for n={n}')
    t0 = time()
    res = func(n) # func becomes the definition of the function
    t1 = time()
    elapsed_time = t1 - t0
    print(f'Result: {res}')
    print(f'Elapsed time: {elapsed_time}')

print(time_func(count_bowls, n)) # count_bowls(n) wouldn't work, cause then it would be interpreted as a function
# that would be ran as the first one and the result would be calculated in that line -> triggering it before
# time_func. We want it the opposite way. This version makes the reference to the function in memory reversing
# the way in which they are ran.
# with very big values of n this becomes a longer process

# print(time_func(count_bowls_recurse, n))
# since we ran recursion from another function, the limit of maximum recursion would drop by 1 to 998.
# recursion is the slowest and has the limit

print(time_func(count_bowls_sequence, n))
# the fastest and barely changes with values of n
# it is like that due to computational complexity - simple loop scales in a linear way
# in time it takes to perform (as it depends only on n - with amount of operations it has to perform).
# also different operations (like n^n or n*log(n)) might scale differently dependent on their complexity.
# Sequence is (near - changes are negligible) constant time, because it always performs just 3 operations.

# in most cases (incl: databases) time is stored as a float = timestamp.


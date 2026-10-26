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

# solution cheese
def count_bowls(n):
    i = 1
    bowls = 0
    while i <= n:
        bowls += i
        i += 1
    return bowls
# else not needed
print(count_bowls(5))

# solution non loop - recursion -> sensible when we work on trees structures (like files, folders, nested folders)
def count_bowls_recurse(n):
    if n == 1:
        return 1
    else:
        return n + count_bowls_recurse(n-1)

result = count_bowls_recurse(5)
print(result)

# looking at the difference between previous and current state, recursion has a maximum depth (limit)
# of 999 recursions (or further depending on coding) - due to calling the function over and over it
# breaks on memory loss

# useful on tree structures, cause there we don't know how many times we have to go inside (how many loops to make)
# if we can replace it with a loop - we should, but sometimes you can't - better for our exercise with folder size
# if it is file - count size, if a folder - recurse

# best solution
def count_bowls_sequence(n):
    return (n*(n+1))/2
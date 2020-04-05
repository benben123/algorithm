# Permutations of an Array of Arrays: Suppose the
# input is [[1, 2, 3], [4], [5, 6]], the output should
# be [[1, 4, 5], [1, 4, 6], [2, 4, 5], [2, 4, 6], [3, 4, 5], [3, 4, 6]]

def permut(lsts, prefix = []):
    if not lsts:
        print prefix
        return
    first = lsts[0]
    rest = lsts[1:]
    # key strategy here
    for letter in first:
        prefix.append(letter)
        permut(rest, prefix)
        prefix.pop()
        # pop here for the lst case


# permute for list of strings case: l = [['a', 'b', 'c'], ['a', 'b'], ['g', 'h', 'r', 'w']]

def permuteLetters(lsts, prefix =""):
    if not lsts:
        print prefix
        return
    first = lsts[0]
    rest = lsts[1:]
    for letter in first:
        permut(rest, prefix+letter)


if __name__ == "__main__":
    lst = [[1, 2, 3], [4], [5, 6]]
    prefix = []
    permut(lst, prefix)

    lst2 = [['a', 'b', 'c'], ['a', 'b'], ['g', 'h', 'r', 'w']]
    permuteLetters(lst2)
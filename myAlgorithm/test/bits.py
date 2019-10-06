class Bits:
    def update_bits(self, n, m, i, j):
        max1 = ~0
        left = max1 - ((1 << j)-1)
        right = ((1 << i) - 1)
        mask = left | right
        return (n & mask) | (m << i)


    def getDiff(self, val1, val2):
        c = val1 ^ val2
        count = 0
        while c:
            count += c & 1
            c >>= 1
        return count

if __name__ == "__main__":
    test = Bits()
    n, m, i, j = 10000000000, 10101, 2, 6
    print test.update_bits(n, m, i, j)
    print test.getDiff(31, 14)
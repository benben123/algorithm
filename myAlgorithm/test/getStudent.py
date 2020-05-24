"""
200 students sit around, count number from 1 to 3. Student who count 3 will stop counting.
The last student left should be with which number?
"""

def getNumber(N):
    people = [0]*N
    outNum, calNum, i = 0, 0, 0
    modVal = N
    while 1:
        if N - outNum == 1:
            break
        elif people[i] == 0:
            calNum += 1
            if calNum % 3 == 0:
                people[i] = 1
                outNum += 1
                calNum = 0
        i += 1
        i = i%N # very good point here, making people as a loop
    return i+1

if __name__ == "__main__":
    N = 200
    print getNumber(N)

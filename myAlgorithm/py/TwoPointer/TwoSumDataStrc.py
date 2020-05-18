class TwoSum:
    def __init__(self):
        self.store =[]

    def add(self, val):
        self.store.append(val)
        print self.store

    def isInStore(self, val):
        checked = []
        for ele in self.store:
            if val - ele in checked:
                return True
            else:
                checked.append(ele)
        return False

if __name__=="__main__":
    test = TwoSum()
    test.add(1)
    test.add(4)
    test.add(2)
    test.add(6)
    print test.isInStore(6)
    print test.isInStore(9)
    test.add(5)
    print test.isInStore(9)
class Hanoi:
    def __init__(self, size):
        self.towers = [[], [], []]
        self.size = size
        self.towers[0] = [x for x in range(size, 0, -1)]

    def moveDisk(self, size, fr, help, to):
        if size ==1:
            data = self.towers[fr-1].pop()
            self.towers[to-1].append(data)
            print 'data', data, 'from tower', fr, '->', to
        else:
            self.moveDisk(size-1, fr, to, help)
            self.moveDisk(1, fr, help, to)
            self.moveDisk(size-1, help, fr, to)

    def printDisk(self):
        for i in self.towers:
            print i

    def runHanoi(self):
        self.printDisk()
        self.moveDisk(self.size, 1, 2, 3)
        self.printDisk()

if __name__ == "__main__":
    Hanoi(4).runHanoi()



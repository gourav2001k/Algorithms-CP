# https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot:

    def __init__(self, width: int, height: int):
        self.n = width-1
        self.m = height-1
        self.dir = 0
        self.moved = False
        self.x, self.y = 0, 0
        self.dirName = ["East", "North", "West", "South"]
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.boundary = [(0, 0), (self.n, 0), (self.n, self.m), (0, self.m)]

    def step(self, k: int) -> None:
        self.moved = True
        k %= 2*(self.n+self.m)
        while k:
            x = self.howMuchMore()
            s = min(x, k)
            self.x += self.dirs[self.dir][0]*s
            self.y += self.dirs[self.dir][1]*s
            k -= s
            if k:
                self.dir += 1
            self.dir %= 4
        if (self.x, self.y) in self.boundary:
            self.dir = (self.boundary.index((self.x, self.y))-1) % 4

    def howMuchMore(self):
        match self.dir:
            case 0: return self.n-self.x
            case 1: return self.m-self.y
            case 2: return self.x
            case 3: return self.y

    def getPos(self) -> List[int]:
        return self.x, self.y

    def getDir(self) -> str:
        return self.dirName[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

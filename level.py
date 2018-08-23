from background import *
from enemy import *
from board import *
from obstacles import *
from mario import *
from user import *
from hurdles import *
from coins import *
import colorama


class Level:
    '''Making of level'''
    def __init__(self,breadth,status):
        self.board = Board(LENGTH,breadth,status)
        self.status = status
        self.offset = 0
        self.breadth = breadth

        #Generate random background
        for i in range(randint(breadth//20,breadth//16)):
            cloud = Cloud(self.board)
        for i in range(randint(breadth//15,breadth//10)):
            bush = Bush(self.board)
        self.display()

        self.generateHurdles()
        self.display()

        self.mario = Mario(FLOOR - 3,3,self.board)
        self.display()
        while True:
            self.scheduler()

    def scheduler(self):
        self.mario.gravity(2)
        for i in USED_COINS:
            i.restore()
        for i in self.board.allEnemies:
            i.selfMove(1)
        self.moveScreen()
        self.userResponse()
        for i in COINS:
            i.check()
        self.display()

    def display(self):
        self.board.status.updateTime()
        self.board.display(self.offset)

    def moveScreen(self):
        if(self.mario.point.y - self.offset > 50):
            self.offset += 15
        if(self.mario.point.y - self.offset < 0):
            self.offset -= 15

    def userResponse(self):
        ch = getInput()
        if ch == 'a':
            self.mario.move_left(1)
        elif ch == 'd':
            self.mario.move_right(1)
        elif ch == 'q':
            quit()
        elif ch == 'w':
            self.mario.jump(6)

    def generateHurdles(self):
        hurdles = HURDLES
        options = len(hurdles)
        x = 25
        while( x < self.breadth):
            option = randint(0,options-1)
            if hurdles[option][0] + x < self.breadth:
                hurdles[option][1](x,self.board)
                x += hurdles[option][0]
                x += randint(10,20)
            else:
                break

if __name__ == '__main__':
    from status import *
    status = Status()
    level = Level(300,status)

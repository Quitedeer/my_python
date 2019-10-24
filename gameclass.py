class Cookie:
    def __init__(self,new_runner):
        self.name=new_runner
        self.x = 0
        self.y = 0
        self.inventory=[]
    def run(self,delta_x, delta_y):
        print(self.name," бежит.")
        if 'Boost jelly' in self.inventory:
            self.x = self.x + 2*delta_x
            self.y = self.y + 2*delta_y
        else:
            self.x = self.x + delta_x
            self.y = self.y + delta_y
    def shoot(self,xs,ys):
        self.xs=xs
        self.ys=ys
        print(self.name," начинает стрелять в точку:", self.xs,",",self.ys)
    def pickup(self,chto):
        print(self.name," подбирает предмет: ",chto)
        self.inventory.append(chto)
    def whereami(self):
        print("Ваше местоположение:", self.x,",",self.y)
    def items(self):
        print("В вашем инвентаре:", self.inventory)
class Legendary_Cookie(Cookie):
    def fly(self,delta_x, delta_y):
        if 'Boost jelly' in self.inventory:
            print(self.name," быстро летит из-за Boost jelly.")
            self.x = self.x + 2*delta_x
            self.y = self.y + 2*delta_y
        else:
            print(self.name," летит.")
            self.x = self.x + delta_x
            self.y = self.y + delta_y

class Game:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y

new_runner=Legendary_Cookie("Moonlight Cookie")
new_runner.fly(4,8)
new_runner.pickup("Boost jelly")
new_runner.run(5,4)
new_runner.shoot(10,8)
new_runner.whereami()
new_runner.items()


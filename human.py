class Human:
    def __init__(self,person='Родился новый человек. Дайте ему имя'):
        self.mame=person
        print(self.mame," пришел в эту бренную циклическую жизнь.")
    def eating(self):
        print(self.mame," ест")
   
    def sleeping(self):
        print(self.mame," спит")

    def working(self):
        print(self.mame," работает")

    def step_back(self):
        print(self.mame," на пенсии")

    def relaxing(self):
        print(self.mame," отдыхает")

    def growing(self):
        print(self.mame," на год ближе к смерти")


class Life:
    def life(self, human, years=70):
        while years:            
            human.growing()
            human.eating()
            human.sleeping()
            if 53>=years and years>5:
                human.working()
            if 5>=years:
                human.step_back()
            human.relaxing()   
            years -= 1
        return(print("Вот и закончилась бренная циклическая жизнь..."))
        
person = Human('Подопытный кролик')
life_person = Life()
life_person.life(person)

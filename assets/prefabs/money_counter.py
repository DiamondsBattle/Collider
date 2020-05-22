from ursina import *


class MoneyCounter(Text):

    def __init__(self, money, **kwargs):
        super().__init__(**kwargs)
        self.money = money
        self.text = (str(self.money) + '$')

    def getMoneyAmount(self):
        return self.money

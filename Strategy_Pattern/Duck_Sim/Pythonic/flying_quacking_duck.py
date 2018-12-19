""" This approach suffers from class explosion """
from duck import Duck, NoFly, NoSound


class FlyWithWings(NoFly):
    def fly(self):
        return "Flying with wings"


class WingedFlyingDuck(Duck, FlyWithWings):
    pass


class FlyWithRocket(NoFly):
    def fly(self):
        return "Flying with rocket"


class RocketFlyingDuck(Duck, FlyWithRocket):
    pass


class QuackingDuck(NoSound):
    def make_sound(self):
        return "Quack Quack"


class QuackingWingedDuck(WingedFlyingDuck, QuackingDuck):
    pass


if __name__ == '__main__':
    d = WingedFlyingDuck(name="Nemopy")
    d.fly()

    # print(help(d))

    d = RocketFlyingDuck(name="Nemopy")
    d.fly()

    # print(help(d))
    print("\n#", "-" * 20, "#\n")
    d = QuackingWingedDuck(name="Nemopy")
    d.make_sound()

    d = QuackingWingedDuck(name="Nemopy")
    d.make_sound()

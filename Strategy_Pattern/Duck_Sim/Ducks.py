from FlyingBehaviours import nofly, wingfly, rocketfly
from Quack_Behaviours import quack, squeak, nosound


class Duck(object):
    def __init__(self, name="Duck", flyingbehaviour=None,
                 quackingbehaviour=None):
        self.name = name
        self.flyingbehaviour = flyingbehaviour
        self.quackingbehaviour = quackingbehaviour

    def fly(self):
        return print(self.name, "-", self.flyingbehaviour(self))

    def make_sound(self):
        return print(self.name, "-", self.quackingbehaviour(self))


if __name__ == '__main__':
    d = Duck("Nemo", nofly, nosound)
    d.fly()
    print(f"\nAdding wings to {d.name}...")
    d.flyingbehaviour = wingfly
    d.fly()
    print(f"\nAdding rocket to {d.name}...")
    d.flyingbehaviour = rocketfly
    d.fly()
    # --------------------------------------
    print('\n#', '-' * 20, '#')
    print(f'\nTesting No Sound')
    d.make_sound()
    print(f'\nQuacking duck,')
    d.quackingbehaviour = quack
    d.make_sound()
    print(f'\nSqueaking duck,')
    d.quackingbehaviour = squeak
    d.make_sound()

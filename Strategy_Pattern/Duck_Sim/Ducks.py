from FlyingBehaviours import NoFly, WingFly, RocketFly


class Duck(object):
    def __init__(self, name="Duck", flyingbehaviour=None):
        self.name = name
        self.flyingbehaviour = flyingbehaviour

    def fly(self):
        return print(self.name, "-", self.flyingbehaviour.fly())


if __name__ == '__main__':
    d = Duck("Nemo", NoFly())
    d.fly()
    print(f"\nAdding wings to {d.name}...")
    d.flyingbehaviour = WingFly()
    d.fly()
    print(f"\nAdding rocket to {d.name}...")
    d.flyingbehaviour = RocketFly()
    d.fly()

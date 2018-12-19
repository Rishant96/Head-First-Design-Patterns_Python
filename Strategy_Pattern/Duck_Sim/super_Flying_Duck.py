from super_Duck import NoFly, Duck


class FlyWithWings(NoFly):
    def fly(self):
        return "Flying with wings"


class FlyingDuck(Duck, FlyWithWings):
    pass


if __name__ == '__main__':
    d = FlyingDuck()
    d.fly()

    print(help(d))
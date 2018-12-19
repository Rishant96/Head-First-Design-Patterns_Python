class NoFly:
    def fly(self):
        return "Cannot fly"


class Duck(NoFly):
    def fly(self, name="Duck"):
        return print(" ".join((name, '-', super().fly())))


if __name__ == '__main__':
    d = Duck()
    d.fly()

    print(help(d))

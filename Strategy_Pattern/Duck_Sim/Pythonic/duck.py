class NoFly:
    def fly(self):
        return "Cannot fly"


class NoSound:
    def make_sound(self):
        return "..."


class Duck(NoFly, NoSound):
    def __init__(self, name="Duck"):
        self.name = name

    def fly(self):
        return print(" ".join((self.name, '-', super().fly())))

    def make_sound(self):
        return print(" ".join((self.name, '-', super().make_sound())))


if __name__ == '__main__':
    d = Duck(name="Nemopy")
    d.fly()
    d.make_sound()
    # print(help(d))

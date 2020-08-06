class Worker(object):
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    def get_income(self):
        return self.__income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name=name, surname=surname, position=position, income=income)

    def get_full_name(self):
        return "{} {}".format(self.name, self.surname)

    def get_total_income(self):
        income = self.get_income()
        return income["wage"] + income["bonus"]


position = Position(name="Andrey", surname="Livintsev", position="Software engineer",
                    income={"wage": 100, "bonus": 999})

print(position.get_full_name())
print(position.get_total_income())

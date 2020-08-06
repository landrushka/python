class Car(object):
    def __init__(self, speed, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self, direction):
        pass

    def show_speed(self):
        message = "Current speed is {speed}. {warn} \n"
        print(message.format(speed=self.speed, warn=""))

    def __repr__(self):
        return "Name: {name}\n" \
               "Color: {color}\n" \
               "Speed: {speed}".format(name=self.name, color=self.color, speed=self.speed)


class TownCar(Car):
    def show_speed(self):
        message = "Current speed is {speed}. {warn}"
        if self.speed > 60:
            warn_message = "WARN! Speed limit exceeded."
        else:
            warn_message = ""
        print(message.format(speed=self.speed, warn=warn_message))


class SportCar(Car):
    ...


class WorkCar(Car):
    def show_speed(self):
        message = "Current speed is {speed}. {warn}"
        if self.speed > 40:
            warn_message = "WARN! Speed limit exceeded."
        else:
            warn_message = ""
        print(message.format(speed=self.speed, warn=warn_message))


class PoliceCar(Car):
    ...


police_car = PoliceCar(speed=100, name="police", color="blue", is_police=True)
print(police_car)
police_car.show_speed()

work_car = WorkCar(speed=99, name="work", color="red")
print(work_car)
work_car.show_speed()

town_car = TownCar(speed=90, name="work", color="red")
print(town_car)
town_car.show_speed()

sport_car = SportCar(speed=999, name="sport", color="white")
print(sport_car)
sport_car.show_speed()

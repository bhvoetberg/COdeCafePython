from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):

    def turn_on(self):
        print("Light turned on")

    def turn_off(self):
        print("Light turned off")


class Fan(Switchable):

    def turn_on(self):
        print("Fan turned on")

    def turn_off(self):
        print("Fan turned off")


class Laptop(Switchable):

    def turn_on(self):
        print("LT turned on")

    def turn_off(self):
        print("LT turned off")


class ElectricPowerSwitch:
    def __init__(self, sd: Switchable):
        self.switchabledevice = sd
        self.on = False

    def press(self):
        if self.on:
            self.switchabledevice.turn_off()
            self.on = False
        else:
            self.switchabledevice.turn_on()
            self.on = True


lampie = LightBulb()
fanny = Fan()
lt = Laptop()
switch = ElectricPowerSwitch(lt)
switch.press()
switch.press()
switch.press()
switch.press()

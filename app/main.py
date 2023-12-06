from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def display(self):
        pass


class DellLaptop(Device):
    def display(self):
        return "Dell Laptop"


class SamsungPhone(Device):
    def display(self):
        return "Samsung Phone"


class DeviceFactory(ABC):
    @abstractmethod
    def create_product(self):
        pass


class DellLaptopFactory(DeviceFactory):
    def create_product(self):
        return DellLaptop()


class SamsungPhoneFactory(DeviceFactory):
    def create_product(self):
        return SamsungPhone()


if __name__ == "__main__":
    dell_factory = DellLaptopFactory()
    samsung_factory = SamsungPhoneFactory()

    print(dell_factory.create_product().display())
    print(samsung_factory.create_product().display())

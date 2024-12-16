class PowerSupply:
    def __init__(self, power):
        self.power = power

    def supply_voltage(self):
        print(f"Подали напряжение с мощностью {self.power} Вт")

class Motherboard:
    def __init__(self, chipset):
        self.chipset = chipset

    def distribute_voltage(self):
        print(f"Перераспределяем напряжение по компонентам с чипсетом {self.chipset}")

class CPU:
    def __init__(self, clock_speed, cores):
        self.clock_speed = clock_speed
        self.cores = cores

    def activate_turbo_mode(self):
        print(f"Активация турбо режима для CPU с тактовой частотой {self.clock_speed} ГГц и {self.cores} ядрами")

class RAM:
    def __init__(self, capacity, frequency):
        self.capacity = capacity
        self.frequency = frequency

    def load_data(self):
        print(f"Загружаем данные в RAM объемом {self.capacity} ГБ с частотой {self.frequency} МГц")

    def unload_data(self):
        print("Выгружаем данные из RAM")

class SSD:
    def __init__(self, capacity):
        self.capacity = capacity

    def save_data(self):
        print(f"Сохраняем данные на SSD объемом {self.capacity} ГБ")

    def delete_data(self):
        print("Удаляем данные с SSD")

class GPU:
    def __init__(self, model, memory):
        self.model = model
        self.memory = memory

    def display_image(self):
        print(f"Выводим изображение на экран с видеокартой модели {self.model} и объемом {self.memory} ГБ")

class Computer:
    def __init__(self, power_supply, motherboard, cpu, ram, ssd, gpu):
        self.power_supply = power_supply
        self.motherboard = motherboard
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
        self.gpu = gpu

    def assemble(self):
        print("Сборка компьютера:")
        self.power_supply.supply_voltage()
        self.motherboard.distribute_voltage()
        self.cpu.activate_turbo_mode()
        self.ram.load_data()
        self.ssd.save_data()
        self.gpu.display_image()

if __name__ == "__main__":
    power_supply = PowerSupply(750)
    motherboard = Motherboard("X570")
    cpu = CPU(4.5, 8)
    ram = RAM(32, 3200)
    ssd = SSD(1024)
    gpu = GPU("NVIDIA RTX 3070Ti" ,12)

    computer = Computer(power_supply, motherboard, cpu, ram, ssd, gpu)
    computer.assemble()

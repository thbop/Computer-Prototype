import pygame

from g_memory import GMemory
from cpu import CPU

class Computer:
    def __init__(self):
        
        pygame.init()

        pygame.display.set_mode()


        self.mem = GMemory(4, 16)

        self.vmem = GMemory(4, 256)

        self.cpu = CPU(self)
        self.cpu.load_program('program1.bin')

    
    def run(self):
        self.cpu.run()
        print(self.cpu.reg)
        # print(self.mem)

if __name__ == '__main__':
    computer = Computer()
    computer.run()
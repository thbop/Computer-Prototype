import pygame

from g_memory import GMemory
from cpu import CPU

class Computer:
    def __init__(self):
        
        # Pygame stuff
        pygame.init()

        self.window = pygame.display.set_mode((240, 240))
        pygame.display.set_caption('Computer')
        self.screen = pygame.Surface((16, 16))

        # Computer stuff
        self.mem = GMemory(4, 16)

        self.vmem = GMemory(4, 256)

        self.cpu = CPU(self)
        self.cpu.load_program('test.bin')

        self.halt = False
    
    def draw_pixel(self, x, y, color):
        fcolor = []
        for b in color:
            if b == '1':
                fcolor.append(255)
            else:
                fcolor.append(0)
        
        pygame.draw.rect(self.screen, fcolor, [x, y, 1, 1])
    
    def update_display(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.halt = True
        
        self.screen.fill((0, 0, 0))

        for x in range(16):
            for y in range(16):
                color = self.vmem.read(bin(x + y * 16))
                color = color.replace('0b', '')
                if color != '0000':
                    self.draw_pixel(x, y, color)

        self.window.blit(pygame.transform.scale(self.screen, (240, 240)), (0, 0))
        pygame.display.flip()
        # We aren't putting a clock here, sorry

    
    def run(self):
        self.cpu.run()
        print(self.cpu.reg)
        # print(self.mem)

if __name__ == '__main__':
    computer = Computer()
    computer.run()
from g_memory import GMemory

class ALU:
    def __init__(self):
        self.last = '0b0'
        self.bit_size = 4

    def bin2(self, i, bitsize):
        b = bin(i).replace('0b', '')
        if bitsize - len(b) > 0:
            b = '0' * (bitsize - len(b)) + b
        return b

    def add(self, a, b):
        intsum = int(a, 2) + int(b, 2)
        if intsum > self.bit_size**2 - 1:
            v = '1111'
        else:
            v = self.bin2(
                int(a, 2) + int(b, 2),
                self.bit_size
            )
        
        self.last = v
        return v
    def sub(self, a, b):
        intsub = int(a, 2) + int(b, 2)
        if intsub < 0:
            v = '0000'
        else:
            v = self.bin2(
                int(a, 2) - int(b, 2),
                self.bit_size
            )
        self.last = v
        return v

class CPU:
    def __init__(self, c):
        self.c = c
        self.alu = ALU()

        self.program = GMemory(16, 4095)

        self.reg = GMemory(4, 8)

        self.line = '0b000000000000'
    
    def load_program(self, program):
        file = open('programs/' + program)

        for i, line in enumerate(file.read().splitlines(), 0):
            self.program.write(bin(i), line)
            
        
        file.close()
    
    def tick(self):
        self.line = bin(
            int(self.line, 2) + 1
        )
    
    def parse_ins(self, ins):
        ins = ins.replace('0b', '')
        return [ins[i:i+4] for i in range(0, len(ins), 4)] # New Bing's code because I didn't want to figure it out.
    
    def run(self):
        running = True
        while running:
            ins = self.parse_ins(self.program.read(self.line))
            doTick = True
            # print(ins)
            # print(self.alu.last)
            # print(self.line)

            if ins[0] == '0000': # ld
                self.reg.write(
                    ins[2],
                    self.c.mem.read(ins[1])
                )
            elif ins[0] == '0001': # set
                self.reg.write(ins[1], ins[2])

            elif ins[0] == '0010': # wrt
                self.c.mem.write(ins[1], self.reg.read(ins[2]))

            
            elif ins[0] == '0011': # add
                a = self.reg.read(ins[1])
                b = self.reg.read(ins[2])
                self.reg.write(ins[3], self.alu.add(a, b))
            
            elif ins[0] == '0100': # sub
                a = self.reg.read(ins[1])
                b = self.reg.read(ins[2])
                self.reg.write(ins[3], self.alu.sub(a, b))
            

            elif ins[0] == '0101': # jmp
                doTick = False
                self.line = ins[1] + ins[2] + ins[3]
            
            elif ins[0] == '0110': # biz
                if int(self.alu.last, 2) == 0:
                    doTick = False
                    self.line = ins[1] + ins[2] + ins[3]

            elif ins[0] == '1110': # dis
                pos = int(self.reg.read(ins[1]), 2) + int(self.reg.read(ins[2]), 2) * 16 # This is not cheating because in reality I would store the video memory as a "2d array"
                self.c.vmem.write(
                    bin(pos), self.reg.read(ins[3])
                )

            if ins[0] == '1111' or self.c.halt: # end
                doTick = False
                self.line = '0b00000000'
                print('Terminated')
                running = False

            if doTick:
                self.tick()
            
            self.c.update_display()
            



if __name__ == '__main__':
    cpu = CPU(None)
    print(cpu.parse_ins('0b00010010'))
    
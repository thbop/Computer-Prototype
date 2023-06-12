from assembler import assemble

class Program:
    def __init__(self):
        self.vars = [] # {'id':'a', 'adr':'00000000'}
        self.current_adr = 0
    
    def bin2(self, i, bit):
        b = bin(i).replace('0b', '')
        if bit - len(b) > 0:
            b = '0' * (bit - len(b)) + b
        return b
    
    def defvar(self, i, adr):
        dup = False
        for c, v in enumerate(self.vars, 0):
            if v['id'] == i: dup = True
        if not dup:
            self.vars.append({'id':i, 'adr':adr})
            self.current_adr += 1


    def compile(self, filename):
        file = open('programs/' + filename + '.t')
        lines = file.read().splitlines()
        file.close()

        out = ''

        for i, l in enumerate(lines, 0):
            line = l.split(' ')
            
            if line[0] == 'var':
                adr = self.bin2(self.current_adr, 8)
                self.defvar(line[1], adr)
                out += f'''set A {self.bin2(int(line[2]), 4)}
wrt {adr[:4]} {adr[4:]} A
'''
        
        out += 'end'
        file = open('programs/' + filename + '.a', 'w')
        file.write(out)
        file.close()
        assemble(filename)

if __name__ == '__main__':
    program = Program()
    program.compile('test')
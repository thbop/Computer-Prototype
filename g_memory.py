
class GMemory:
    def __init__(self, bit, size):
        self.bit = bit
        self.size = size
        self._memory = ['0b'+'0'*bit for i in range(size)]
    
    def format_e(self, adr, data):
        adr = adr.replace('0b', '')
        data = data.replace('0b', '')
        if int(adr, 2) > self.size - 1:
            raise ValueError('Address not found! Too large.')
        if len(data) > self.bit:
            raise ValueError(f'Data string must be {self.bit}-bit! Not {len(data)}-bit!')
        return adr, data
        

    def write(self, adr, data):
        adr, data = self.format_e(adr, data)
        
        self._memory[int(adr, 2)] = data
    
    def clear(self, adr):
        self.write(adr, '0'*self.bit)
    
    def read(self, adr):
        adr = self.format_e(adr, '0')[0]
        return self._memory[int(adr, 2)]
    
    
    def __repr__(self):
        v = ''
        for a, b in enumerate(self._memory, 0):
            v += f'{bin(a)} {a} {b} \n'
        return v

if __name__ == '__main__':
    m = GMemory(8, 256)
    
    m.write('0b0', '0b00000101')
    print(m.read('0b00000000'))

    # print(m)
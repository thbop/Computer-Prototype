def assemble(filename):
    file = open('programs/' + filename + '.a')
    lines = file.read().splitlines()
    file.close()

    out = ''

    def bin2(i):
        b = bin(i).replace('0b', '')
        if 4 - len(b) > 0:
            b = '0' * (4 - len(b)) + b
        return b

    def reg_calc(i):
        alphabet = 'ABCDEFGH'
        reg = alphabet.find(i)
        if reg == -1:
            raise ValueError('Invalid register!')
        
        return bin2(reg)

    for l in lines:
        if l != '':
            args = l.split(' ')
            
            if args[0] == 'ld':
                out += '0000' + args[1] + args[2] + reg_calc(args[3]) + '\n'
            
            elif args[0] == 'set':
                out += '0001' + reg_calc(args[1]) + args[2] + '0000' + '\n'
            
            elif args[0] == 'wrt':
                out += '0010' + args[1] + args[2] + reg_calc(args[3]) + '\n'


            elif args[0] == 'add':
                out += '0011' + reg_calc(args[1]) + reg_calc(args[2]) + reg_calc(args[3]) + '\n'
            
            elif args[0] == 'sub':
                out += '0100' + reg_calc(args[1]) + reg_calc(args[2]) + reg_calc(args[3]) + '\n'

            
            elif args[0] == 'jmp':
                out += '0101' + args[1] + args[2] + args[3] + '\n'

            elif args[0] == 'biz':
                out += '0110' + args[1] + args[2] + args[3] + '\n'


            elif args[0] == 'dis':
                out += '1110' + reg_calc(args[1]) + reg_calc(args[2]) + reg_calc(args[3]) + '\n'

            elif args[0] == 'end':
                out += '1111' + '000000000000'


    # print(out)

    file = open('programs/' + filename + '.bin', 'w')
    file.write(out)
    file.close()

if __name__ == '__main__':
    assemble('test')
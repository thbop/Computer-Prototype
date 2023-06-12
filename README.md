# Computer-Prototype
 A little computer prototype simulating basic hardware

## Cheatsheet
* 0000 ld mem mem reg - loads data from memory into register via addresses
* 0001 set reg val nul - sets reg data as a value
* 0010 wrt mem mem reg - writes data to memory from registers via addresses

* 0011 add reg reg reg - adds data in register A plus data in register B and stores the result in register C
* 0100 sub reg reg reg - subtracts data in register A minus data in register B and stores the result in register C

* 0101 jmp lin lin lin - jumps to the specified line (combines all the line arguments)
* 0110 biz lin lin lin - braches/jumps to the specified line if the last ALU operation resulted in a zero (combines all the line arguments)

* 1110 dis reg reg reg - displays a pixel at the x location stored in register A; the y stored in register B; and the color stored in register C (rgba)
* 1111 end nul nul nul - halts the program
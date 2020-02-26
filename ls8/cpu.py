"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""

        self.running = True #Is CPU Live?

        #General Purpose Registers
        self.reg = [0] * 8 #General Registers
        self.reg[7] = 0xf4 #Register[7] set to 0xF4
        self.memory = [0] * 256 #256 Bytes of RAM
        #Special Purpose Registers
        self.IR = 0 #Instruction Register, contains a copy of the instruction currently being executed
        self.PC = 0 #Program Counter, address of the currently executing instruction
        self.MAR = 0 #Memory Address Register, holds the memory address we're reading or writing
        self.MDR = 0 #Memory Data Register, holds the value to write or the value just read


        self.SP = 7
      
        
        
    def ram_read(self, MAR):
        return self.memory[MAR]

    def ram_write(self, MAR, MDR):
        self.memory[MAR] = MDR

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        with open(sys.argv[1]) as f:
            for line in f:
                if line[0] != '#' and line != '\n':
                    self.memory[address] = int(line[0:8], 2)
                    address += 1
                f.closed
            print(self.memory)

            

        for instruction in program:
            self.memory[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]
        elif op == "DEC":
            self.reg[reg_a] -= 1
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == "DIV":
            if self.reg[reg_b] == 0:
                print("Error, Cannot divide by 0")
            else:
                 self.reg[reg_a] = self.reg[reg_a] / self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.PC,
            #self.fl,
            #self.ie,
            self.ram_read(self.PC),
            self.ram_read(self.PC + 1),
            self.ram_read(self.PC + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True

        while self.running:
            opp_a = self.ram_read(self.PC + 1)
            opp_b = self.ram_read(self.PC + 2)
            if self.memory[self.PC] == HLT:
                self.running == False
                break

            elif self.memory[self.PC] == ADD:
                self.alu("ADD", opp_a)

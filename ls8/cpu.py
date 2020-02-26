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
        self.ram = [0] * 256 #256 Bytes of RAM
        #Special Purpose Registers
        #self.IR = 0 #Instruction Register, contains a copy of the instruction currently being executed
        self.PC = 0 #Program Counter, address of the currently executing instruction
        self.MAR = 0 #Memory Address Register, holds the memory address we're reading or writing
        self.MDR = 0 #Memory Data Register, holds the value to write or the value just read
        self.SP = 7
      
        self.cmds = {
          0b00000001: self.hlt,
          0b10000010: self.ldi,
          0b01000111: self.prn
      }
        
        
    def ram_read(self, MAR):
        # print("\n------------------------")
        # print(f"ram_read()")
        # print(f"self.ram[{MAR}]: ", self.ram[MAR])
        # print("------------------------\n")
        
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    def hlt(self, opp_a, opp_b):
        return(0, False)

    def ldi(self, opp_a, opp_b):
        print(f"ldi(self, opp_a, opp_b): ldi({self}, {opp_a}, {opp_b})")
        print("Virgin self.reg: ", self.reg)
        self.reg[opp_a] = opp_b
        print("Self.reg: ", self.reg)
        return (3, True)

    def prn(self, opp_a, opp_b):
        print(f"prn(self, opp_a, opp_b): prn({opp_a}, {opp_b}")
        print("Result: ", self.reg[opp_a])
        return (2, True)



    def load(self, program):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        # programx = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        with open(program) as f:
            print("\n------------------------")
            print("load() \n")
            for line in f:
                #Clean comments out and strip the commands of trailing spaces
                prepped = line.split("#") 
                number = prepped[0].strip()

                print(f"Number: {number}")
                try:
                    self.ram[address] = int(number[0:8], 2)
                    address += 1
                except ValueError:
                    print(f"Value Error: {ValueError}")
                    pass
            print("\n------------------------")
        #         if line[0] != '#' and line != '\n':
        #             self.ram[address] = int(line[0:8], 2)
        #             address += 1
        #         f.closed
        #     print(self.ram)
            

        # for instruction in programx:
        #     self.ram[address] = instruction
        #     address += 1

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
        
        print("trace() \n")
        print("self.PC | self.PC, self.PC + 1, self.PC + 2 |")
        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.PC,
            #self.fl,
            #self.ie,
            self.ram_read(self.PC),
            self.ram_read(self.PC + 1),
            self.ram_read(self.PC + 2)
        ), end='')

        print("\n------------------------")
        
        print("self.reg[i] in range(8)")
        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print("\n------------------------")

        print()

    def run(self):
        """Run the CPU."""
        running = True
        print("\n------------------------")
        print("run() \n")
        self.trace()
        print(f"Program Counter: {self.PC}")
        self.PC = 0
        while running:
            IR = self.ram_read(self.PC) #Set Instruction Register
            print("IR: ", IR)
            print(f"self.pc: {self.PC}")
            print(f"Self.ram: {self.ram}")

            opp_a = self.ram_read(self.PC + 1)
            opp_b = self.ram_read(self.PC + 2)
            
            try:
                op= self.cmds[IR](opp_a, opp_b)
                running = op[1]
                print("Running: ",  running)
                self.PC += op[0]
                print("TRY self.pc: ", self.PC)
                print("TRY operation: ", op)

            except:
                print(f"Error: IR {IR} not available")
                sys.exit(1)
            # if self.ram[self.PC] == HLT:
            #     self.running == False
            #     break

            # elif self.ram[self.PC] == ADD:
            #     self.alu("ADD", opp_a)

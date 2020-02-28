"""CPU functionality."""

import sys

#ALU OPCODES
ADD  = 0b10100000
SUB  = 0b10100001
MUL  = 0b10100010
DIV  = 0b10100011
MOD  = 0b10100100

INC  = 0b01100101
DEC  = 0b01100110

CMP  = 0b10100111

AND  = 0b10101000
NOT  = 0b01101001
OR   = 0b10101010
XOR  = 0b10101011
SHL  = 0b10101100
SHR  = 0b10101101

#PC MUTATOR OPCODES
CALL = 0b01010000
RET  = 0b00010001

INT  = 0b01010010
IRET = 0b00010011

JMP  = 0b01010100
JEQ  = 0b01010101
JNE  = 0b01010110
JGT  = 0b01010111
JLT  = 0b01011000
JLE  = 0b01011001
JGE  = 0b01011010

#OTHER OPCODES
NOP  = 0b00000000

HLT  = 0b00000001

LDI  = 0b10000010

LD   = 0b10000011
ST   = 0b10000100

PUSH = 0b01000101
POP  = 0b01000110

PRN  = 0b01000111
PRA  = 0b01001000

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
        self.SP = 0xF4
        self.FL = 0 #Flag
        self.E = 0
        self.L = 0
        self.G = 0

        self.branch_table = {
          HLT: self.HLT,
          PRN: self.PRN,
          LDI: self.LDI,

          ADD: self.ADD,
          SUB: self.SUB,
          MUL: self.MUL,
          DIV: self.DIV,
          MOD: self.MOD,

          INC: self.INC,
          DEC: self.DEC,

          CMP: self.CMP,

          AND: self.AND,
          NOT: self.NOT,
          OR: self.OR,
          XOR: self.XOR,
          SHL: self.SHL,
          SHR: self.SHR,
        
          PUSH: self.PUSH,
          POP: self.POP
      }
        
        
    def ram_read(self, MAR):
        #print("\n-------------------------")
        #print(f"ram_read()")
        #print(f"self.ram[MAR: {MAR}]: ",  self.ram[MAR])
        #print("-------------------------\n")
        
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR






    def HLT(self, opp_a, opp_b):
        print("-----------HLT-----------")
        return(0, False)


    def PRN(self, opp_a, opp_b):
        print("\n-----------PRINT--------------")
        print(f"PRN(opp_a, opp_b): PRN({opp_a}, {opp_b})")
        print("--------------------------------- \n")
        print("---------------------------------Result: ", self.reg[opp_a])
        print("--------------------------------- \n")

        return (2, True)

    def LDI(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"LDI(self, opp_a, opp_b): LDI({self}, {opp_a}, {opp_b})")
        #print("Virgin self.reg: ", self.reg)
        self.reg[opp_a] = opp_b
        #print("Self.reg: ", self.reg)
        return (3, True)



    
    
    def ADD(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"ADD(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("ADD", opp_a, opp_b)
        return(3, True)

    def SUB(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"SUB(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("SUB", opp_a, opp_b)
        return(3, True)
    
    def MUL(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"MUL(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("MUL", opp_a, opp_b)
        return(3, True)
        
    def DIV(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"DIV(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("DIV", opp_a, opp_b)
        return(3, True)

    def MOD(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"MOD(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("MOD", opp_a, opp_b)
        return(3, True)



    def INC(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"INC(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("INC", opp_a, opp_b)
        return(3, True)
        
    def DEC(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"DEC(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("DEC", opp_a, opp_b)
        return(3, True)


    

    def CMP(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"CMP(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("CMP", opp_a, opp_b)
        return(3, True)




    def AND(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"AND(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("AND", opp_a, opp_b)
        return(3, True)

    def NOT(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"NOT(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("NOT", opp_a, opp_b)
        return(2, True)


    def OR(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"OR(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("OR", opp_a, opp_b)
        return(3, True)


    def XOR(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"XOR(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("XOR", opp_a, opp_b)
        return(3, True)


    def SHL(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"SHL(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("SHL", opp_a, opp_b)
        return(3, True)

    def SHR(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"SHR(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        self.alu("SHR", opp_a, opp_b)
        return(3, True)



    def PUSH(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"PUSH(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        regIndex = self.ram[self.PC + 1]
        self.SP -= 1
        val = self.reg[regIndex]
        self.ram[self.SP] = val
        return (2, True)
        
    def POP(self, opp_a, opp_b):
        print("\n-------------------------")
        print(f"POP(self: {self}, opp_a: {opp_a}, opp_b: {opp_b})")
        popVal = self.ram[self.SP]
        regIndex = self.ram[self.PC + 1]
        self.reg[regIndex] = popVal
        self.SP += 1
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
            print("\n-------------------------")
            print("load() \n")
            print(f"Initial self.reg: {self.reg}")
            print(f"Initial self.ram: {self.ram}")
            for line in f:
                #Clean comments out and strip the commands of trailing spaces
                prepped = line.split("#") 
                number = prepped[0].strip()
                intNum = int(number[0:8], 2)

                print(f"Address: {address}, Number: {number}, intNum: {intNum} ")
                try:
                    self.ram[address] = int(number[0:8], 2)
                    address += 1
                except ValueError:
                    print(f"Value Error: {ValueError}")
                    pass
            print(f"self.reg: {self.reg}")
            print(f"ram after loading program data - self.ram: {self.ram}")


            print("\n-------------------------")
        #         if line[0] != '#' and line != '\n':
        #             self.ram[address] = int(line[0:8], 2)
        #             address += 1
        #         f.closed
        #     print(self.ram)
            

        # for instruction in programx:
        #     self.ram[address] = instruction
        #     address += 1

    def alu(self, op, reg_a, reg_b):

        """
        ALU operations
            Run computations using the numbers in the register, and set the result to be the new register value
                    
        """
        print("\n-------------------------")

        print(f"alu(op, reg_a, reg_b)")
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]

        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]

        elif op == "MUL":
            self.reg[reg_a] = (self.reg[reg_a] * self.reg[reg_b])

        elif op == "DIV":
            if self.reg[reg_b] == 0:
                print("Error, Cannot divide by 0")
            else:
                 self.reg[reg_a] = (self.reg[reg_a] / self.reg[reg_b])
        elif op == "MOD":
            self.reg[reg_a] = (self.reg[reg_a] % self.reg[reg_b])

        elif op == "INC":
            self.reg[reg_a] += 1

        elif op == "DEC":
            self.reg[reg_a] -= 1
            
        elif op == "AND":
            self.reg[reg_a] = self.reg[reg_a] & self.reg[reg_b]

        elif op == "NOT":
            self.reg[reg_a] = ~self.reg[reg_a]
            
        elif op == "OR":
            self.reg[reg_a] = self.reg[reg_a] | self.reg[reg_b]
            
        elif op == "XOR":
            self.reg[reg_a] = self.reg[reg_a] ^ self.reg[reg_b]

        elif op == "SHL":
            self.reg[reg_a] << self.reg[reg_b]
            
        elif op == "SHR":
            self.reg[reg_a] >> self.reg[reg_b]

        elif op == "CMP":
            if self.reg[reg_a] == self.reg[reg_b]:
                self.E = 1
                self.L = 0
                self.G = 0

            if self.reg[reg_a] <= self.reg[reg_b]:
                self.E = 0
                self.L = 1
                self.G = 0

            else:
                self.E = 0
                self.L = 0
                self.G = 1

        

        else:
            raise Exception("Unsupported ALU operation")

        print(f"alu({op}, {reg_a}, {reg_b}) | Result: {self.reg[reg_a]}")

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

        print("\n-------------------------")
        
        print("self.reg[i] in range(8)")
        for i in range(8):
            print(f"self.reg[i:{i}]:", self.reg[i],"| Hex Value: ", " %02X" % self.reg[i], end='\n')

        print("\n-------------------------")

        print()

    def run(self):
        """Run the CPU."""
        running = True
        # while True:
        #     command = self.ram[self.PC]
        #     opp_a = self.ram_read(self.PC + 1)
        #     opp_b = self.ram_read(self.PC + 2)

        #     self.branch_table[command](opp_a, opp_b)
        print("\n-------------------------")
        print("run() \n")
        #self.trace()
        print(f"Program Counter: {self.PC}")
        
        while running:
            IR = self.ram_read(self.PC) #Set Instruction Register
            #print(f"LSD:JFP:SDJF: ",  self.ram[self.PC])
            #print("IR: ", IR)
            #print(f"self.pc: {self.PC}")
            #print(f"Self.ram: {self.ram}")
            print(f"REGISTER: {self.reg}")

            opp_a = self.ram_read(self.PC + 1)
            opp_b = self.ram_read(self.PC + 2)
            
            try:
                op = self.branch_table[IR](opp_a, opp_b)
                running = op[1]
                #print("Running: ",  running)
                self.PC += op[0]
                print("PROGRAM COUNTER: ", self.PC)
                print(f"OPERATION: self.branch_table[IR: {IR}](opp_a: {opp_a}, opp_b: {opp_b}) ", op)

            except:
                print(f"Error: IR {IR} not available")
                sys.exit(1)
            # if self.ram[self.PC] == HLT:
            #     self.running == False
            #     break

            # elif self.ram[self.PC] == ADD:
            #     self.alu("ADD", opp_a)
        
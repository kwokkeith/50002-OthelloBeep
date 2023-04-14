########################################################################
### 50.002 BETA Macro package -                  revised 9/28/11 SAW  ###
###  This file defines our 32-bit Beta instruction set.              ###
########################################################################

# Global instruction definition conventions:
#  * DESTINATION arg is LAST

# Instruction set summary.  Notation:
# ra, rb, rc: registers
#         CC: 18-bit signed constant
#      label: statement/location tag (becomes PC-relative offset)

# ADD(RA, RB, RC)       # RC <- <RA> + <RB>
# ADDC(RA, C, RC)       # RC <- <RA> + C
# AND(RA, RB, RC)       # RC <- <RA> & <RB>
# ANDC(RA, C, RC)       # RC <- <RA> & C
# MUL(RA, RB, RC)       # RC <- <RA> * <RB>
# MULC(RA, C, RC)       # RC <- <RA> * C
# OR( RA, RB, RC)       # RC <- <RA> # <RB>
# ORC(RA,  C, RC)       # RC <- <RA> # C
# SHL(RA, RB, RC)       # RC <- <RA> << <RB>
# SHLC(RA, C, RC)       # RC <- <RA> << C
# SHR(RA, RB, RC)       # RC <- <RA> >> <RB>
# SHRC(RA, C, RC)       # RC <- <RA> >> C
# SRA(RA, RB, RC)       # RC <- <RA> >> <RB>
# SRAC(RA, C, RC)       # RC <- <RA> >> C
# SUB(RA, RB, RC)       # RC <- <RA> - <RB>
# SUBC(RA, C, RC)       # RC <- <RA> - C
# XOR(RA, RB, RC)       # RC <- <RA> ^ <RB>
# XORC(RA, C, RC)       # RC <- <RA> ^ C
# CMPEQ(RA, RB, RC)     # RC <- <RA> == <RB>
# CMPEQC(RA, C, RC)     # RC <- <RA> == C
# CMPLE(RA, RB, RC)     # RC <- <RA> <= <RB>
# CMPLEC(RA, C, RC)     # RC <- <RA> <= C
# CMPLT(RA, RB, RC)     # RC <- <RA> <  <RB>
# CMPLTC(RA, C, RC)     # RC <- <RA> <  C


# BR(LABEL,RC)          # RC <- <PC>+4; PC <- LABEL (PC-relative addressing)
# BR(LABEL)             # PC <- LABEL (PC-relative addressing)
# BEQ(RA, LABEL, RC)    # RC <- <PC>+4; IF <RA>==0 THEN PC <- LABEL
# BEQ(RA, LABEL)        # IF <RA>==0 THEN PC <- LABEL
# BF(RA, LABEL, RC)     # RC <- <PC>+4; IF <RA>==0 THEN PC <- LABEL
# BF(RA, LABEL)         # IF <RA>==0 THEN PC <- LABEL
# BNE(RA, LABEL, RC)    # RC <- <PC>+4; IF <RA>!=0 THEN PC <- LABEL
# BNE(RA, LABEL)        # IF <RA>!=0 THEN PC <- LABEL
# BT(RA, LABEL, RC)     # RC <- <PC>+4; IF <RA>!=0 THEN PC <- LABEL
# BT(RA, LABEL)         # IF <RA>!=0 THEN PC <- LABEL
# JMP(RA, RC)           # RC <- <PC>+4; PC <- <RA> & 0x40000
# JMP(RB)               # PC <- <RB> & 0xFFFC  <-- 0x40000 to make it word addressable

# INP(RC)               # RC <- <INPUT ROM>

# MOVE(RA, RC)          # RC <- <RA>
# CMOVE(CC, RC)         # RC <- CC
# HALT()                # STOPS SIMULATOR.

# WORD(val)             # Assemble val as a 16-bit datum
# LONG(val)             # Assemble val as a 32-bit datum
# VLONG(val)            # Assemble val as a 64-bit datum
# STORAGE(NWORDS)       # Reserve NWORDS 32-bit words of DRAM

# Extra register conventions, for procedure linkage:
# LP = 14                       # Linkage register (holds return adr)

########################################################################
### End of documentation.  Following are the actual definitions...   ###
########################################################################

# var storing current instruction address
dot = 0

# var storing output formatter func
output_func = bin
output_size = 2

# Instruction size in bits
instruction_width = 32
memory_width = 64

# register designators
# this allows symbols like r0, etc to be used as
# operands in instructions. Note that there is no real difference
# in this assembler between register operands and small integers.
r0 = 0
r1 = 1
r2 = 2
r3 = 3
r4 = 4
r5 = 5
r6 = 6
r7 = 7
r8 = 8
r9 = 9
r10 = 10
r11 = 11
r12 = 12
r13 = 13
r14 = 14
r15 = 15    # Always 0 register

# understand upper case, too.
R0 = r0
R1 = r1
R2 = r2
R3 = r3
R4 = r4
R5 = r5
R6 = r6
R7 = r7
R8 = r8
R9 = r9
R10 = r10
R11 = r11
R12 = r12
R13 = r13
R14 = r14
R15 = r15

# Trap and interrupt vectors
VEC_RESET = 0  # Reset (powerup)
VEC_CLK = 8  # Clock interrupt

def WORD(x):
    return [output_func((x % 0x100))[2:].zfill(output_size)] + [
        output_func((x >> 8) % 0x100)[2:].zfill(output_size)
    ]
    # return list(hex(((x % 0x100) << 8) + ((x >> 8) % 0x100))[2:].zfill(4))


def LONG(x):
    # Return 32-bit byte array (in hex)
    return WORD(x) + WORD(x >> 16)


def STORAGE(NWORDS):
    global dot
    dot += 4 * NWORDS


def betaop(OP, RA, RB, RC):
    align(4)
    # LONG() will convert to little-endian
    # If we want big-endian, return the arg instead
    return LONG(
        (OP << 26) + ((RC % 0x10) << 22) + ((RA % 0x10) << 18) + ((RB % 0x10) << 14)
    )


def betaopc(OP, RA, CC, RC):
    align(4)
    # LONG() will convert to little-endian
    # If we want big-endian, return the arg instead
    return LONG((OP << 26) + ((RC % 0x10) << 22) + ((RA % 0x10) << 18) + (CC % 0x40000))


def align(x=4):
    global dot
    dot = ((dot - 1) // x + 1) * x


ADD = lambda RA, RB, RC: betaop(0x20, RA, RB, RC)
ADDC = lambda RA, C, RC: betaopc(0x30, RA, C, RC)
AND = lambda RA, RB, RC: betaop(0x28, RA, RB, RC)
ANDC = lambda RA, C, RC: betaopc(0x38, RA, C, RC)
MUL = lambda RA, RB, RC: betaop(0x22, RA, RB, RC)
MULC = lambda RA, C, RC: betaopc(0x32, RA, C, RC)
OR = lambda RA, RB, RC: betaop(0x29, RA, RB, RC)
ORC = lambda RA, C, RC: betaopc(0x39, RA, C, RC)
SHL = lambda RA, RB, RC: betaop(0x2C, RA, RB, RC)
SHLC = lambda RA, C, RC: betaopc(0x3C, RA, C, RC)
SHR = lambda RA, RB, RC: betaop(0x2D, RA, RB, RC)
SHRC = lambda RA, C, RC: betaopc(0x3D, RA, C, RC)
SRA = lambda RA, RB, RC: betaop(0x2E, RA, RB, RC)
SRAC = lambda RA, C, RC: betaopc(0x3E, RA, C, RC)
SUB = lambda RA, RB, RC: betaop(0x21, RA, RB, RC)
SUBC = lambda RA, C, RC: betaopc(0x31, RA, C, RC)
XOR = lambda RA, RB, RC: betaop(0x2A, RA, RB, RC)
XORC = lambda RA, C, RC: betaopc(0x3A, RA, C, RC)
CMPEQ = lambda RA, RB, RC: betaop(0x24, RA, RB, RC)
CMPEQC = lambda RA, C, RC: betaopc(0x34, RA, C, RC)
CMPLE = lambda RA, RB, RC: betaop(0x26, RA, RB, RC)
CMPLEC = lambda RA, C, RC: betaopc(0x36, RA, C, RC)
CMPLT = lambda RA, RB, RC: betaop(0x25, RA, RB, RC)
CMPLTC = lambda RA, C, RC: betaopc(0x35, RA, C, RC)
INP = lambda RC: betaop(0x17, R15, R15, RC)

BETABR = lambda OP, RA, RC, LABEL: betaopc(OP, RA, ((LABEL - dot) >> 2) - 1, RC)

BEQ = lambda RA, LABEL, RC=15: BETABR(0x1D, RA, RC, LABEL) # 0x1D <-- OPCODE: Ob011101 (BEQ)
BF = lambda RA, LABEL, RC=15: BEQ(RA, LABEL, RC)
BNE = lambda RA, LABEL, RC=15: BETABR(0x1E, RA, RC, LABEL)
BT = lambda RA, LABEL, RC=15: BNE(RA, LABEL, RC)
BR = lambda LABEL, RC=15: BEQ(r15, LABEL, RC)
JMP = lambda RA, RC=15: betaopc(0x1B, RA, 0, RC)

MOVE = lambda RA, RC: ADD(RA, R15, RC)
CMOVE = lambda CC, RC: ADDC(R15, CC, RC)

PRIV_OP = lambda FNCODE: betaopc(0x00, 0, FNCODE, 0)
HALT = lambda: PRIV_OP(0)
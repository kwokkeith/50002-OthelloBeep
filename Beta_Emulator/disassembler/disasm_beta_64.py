# Each tuple stores number of bits to shift and width in bits of arg
# op = [(16, 5, False), (11, 5, False), (21, 5, False)]
# opc = [(16, 5, False), (0, 16, True), (21, 5, False)]
#op = [(11, 3, False), (15, 3, False), (7, 3, False)]
#opc = [(11, 3, False), (0, 15, True), (7, 3, False)]

op = [(18, 4, False), (14, 4, False), (22, 4, False)]
opc = [(18, 4, False), (0, 18, True), (22, 4, False)]

val_ops = {
    0x20: ("ADD", op),
    0x30: ("ADDC", opc),
    0x28: ("AND", op),
    0x38: ("ANDC", opc),
    0x22: ("MUL", op),
    0x32: ("MULC", opc),
    0x29: ("OR", op),
    0x39: ("ORC", opc),
    0x2C: ("SHL", op),
    0x3C: ("SHLC", opc),
    0x2D: ("SHR", op),
    0x3D: ("SHRC", opc),
    0x2E: ("SRA", op),
    0x3E: ("SRAC", opc),
    0x21: ("SUB", op),
    0x31: ("SUBC", opc),
    0x2A: ("XOR", op),
    0x3A: ("XORC", opc),
    0x2B: ("XNOR", op),
    0x3B: ("XNORC", opc),
    0x24: ("CMPEQ", op),
    0x34: ("CMPEQC", opc),
    0x26: ("CMPLE", op),
    0x36: ("CMPLEC", opc),
    0x25: ("CMPLT", op),
    0x35: ("CMPLTC", opc),
    0x17: ("INP", opc),
    0x1D: ("BEQ", [(18, 4, False), (0, 18, True), (22, 4, False)]),
    0x1E: ("BNE", [(18, 4, False), (0, 18, True), (22, 4, False)]),
    0x1B: ("JMP", [(18, 4, False), (22, 4, False)]),
    0x02: ("NOP", []),
    0x00: ("PRIV_OP", [(0, 18, True)])
}

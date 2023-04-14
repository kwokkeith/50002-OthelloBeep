import bitstring
from rich import print
from rich.syntax import Syntax
from rich.table import Table

from . import disasm_beta_64 as beta

# WARNING: PLEASE GENERATE HEXCODE OF ASSEMBLY INSTRUCTION NOT BINARY 
# IN ASSEMBLER FILE: DO python3 assembler_output.py -x ../uasm_files/game
# THIS BECAUSE THERE IS CURRENTLY NO CODE TO CONVERT FROM BINARY TO THE EMULATOR OUTPUT :>

def str_to_arr(data):
    """Convenience function to split a string on comma and remove whitespace"""
    return [i.strip() for i in data.split(",") if i.strip()]


def disassemble_instr(instr, split=False):
    """ # Sean: Example input -> 0x64640088 
    Takes integer value and returns the instruction that generated it
    """
    if not instr:
        return "HALT()" if not split else ["HALT", []]
    opcode = (instr >> 26).int
    if opcode in beta.val_ops:
        alias, args = beta.val_ops[opcode]
        parsed_args = []
        for shift, width, signed in args:
            # TODO: Convert literals back to labels for branching instructions 
            bits = bitstring.Bits( 
                # Sean: len(instr) == 32, after the conversion of the hexadecimal input into binary numbers
                bin=instr[len(instr) - shift - width : len(instr) - shift].bin 
                # Sean: .bin -> Property for representation of the bitstring as a binary string
            )   
            # Sean: .int -> property for the signed two's complement integer representation of the bitstring
            # Sean: .uint -> property for the unsigned base-2 integer representation of the binary string
            parsed_args.append(bits.int if signed else bits.uint)
        print(parsed_args)
        return (
            f"{alias}({', '.join([str(i) for i in parsed_args])})"
            if not split
            else [alias, parsed_args]
        )
    else:
        return "ILLOP()" if not split else ["ILLOP", []]


if __name__ == "__main__":
    with open("./uasm_files/game.hex", "r", encoding="utf8") as fp:
        data = str_to_arr(fp.read()) 
    print("DATA: " + data)
    table = Table()
    table.add_column("n")
    table.add_column("ASM")
    table.add_column("DISASM")

    disasm_instr = []

    # Iterate backwards since it was written backwards
    for i, instr in enumerate(data[::-1]):
        disasm_instr.append(disassemble_instr(bitstring.Bits(hex=instr[1:])))
        # TODO: Add support for binary
        # Store to disasm_instr first so that we can calculate max length
        # disasm_instr.append(disassemble_instr(int(instr[1:], 16)))
    code_width = len(max(disasm_instr, key=len))

    for i, instr in enumerate(disasm_instr):
        table.add_row(
            str(i),
            data[~i],
            Syntax(instr, "asm", code_width=code_width),
        )
    print(table)

import bitstring

import emu_beta_32 as beta
from disassembler.disassembler import disassemble_instr, str_to_arr


class Emulator:
    """
    TODO: Add class docstring
    """

    def __init__(self, filename, filetype):
        """
        TODO: Add method docstring
        """
        if filetype in ("bin", "hex"):
            self.filetype = filetype
        else:
            raise ValueError("Invalid filetype")

        with open(f"{filename}.{filetype}", "r", encoding="utf8") as file_pointer:
            self.asm_instr = str_to_arr(file_pointer.read())

        try:
            with open(f"{filename}_data.hex", "r", encoding="utf8") as file_pointer:
                self.asm_data = str_to_arr(file_pointer.read())
        except FileNotFoundError:
            # If no data file is found, just set it to an empty list
            self.asm_data = []

        if self.filetype == "bin":
            self.disasm_instr = [
                disassemble_instr(bitstring.Bits(bin=instr[1:]))
                for instr in self.asm_instr[::-1]
            ]
            self.raw_disasm_instr = [
                disassemble_instr(bitstring.Bits(bin=instr[1:]), True)
                for instr in self.asm_instr[::-1]
            ]
        else:
            self.disasm_instr = [
                disassemble_instr(bitstring.Bits(hex=instr[1:]))
                for instr in self.asm_instr[::-1]
            ]
            self.raw_disasm_instr = [
                disassemble_instr(bitstring.Bits(hex=instr[1:]), True)
                for instr in self.asm_instr[::-1]
            ]

        self.registers = [0] * beta.num_registers
        self.history = []
        self.program_counter = 0

    def step(self):
        """
        TODO: Add method docstring
        """
        # 1. Get instruction
        # 2. Calcuate register endstate
        # 3. Update history
        #    - Store history as:
        #      instr_addr: {register_updated: (reg_idx, reg_val), data_mem_updated: (data_addr, data_val), stack_updated(?): (sp, stack_val)}
        #    - Only store new values
        #    - NOTE: WE SHOULD BE STORING THE OLD VALUES,
        #            NOT THE UPDATED VALUES
        # 4. Return values
        instruction = self.raw_disasm_instr[self.program_counter // 4]
        print(instruction)
        self.parse(instruction)

    def parse(self, instruction):
        # op is of type string corresponding to instruction opcode
        # args are of type bitstream.Bits corresponding to instruction arguments
        op, args = instruction

        if hasattr(beta, op):
            result = getattr(beta, op)(
                op,
                args,
                {
                    "registers": self.registers,
                    "data_memory": self.asm_data,
                    "pc": self.program_counter,
                },
            )
        else:
            result = {}
        print(result)
        if "pc" in result:
            self.program_counter = result["pc"][1]
            # Only instruction that doesn't change PC is HALT
            # Meaning we only don't add to history when HALT-ed; end program
            self.history.append(result)
        if "registers" in result:
            reg = result["registers"]
            self.registers[reg[0]] = reg[1]
        if "data_memory" in result:
            data = result["data_memory"]
            self.asm_data[data[0]] = data[1]

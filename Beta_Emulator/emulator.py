import bitstring

import emu_beta_64 as beta
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
            if self.filetype == "hex":
                self.asm_data = [bitstring.Bits(hex=i[1:]).int for i in self.asm_data][
                    ::-1
                ]
            else:
                self.asm_data = [bitstring.Bits(bin=i[1:]).int for i in self.asm_data][
                    ::-1
                ]
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

        # Expose machine-specific constants to the output
        self.memory_width = beta.memory_width
        self.instruction_width = beta.instruction_width
        self.num_registers = beta.num_registers

        self.registers = [0] * beta.num_registers
        self.history = []
        self.program_counter = 0

        self.last_accessed = {"registers": [], "data_memory": []}

    def step_forward(self):
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
        instruction = self.raw_disasm_instr[
            self.program_counter // (beta.instruction_width // 8)
        ]
        self.parse(instruction)

    def step_backward(self):
        if len(self.history) > 0:
            if "pc" in self.history[-1]:
                self.program_counter = self.history[-1]["pc"][0]
            if "registers" in self.history[-1]:
                reg = self.history[-1]["registers"]
                self.registers[reg[0]] = reg[1]
                self.last_accessed["registers"].pop()
            if "data_memory" in self.history[-1]:
                data = self.history[-1]["data_memory"]
                self.asm_data[data[0] // (beta.memory_width // 8)] = data[1]
                self.last_accessed["data_memory"].pop()

            return self.history.pop()
        else:
            # TODO: Verify this is the right way to handle it
            return {"pc": 0}

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

        # Check if register being overwritten is R15
        if "registers" in result and result["registers"][0] == 15:
            del result["registers"]

        if not self.history or result != self.history[-1]:
            if "pc" in result:
                self.program_counter = result["pc"][1]
                # Only instruction that doesn't change PC is HALT
                # Meaning we only don't add to history when HALT-ed; end program
                self.history.append(result)
            if "registers" in result:
                reg = result["registers"]
                self.registers[reg[0]] = reg[2]
                self.last_accessed["registers"].append(reg[0])
            if "data_memory" in result:
                data = result["data_memory"]
                self.asm_data[data[0] // (beta.memory_width // 8)] = data[2]
                self.last_accessed["data_memory"].append(data[0])

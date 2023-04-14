import random

import bitstring

instruction_width = 32
memory_width = 32
num_registers = 32


def op(operator, args, state):
    if operator == "ADD":
        result = (state["registers"][args[0]] + state["registers"][args[1]]) & (
            2 ** (memory_width + 1) - 1
        )
    elif operator == "SUB":
        result = (state["registers"][args[0]] - state["registers"][args[1]]) & (
            2 ** (memory_width + 1) - 1
        )
    elif operator == "MUL":
        result = (state["registers"][args[0]] * state["registers"][args[1]]) & (
            2 ** (memory_width + 1) - 1
        )
    elif operator == "DIV":
        result = (state["registers"][args[0]] // state["registers"][args[1]]) & (
            2 ** (memory_width + 1) - 1
        )
    elif operator == "CMPEQ":
        result = int(state["registers"][args[0]] == state["registers"][args[1]])
    elif operator == "CMPLT":
        result = int(state["registers"][args[0]] < state["registers"][args[1]])
    elif operator == "CMPLE":
        result = int(state["registers"][args[0]] <= state["registers"][args[1]])
    elif operator == "AND":
        result = (
            bitstring.Bits(int=state["registers"][args[0]], length=memory_width)
            & bitstring.Bits(int=state["registers"][args[1]], length=memory_width)
        ).int
    elif operator == "OR":
        result = (
            bitstring.Bits(int=state["registers"][args[0]], length=memory_width)
            | bitstring.Bits(int=state["registers"][args[1]], length=memory_width)
        ).int
    elif operator == "XOR":
        result = (
            bitstring.Bits(int=state["registers"][args[0]], length=memory_width)
            ^ bitstring.Bits(int=state["registers"][args[1]], length=memory_width)
        ).int
    elif operator == "XNOR":
        result = ~(
            bitstring.Bits(int=state["registers"][args[0]], length=memory_width)
            ^ bitstring.Bits(int=state["registers"][args[1]], length=memory_width)
        ).int
    elif operator == "SHL":
        result = (
            bitstring.Bits(int=state["registers"][args[0]], length=memory_width)
            << state["registers"][args[1]]
        ).int
    elif operator == "SHR":
        result = (
            bitstring.Bits(int=state["registers"][args[0]], length=memory_width)
            >> state["registers"][args[1]]
        ).int
    elif operator == "SRA":
        result = (state["registers"][args[0]] % (1 << memory_width)) >> state[
            "registers"
        ][args[1]]
    else:
        raise ValueError("Unknown operator: " + operator)

    if (result & (1 << (memory_width - 1))) != 0:
        result = result - (1 << result)

    # Returns (register_number, old_value, new_value)
    return {
        "registers": (args[2], state["registers"][args[2]], result),
        "pc": (state["pc"], state["pc"] + 4),
    }


def opc(operator, args, state):
    if operator == "ADDC":
        result = (state["registers"][args[0]] + args[1]) & (2 ** (memory_width + 1) - 1)
    elif operator == "SUBC":
        result = (state["registers"][args[0]] - args[1]) & (2 ** (memory_width + 1) - 1)
    elif operator == "MULC":
        result = (state["registers"][args[0]] * args[1]) & (2 ** (memory_width + 1) - 1)
    elif operator == "DIVC":
        result = (state["registers"][args[0]] // args[1]) & (
            2 ** (memory_width + 1) - 1
        )
    elif operator == "CMPEQC":
        result = int(state["registers"][args[0]] == args[1])
    elif operator == "CMPLTC":
        result = int(state["registers"][args[0]] < args[1])
    elif operator == "CMPLEC":
        result = int(state["registers"][args[0]] <= args[1])
    elif operator == "ANDC":
        result = (
            bitstring.Bits(int=state["registers"][args[0]], length=memory_width)
            & bitstring.Bits(int=args[1], length=memory_width)
        ).int
    elif operator == "ORC":
        result = (
            bitstring.Bits(int=state["registers"][args[0]], length=memory_width)
            | bitstring.Bits(int=args[1], length=memory_width)
        ).int
    elif operator == "XORC":
        result = (
            bitstring.Bits(int=state["registers"][args[0]], length=memory_width)
            ^ bitstring.Bits(int=args[1], length=memory_width)
        ).int
    elif operator == "XNORC":
        result = ~(
            bitstring.Bits(int=state["registers"][args[0]], length=memory_width)
            ^ bitstring.Bits(int=args[1], length=memory_width)
        ).int
    elif operator == "SHLC":
        result = (
            bitstring.Bits(int=state["registers"][args[0]], length=memory_width)
            << args[1]
        ).int
    elif operator == "SHRC":
        result = (
            bitstring.Bits(int=state["registers"][args[0]], length=memory_width)
            >> args[1]
        ).int
    elif operator == "SRAC":
        result = (state["registers"][args[0]] % (1 << memory_width)) >> state[
            "registers"
        ][args[1]]
    else:
        raise ValueError("Unknown operator: " + operator)

    if (result & (1 << (memory_width - 1))) != 0:
        result = result - (1 << result)
    # Returns (register_number, old_value, new_value)
    return {
        "registers": (args[2], state["registers"][args[2]], result),
        "pc": (state["pc"], state["pc"] + 4),
    }


ADD = lambda operator, args, state: op(operator, args, state)
SUB = lambda operator, args, state: op(operator, args, state)
MUL = lambda operator, args, state: op(operator, args, state)
DIV = lambda operator, args, state: op(operator, args, state)
CMPEQ = lambda operator, args, state: op(operator, args, state)
CMPLT = lambda operator, args, state: op(operator, args, state)
CMPLE = lambda operator, args, state: op(operator, args, state)
AND = lambda operator, args, state: op(operator, args, state)
OR = lambda operator, args, state: op(operator, args, state)
XOR = lambda operator, args, state: op(operator, args, state)
XNOR = lambda operator, args, state: op(operator, args, state)
SHL = lambda operator, args, state: op(operator, args, state)
SHR = lambda operator, args, state: op(operator, args, state)
SRA = lambda operator, args, state: op(operator, args, state)

ADDC = lambda operator, args, state: opc(operator, args, state)
SUBC = lambda operator, args, state: opc(operator, args, state)
MULC = lambda operator, args, state: opc(operator, args, state)
DIVC = lambda operator, args, state: opc(operator, args, state)
CMPEQC = lambda operator, args, state: opc(operator, args, state)
CMPLTC = lambda operator, args, state: opc(operator, args, state)
CMPLEC = lambda operator, args, state: opc(operator, args, state)
ANDC = lambda operator, args, state: opc(operator, args, state)
ORC = lambda operator, args, state: opc(operator, args, state)
XORC = lambda operator, args, state: opc(operator, args, state)
XNORC = lambda operator, args, state: opc(operator, args, state)
SHLC = lambda operator, args, state: opc(operator, args, state)
SHRC = lambda operator, args, state: opc(operator, args, state)
SRAC = lambda operator, args, state: opc(operator, args, state)


def LD(operator, args, state):
    return {
        "registers": (
            args[2],
            state["registers"][args[2]],
            state["data_memory"][
                (state["registers"][args[0]] + args[1]) // (memory_width // 8)
            ],
        ),
        "pc": (state["pc"], state["pc"] + 4),
    }


def ST(operator, args, state):
    return {
        "data_memory": (
            state["registers"][args[2]] + args[1],
            state["data_memory"][
                (state["registers"][args[2]] + args[1]) // (memory_width // 8)
            ],
            state["registers"][args[0]],
        ),
        "pc": (state["pc"], state["pc"] + 4),
    }


def JMP(operator, args, state):
    return {
        "registers": (args[1], state["registers"][args[1]], state["pc"] + 4),
        "pc": (
            state["pc"],
            (
                bitstring.Bits(uint=state["registers"][args[0]], length=32)
                & bitstring.Bits(uint=0xFFFFFFFC, length=32)
            ).uint,
        ),
    }


def BEQ(operator, args, state):
    if state["registers"][args[0]] == 0:
        return {
            "registers": (args[2], state["registers"][args[2]], state["pc"] + 4),
            "pc": (state["pc"], state["pc"] + 4 + 4 * args[1]),
        }
    else:
        return {
            "registers": (args[2], state["registers"][args[2]], state["pc"] + 4),
            "pc": (state["pc"], state["pc"] + 4),
        }


def BNE(operator, args, state):
    if state["registers"][args[0]] != 0:
        return {
            "registers": (args[2], state["registers"][args[2]], state["pc"] + 4),
            "pc": (state["pc"], state["pc"] + 4 + 4 * args[1]),
        }
    else:
        return {
            "registers": (args[2], state["registers"][args[2]], state["pc"] + 4),
            "pc": (state["pc"], state["pc"] + 4),
        }


def LDR(operator, args, state):
    return {
        "registers": (
            args[2],
            state["registers"][args[2]],
            state["data_memory"][state["pc"] + 4 + 4 * args[1]],
        ),
        "pc": (state["pc"], state["pc"] + 4),
    }


def RAND(operator, args, state):
    return {
        "registers": (
            args[0],
            state["registers"][args[0]],
            random.randint(0, 2**5 - 1),
        ),
        "pc": (state["pc"], state["pc"] + 4),
    }


def NOP(operator, args, state):
    return {"pc": (state["pc"], state["pc"] + 4)}


def PRIV_OP(operator, args, state):
    # TODO: Implement
    return {"pc": (state["pc"], state["pc"] + 4)}


def SVC(operator, args, state):
    # TODO: Implement
    if args[0] == 0:
        # # For running emulator.py
        # button = None
        # while button is None or not button.isnumeric() or not 1 <= int(button) <= 16:
        #     # button = input("Button pressed (1-16): ")
        #     button = str(random.randint(1, 16))

        # return {
        #     "registers": (0, state["registers"][0], int(button)),
        #     "pc": (state["pc"], state["pc"] + 4),
        # }

        # For actual SVC implementation
        return {
            "registers": (30, state["registers"][30], state["pc"] + 4),
            "pc": (state["pc"], 0x800),
        }
    return {"pc": (state["pc"], state["pc"] + 4)}

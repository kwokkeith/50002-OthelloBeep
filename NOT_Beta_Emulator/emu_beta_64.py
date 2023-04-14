import bitstring

instruction_width = 32
memory_width = 64
num_registers = 16

# Operator 
def op(operator, args, state):
    if operator == "ADD":
        result = (state["registers"][args[0]] + state["registers"][args[1]]) & (
            2 ** (memory_width) - 1
        )
    elif operator == "SUB":
        result = (state["registers"][args[0]] - state["registers"][args[1]]) & (
            2 ** (memory_width) - 1
        )
    elif operator == "MUL":
        result = (state["registers"][args[0]] * state["registers"][args[1]]) & (
            2 ** (memory_width) - 1
        )
    elif operator == "DIV":
        result = (state["registers"][args[0]] // state["registers"][args[1]]) & (
            2 ** (memory_width) - 1
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
    elif operator == "INP":
        result = (state["registers"][args[2]] & (2 ** (memory_width) - 1))
    else:
        raise ValueError("Unknown operator: " + operator)

    if result > 0 and (result & (1 << (memory_width - 1))) != 0:
        result = result - (1 << memory_width)

    # Returns (register_number, old_value, new_value)
    return {
        "registers": (args[2], state["registers"][args[2]], result),
        "pc": (state["pc"], state["pc"] + 4),
    }


def opc(operator, args, state):
    if operator == "ADDC":
        result = (state["registers"][args[0]] + args[1]) & (2 ** (memory_width) - 1)
    elif operator == "SUBC":
        result = (state["registers"][args[0]] - args[1]) & (2 ** (memory_width) - 1)
    elif operator == "MULC":
        result = (state["registers"][args[0]] * args[1]) & (2 ** (memory_width) - 1)
    elif operator == "DIVC":
        result = (state["registers"][args[0]] // args[1]) & (2 ** (memory_width) - 1)
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

    if result > 0 and (result & (1 << (memory_width - 1))) != 0:
        result = result - (1 << memory_width)
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
INP = lambda operator, args, state: op(operator, args, state)

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
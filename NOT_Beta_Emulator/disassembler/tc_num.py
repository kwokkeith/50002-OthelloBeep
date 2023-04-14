class TCNum:
    def __init__(self, val, num_bits):
        if isinstance(val, str):
            if set(val).issubset({"0", "1"}):
                self.val = self.twos_comp(int(val, 2), num_bits)
            elif set(val.lower()).issubset(set("abdef0123456789")):
                self.val = self.twos_comp(int(val, 16), num_bits)
            else:
                raise Exception("Invalid value provided to TCNum constructor.")
        elif isinstance(val, int):
            self.val = val
        else:
            raise Exception("Invalid value provided to TCNum constructor.")
        self.num_bits = num_bits

    def twos_comp(self, val, bits):
        """compute the 2's complement of int value val"""
        if (val & (1 << (bits - 1))) != 0:  # if sign bit is set e.g., 8bit: 128-255
            val = val - (1 << bits)  # compute negative value
        return val

    @property
    def bin(self):
        return bin(self.twos_comp(self.val, self.num_bits))[2:].zfill(self.num_bits)

    @bin.setter
    def bin(self, val):
        self.val = self.twos_comp(int(val, 2), self.num_bits)

    @property
    def int(self):
        return self.val

    @int.setter
    def int(self, val):
        self.val = val

    @property
    def hex(self):
        return hex(self.twos_comp(self.val, self.num_bits))[2:].zfill(
            self.num_bits // 4
        )

    @hex.setter
    def hex(self, val):
        self.val = self.twos_comp(int(val, 16), self.num_bits)

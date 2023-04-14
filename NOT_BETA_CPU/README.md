## 64-bit NOT_BETA_CPU

This repository contains the source code that implements 64-bit Beta CPU in Lucid programming language used to run the modified Othello game. Simply open `NOT_BETA_CPU.alp` with [Alchitry Lab](https://alchitry.com/alchitry-labs), **compile**, and **flash** it to Alchitry Au + Alchitry Io Element Board.

This NOT_BETA_CPU contains 16 64-bits registers with a 32-bit instruction memory.

### Instruction Data

Currently, a set of instruction has been inputted inside the `instruction_rom.luc`. These instructions runs the assembly code found in `1d-project-group06/Assembly_Code`. These instructions will start the modified-othello game, which we like to call it Othello-Beep! For the reason of it beeping too much... because it is a rapid-fire inspired game.

The set of instructions also starts with a program checker to ensure that all functionalities of the NOT_BETA_CPU is working before running the game. You might not notice it if you are running the NOT_BETA_CPU in FPGA clock speed (see below). Upon an error, the NOT_BETA_CPU would not run the game but will be trapped into an error mode. You will not see anything lit up on the led matrix if it is connected.

Please refer to our report to understand the game logic. 

### Running the Beta

Firstly, build the game... hopefully it has already been built for you. If not you will have to wait for quite some time... go get some coffee.

Next, ensure that **ALL** `io_dip` is switched OFF when flashing the binary.

Once flashed, you may set the following to run the NOT_BETA_CPU:

1. io_dip[2][7]: toggles between manual (0) and auto mode (1)
2. io_dip[2][6]: toggles between slow (0) or faster clock (1)
3. io_dip[2][5]: toggles clock to FPGA clock speed (1) ("Instant execution")
4. io_dip[1][3](1) + io_button[4]: advances instruction by 1 when in **manual** mode


### Debug Signals

The debug signals spans from `io_led[1:0]` and also the 7 segment.

`io_dip[0]` can be changed to "view" various states presented at `io_led[1]` and `io_led[0]` (16 bits of values at once). Simply set it to represent the values below, e.g: `0x3` means that `io_dip[0]` is set to `00000011` (turn the rightmost two switches on). 

**NOTE**: To output the contents of the register there is a dip-switch (io_dip[1][0])... On (1) this toggles to output the register's content... On (0) this toggles to do the following exhaustive list of debug outputs:

1. `0x0`: MSB 16 bits of current instruction (id[31:16])
2. `0x1`: LSB 16 bits of current instruction (id[15:0])
3. `0x2`: LSB 16 bits of instruction address (ia[15:0])
4. `0x9`: LSB 16 bits of pcsel_out
5. `0xA`: LSB 16 bits of asel_out
6. `0xB`: LSB 16 bits of bsel_out
7. `0xC`: LSB 16 bits of wdsel_out
8. `0xD`: MSB 16 bits of instruction address. Useful to see PC31 (kernel/user mode) (ia[31:16])

The following are the list of register content outputs (when io_dip[1][0] == b1):

io_dip[0][7:4] is used to choose the register you wish to get the contents out of... specifically, if you switched b0010 you be extracting the content of register R2...

1. `0x0`: Reg[15:0] content
2. `0x1`: Reg[31:16] content
3. `0x2`: Reg[47:32] content
4. `0x3`: Reg[63:48] content

### Reset button

If you press Alchitry Au reset button, it will reset the NOT_BETA_CPU to its original state (`PC` set to `0x0`)
In addition, there is also a signal into the CPU connected to an external reset button. That would do the same as the above. 

### Additional Signals

There are 4 additional signals indicated in `io_led[2][7:4]`. This is just a status signal to indicate which clock your Beta CPU is running on.

1. `io_led[2][7]`: auto mode is ON or OFF
2. `io_led[2][6]`: `fastclock` is ON or OFF
3. `io_led[2][5]`: signifies `slowclock` signal
4. `io_led[2][4]`: signifies `fastclock` signal


Project By:
Group 06: Kwok Keith (1006344) | Gizelle Lim Yin Xuan (1006141) | Ong Zheng Han (1005867) | Sean Phay Wei Xiang (1005969) | Cheong Hao Shaun (1005881) | Mubaraquali Muhammed Sufyanali (1006394)

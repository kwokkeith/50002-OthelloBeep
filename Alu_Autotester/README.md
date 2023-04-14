## 64-bit ALU Auto Tester

This repository contains the source code that implements an auto tester to check all instructions in the custom instruction set of the 64-bit ALU. Simply open `ALU_Beta.alp` with [Alchitry Lab](https://alchitry.com/alchitry-labs), **compile**, and **flash** it to Alchitry Au + Alchitry Io Element Board.

This source code contains the main 64-bit ALU used in the NOT_BETA_CPU, and an autotester that runs through all the possible error that could be induced.

### Running the 64-bit ALU Auto tester

Firstly, build the autotester... hopefully it has already been built for you. If not you will have to wait for just awhile... go to the washroom if you like.

Next, ensure that **ALL** `io_dip` is switched OFF when flashing the binary.

### Debug Signals

The debug signals spans from `io_led[1:0]` and also the 7 segment.

`io_dip[0]` can be changed to "view" various states presented at `io_led[1]` and `io_led[0]` (16 bits of values at once). Simply set it to represent the values below, e.g: `0x3` means that `io_dip[0]` is set to `00000011` (turn the rightmost two switches on). 

1. `0x0`: Contents of tester output[15:0]
2. `0x1`: Contents of tester output[31:16]
3. `0x2`: Contents of tester output[47:32]
4. `0x9`: Contents of tester output[63:48]

### Reset button

If you press Alchitry Au reset button, it will reset the FPGA and the autotester

### Additional Signals

There are also inputs to start a new test while the auto-tester is running as well as other functionality...

io_button[2] the bottom button, when triggered will start a new test.
io_button[3] the left button, when triggered will go to the next state... Tester States are explained below:

1. When Tester is running, it will go through a list of test cases. The index of the test case would be displayed on the 7-segment display. 
2. On Error, the Tester will halt and toggle between these 3 states (io_button[3] would toggle between these states)
    Test_ID (Test ID that you can find more information on in our report) -> ALUFN (Output from the 64-bit ALU) -> CORRECT (Correct output from the tester) -> (Back to TEST_ID)
3. On Success, the 7-segment would display `8888` and the io_led on the Alchitry IO Element board would all be lit up. This state indicates that the 64-bit ALU has successfully exceeded all test cases and is ready to be used. 


Done By:
Group 06: Kwok Keith (1006344) | Gizelle Lim Yin Xuan (1006141) | Ong Zheng Han (1005867) | Sean Phay Wei Xiang (1005969) | Cheong Hao Shaun (1005881) | Mubaraquali Muhammed Sufyanali (1006394)
import textual
import bitstring
from bitstring import Bits
from rich.syntax import Syntax
from rich.table import Table
from textual import events
from textual.app import App
from textual.reactive import Reactive
from textual.views import GridView
from textual.widget import Widget
from textual.widgets import Footer, Header
from textual_inputs import IntegerInput
from rich.panel import Panel
from rich.console import Group
from rich.columns import Columns
from rich.align import Align
from emulator import Emulator

# Use python3 emulator_output.py in terminal to run the emulator... 
# Require game.hex in uasm folder
# => Put a game.uasm file in uasm_files
# => navigate to assembler folder
# => Run python3 assembler_output.py -x ../uasm/game (get hexfile)


# Set to False to disable the weird flickering bug going on
refresh_screen = False


def get_range(target_addr, data_len): 
    """
    Left bound => 
    """
    left_bound = right_bound = target_addr

    while right_bound - left_bound < 64 and (left_bound > 0 or right_bound <= data_len):
        if left_bound > 0:
            left_bound -= 1
        if right_bound < data_len:
            right_bound += 1

    return left_bound, right_bound # 0,31 for first iteration


class DataWidget(Widget):
    """
    Reactive Class => Functions as a trigger that tells Textual to change the output display whenever the variable is updated.
    """
    last_accessed = Reactive(-1)  # Init value
    data = Reactive([]) # 
    output_format = Reactive(0)

    def __init__(self, data, memory_width, **kwargs):
        if data:
            DataWidget.data = data
        else:
            DataWidget.data = [00000000] * 100
        DataWidget.memory_width = memory_width
        super().__init__(**kwargs)

    def render(self):
        if self.last_accessed == -1: 
            left_bound, right_bound = get_range(0, len(self.data))
        else:
            left_bound, right_bound = get_range(self.last_accessed, len(self.data))

        table = Table(expand=True)
        table.add_column("n")
        table.add_column(("DATA (HEX)", "DATA (BIN)", "DATA (DEC)")[self.output_format])

        for idx, val in enumerate(self.data[left_bound:right_bound], left_bound):
            if self.last_accessed == idx:
                table.add_row(
                    f"{idx * self.memory_width // 8}",
                    f"{(Bits(int=val, length=self.memory_width).hex, Bits(int=val, length=self.memory_width).bin, val)[self.output_format]}",
                    style="on red",
                )
            else:
                table.add_row(
                    f"{idx * self.memory_width // 8}",
                    f"{(Bits(int=val, length=self.memory_width).hex, Bits(int=val, length=self.memory_width).bin, val)[self.output_format]}",
                )
        return table


class DisassemblerWidget(Widget):
    program_counter = Reactive(0)

    def __init__(self, bytecode, disasm_data, instruction_width, **kwargs):
        self.bytecode = bytecode
        self.disasm_data = disasm_data
        self.instruction_width = instruction_width
        super().__init__(**kwargs)

    def render(self):
        table = Table(expand=True)
        table.add_column("n")
        table.add_column("ASM")
        table.add_column("DISASM")

        code_width = len(max(self.disasm_data, key=len))

        left_bound, right_bound = get_range(self.program_counter, len(self.bytecode))

        for i, instr in enumerate(self.disasm_data[left_bound:right_bound], left_bound):
            if self.program_counter == i:
                table.add_row(
                    f"{i * self.instruction_width // 8}",
                    f"{self.bytecode[i]}",
                    Syntax(instr, "asm", code_width=code_width, background_color="red"),
                    style="on red",
                )
            else:
                table.add_row(
                    str(i * self.instruction_width // 8),
                    self.bytecode[i],
                    Syntax(instr, "asm", code_width=code_width),
                )

        return table


class RegisterWidget(Widget):
    last_accessed = Reactive(-1)
    registers = Reactive([])
    output_format = Reactive(0)

    def __init__(self, registers, memory_width, **kwargs):
        RegisterWidget.registers = registers
        RegisterWidget.memory_width = memory_width
        super().__init__(**kwargs)

    def render(self):
        table = Table(expand=True)
        table.add_column("REG", justify="right")
        table.add_column(("REG (HEX)", "REG (BIN)", "REG (DEC)")[self.output_format])

        for idx, val in enumerate(self.registers):
            if self.last_accessed == idx:
                table.add_row(
                    f"R{idx}",
                    f"{(Bits(int=val, length=self.memory_width).hex, Bits(int=val, length=self.memory_width).bin, val)[self.output_format]}",
                    style="on red",
                )
            else:
                table.add_row(
                    f"R{idx}",
                    f"{(Bits(int=val, length=self.memory_width).hex, Bits(int=val, length=self.memory_width).bin, val)[self.output_format]}",
                )

        return table


class StackWidget(Widget):
    stack_pointer = Reactive(-1)
    stack = Reactive([])
    output_format = Reactive(0)

    def __init__(self, stack, stack_pointer, memory_width, **kwargs):
        StackWidget.stack = stack
        StackWidget.stack_pointer = stack_pointer
        StackWidget.memory_width = memory_width
        super().__init__(**kwargs)

    def render(self):
        table = Table(expand=True)
        table.add_column("n")
        table.add_column(
            ("STACK (HEX)", "STACK (BIN)", "STACK (DEC)")[self.output_format]
        )

        left_bound, right_bound = get_range(self.stack_pointer, len(self.stack))

        # for idx, val in enumerate(self.stack[left_bound:right_bound], left_bound):
        #     if self.stack_pointer == idx:
        #         table.add_row(
        #             f"{idx * self.memory_width // 8}",
        #             f"{(Bits(int=val, length=self.memory_width).hex, Bits(int=val, length=self.memory_width).bin, val)[self.output_format]}",
        #             style="on red",
        #         )
        #     else:
        #         table.add_row(
        #             f"{idx * self.memory_width // 8}",
        #             f"{(Bits(int=val, length=self.memory_width).hex, Bits(int=val, length=self.memory_width).bin, val)[self.output_format]}",
        #         )

        return table



class ScreenWidget(Widget):
    registers = Reactive([0] * 16)

    def __init__(self, **kwargs):
        ScreenWidget.registers = [0] * 16
        super().__init__(**kwargs)




    def render(self):
        table = Table.grid(expand=True, padding=1)
        table.add_column(justify="center")

        output = []
        # Game-specific output for peg solitaire

        for i in reversed(range(0,64)):

            # # 23, 25, 24
            # if i == 36 or i == 27:
            #     output.append(Panel(f"{i + 0:02d}", style="bold red", expand=False))
            # elif i == 35 or i == 28:
            #     output.append(Panel(f"{i + 0:02d}", style="blue", expand=False))
            # if self.registers[23] == i + 1:
            #     output.append(Panel(f"{i + 1}", style="bold red", expand=False))
            # elif self.registers[5] & (1 << i):
            #     output.append(Panel(f"{i + 1}", style="bold green", expand=False))
            if self.registers[11] & (1 << i):
                output.append(Panel(f"{i + 0:02d}", style="red", expand=False))
            elif self.registers[10] & (1 << i):
                output.append(Panel(f"{i + 0:02d}", style="blue", expand=False))
            elif self.registers[6] & (1 << i):
                output.append(Panel(f"{i + 0:02d}", style="green", expand=False))
            elif self.registers[9] & (1 << i):
                output.append(Panel(f"{i + 0:02d}", style="magenta", expand=False))
            else:
                output.append(Panel(f"{i + 0:02d}", style="white", expand=False))
                

        ## Sean: This is the input table
        ## Desired output: 8x8 Grid that cycles between P1 and P2
        
        ## Original Code
        # count = 0
        # for i in range(5):
        #     temp_table = Table.grid()
        #     for _ in range(i):
        #         temp_table.add_column(justify="center")
        #     temp_table.add_row(*output[count : count + i + 1])
        #     table.add_row(Align(temp_table, align="center"))
        #     count += i + 1

        ## Anyhow whack code
        # TO generate the grid of the led matrix for Othello (8 x 8)
        for i in range(8):
            temp_table = Table.grid()
            for _ in range(8):
                temp_table.add_column(justify="center", min_width=10)
            temp_table.add_row(*output[i*8 : i*8 + 8])
            table.add_row(Align(temp_table, align="center"))

        ## TODO 
        # print(output)
        # temp = Table.grid()
        # temp.add_column(justify="left",min_width=70)
        # temp.add_row(*output[0])
        # table.add_row(Align(temp,align="center"))
        return table

    @staticmethod
    def get_singleton():
        if not hasattr(ScreenWidget, "instance"):
            ScreenWidget.instance = ScreenWidget()
        return ScreenWidget.instance



class EmulatorOutput(GridView):
    # TODO: Read from CLI args
    filetype = "hex"

    async def step_forward(self):
        # try:
        #     self.emulator.step_forward()
        # except Exception as e:
        #     self.log(e)

        self.emulator.step_forward()

        state_change = self.emulator.history[-1]
        if "pc" not in state_change:
            self.timer.stop()

        DisassemblerWidget.program_counter = self.emulator.program_counter // (
            self.emulator.instruction_width // 8
        )
        if "registers" in state_change:
            RegisterWidget.registers[state_change["registers"][0]] = state_change[
                "registers"
            ][2]

            ScreenWidget.registers[state_change["registers"][0]] = state_change[
                "registers"
            ][2]

            RegisterWidget.last_accessed = self.emulator.last_accessed["registers"][-1]

            

        # if "data_memory" in state_change:
        #     DataWidget.data[
        #         state_change["data_memory"][0] // (self.emulator.memory_width // 8)
        #     ] = state_change["data_memory"][2]
        #     DataWidget.last_accessed = self.emulator.last_accessed["data_memory"][
        #         -1
        #     ] // (self.emulator.memory_width // 8)

        self.disassembler_widget.refresh()
        self.register_widget.refresh()
        # self.data_widget.refresh()
        # self.stack_widget.refresh()
        # TODO: Figure out flickering issue
        if refresh_screen:
            ScreenWidget.get_singleton().refresh()

    async def step_backward(self):
        state_change = self.emulator.step_backward()
        if "pc" not in state_change:
            await self.timer.stop()

        DisassemblerWidget.program_counter = self.emulator.program_counter // (
            self.emulator.instruction_width // 8
        )
        if "registers" in state_change:
            RegisterWidget.registers[state_change["registers"][0]] = state_change[
                "registers"
            ][1]

            ScreenWidget.registers[state_change["registers"][0]] = state_change[
                "registers"
            ][1]
            if len(self.emulator.last_accessed["registers"]) > 0:
                RegisterWidget.last_accessed = self.emulator.last_accessed["registers"][
                    -1
                ]
            else:
                RegisterWidget.last_accessed = -1

        if "data_memory" in state_change:
            DataWidget.data[
                state_change["data_memory"][0] // (self.emulator.memory_width // 8)
            ] = state_change["data_memory"][1]
            if len(self.emulator.last_accessed["data_memory"]) > 0:
                DataWidget.last_accessed = self.emulator.last_accessed["data_memory"][
                    -1
                ] // (self.emulator.memory_width // 8)
            else:
                DataWidget.last_accessed = -1

        self.disassembler_widget.refresh()
        self.register_widget.refresh()
        self.data_widget.refresh()
        self.stack_widget.refresh()
        # TODO: Figure out flickering issue
        if refresh_screen:
            ScreenWidget.get_singleton().refresh()

    async def on_mount(self, _) -> None:
        # TODO: Take filename argument from CLI
        self.emulator = Emulator("uasm_files/game", self.filetype)

        self.timer = self.set_interval(0.0005, self.step_forward)

        self.grid.add_column(name="a")
        self.grid.add_column(name="b")
        # self.grid.add_column(name="c")
        # self.grid.add_column(name="d")

        self.grid.add_row(fraction=1, name="1")
        self.grid.add_row(fraction=1, name="2")

        self.grid.add_areas(
            area1="a,1-start|2-end",
            area2="b,1-start|2-end",
            # area3="c,1-start|2-end",
            # area4="d,1-start|2-end",
        )

        self.disassembler_widget = DisassemblerWidget(
            [i[1:] for i in self.emulator.asm_instr[::-1]],
            self.emulator.disasm_instr,
            self.emulator.instruction_width,
        )
        self.register_widget = RegisterWidget(
            self.emulator.registers, self.emulator.memory_width
        )
        # self.data_widget = DataWidget(
        #     self.emulator.asm_data[::-1], self.emulator.memory_width
        # )

        # self.stack_widget = StackWidget(
        #     self.emulator.asm_data[::-1],
        #     self.emulator.registers[29],
        #     self.emulator.memory_width,
        # )
        self.grid.place(
            area1=self.disassembler_widget,
            area2=self.register_widget,
            # area3=self.data_widget,
            # area4=self.stack_widget,
        )


class EmulatorOutputApp(App):
    running = True

    async def on_load(self, event: events.Load) -> None:
        await self.bind("q", "quit", "Quit")
        await self.bind("escape", "quit", "Quit")
        await self.bind("p", "toggle", "Toggle")
        #await self.bind("a", "step_backward", "Step Backward")
        # await self.bind("d", "step_forward", "Step Foward")
        #await self.bind("b", "output_format", "Toggle Format")
        await self.bind("j", "toggle_io", "IO")
        await self.bind("enter", "submit", "Submit")
        
        # TODO Testing new bindings
        # need to bind the left, right, up, down, confirm and R5
        await self.bind("w", "up", "Up")
        await self.bind("a", "left", "Left")
        await self.bind("s", "down", "Down")
        await self.bind("d", "right", "Right")

        await self.bind("5", "register5", "Register5")

    async def on_mount(self) -> None:
        self.emulator_output = EmulatorOutput()
        self.integer_input = IntegerInput(name="input", title="Input")
        self.screen_output = ScreenWidget.get_singleton()
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom", z=1)
        await self.view.dock(self.emulator_output, edge="top")
        await self.view.dock(self.integer_input, self.screen_output, edge="top", z=1)

        self.integer_input.layout_offset_x = -1000
        self.screen_output.layout_offset_x = -1000

    async def action_toggle(self):
        if self.running:
            self.emulator_output.timer.pause()
            self.running = False
        else:
            self.emulator_output.timer.resume()
            self.running = True

    async def action_toggle_io(self):
        if self.integer_input.layout_offset_x == 0:
            self.integer_input.layout_offset_x = -1000
            self.screen_output.layout_offset_x = -1000
        else:
            self.integer_input.layout_offset_x = 0
            self.screen_output.layout_offset_x = 0

    async def action_submit(self):
        pass
        # self.emulator_output.emulator.registers[22] = self.integer_input.value
        # self.integer_input.value = 0
        # self.integer_input.layout_offset_x = -1000
        # self.screen_output.layout_offset_x = -1000

 

    async def action_step_backward(self):
        await self.emulator_output.step_backward()

    async def action_step_forward(self):
        await self.emulator_output.step_forward()

    # TODO Event Actions 
    async def action_up(self):
        # 00100
        """
        Initialise a pointer in the screen widget table => 
        Throw the value into R5 first
        There'll be a function out
        """
        self.emulator_output.emulator.registers[5] = 3
        ...

    async def action_left(self):
        # 10000
        self.emulator_output.emulator.registers[5] = 1
        ...

    async def action_down(self):
        # 00010
        self.emulator_output.emulator.registers[5] = 4
        ...

    async def action_right(self):
        # 01000
        self.emulator_output.emulator.registers[5] = 2
        ...

    async def action_register5(self):
        self.emulator_output.emulator.registers[5] = 5
        

        ...    


    async def action_output_format(self):
        self.emulator_output.register_widget.output_format = (
            self.emulator_output.register_widget.output_format + 1
        ) % 3
        self.emulator_output.stack_widget.output_format = (
            self.emulator_output.stack_widget.output_format + 1
        ) % 3

        self.emulator_output.data_widget.output_format = (
            self.emulator_output.data_widget.output_format + 1
        ) % 3


EmulatorOutputApp.run(title="Beta Emulator", log="textual.log")

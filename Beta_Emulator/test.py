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
from rich.console import Group, Console
from rich.columns import Columns
from rich.align import Align
from emulator import Emulator
# from rich import print as rprint
grid = Table.grid(expand=True)
grid.add_column()
grid.add_column(justify="right")
# grid.add_row("Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:")

for i in range(8):
    grid.add_row("hellos")
    # grid.add_column("yope")


console = Console()
console.print(grid)
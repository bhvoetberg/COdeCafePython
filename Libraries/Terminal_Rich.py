# pip install rich

from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars")
table.add_column("Released")
table.add_column("Title")

table.add_row("Some year", "Some title")

console = Console()
console.print(table)



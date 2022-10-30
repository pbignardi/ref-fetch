from rich.console import Console
from rich.theme import Theme

default_theme = Theme({
    "info": "italic cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green",
    "header": "bold"
})

console = Console(theme=default_theme)

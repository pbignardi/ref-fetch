from rich.layout import Layout
from rich.table import Table
from rich.box import SIMPLE_HEAD, SIMPLE_HEAVY
from data import Configuration, ResultData
from console import console


def res_table(rd: ResultData):
    """
    Function to return table with results
    Display table from rp.start to rp.start+rp.n_it
    """
    table = Table(
        expand=True,
        show_lines=False,
        box=SIMPLE_HEAVY,
        show_footer=True
    )
    table.add_column("", width=4, no_wrap=True, justify="center")
    table.add_column("[magenta][Id][/magenta]", max_width=7, no_wrap=True)
    table.add_column("[header]Title[/header]", ratio=5, no_wrap=True)
    table.add_column("[header]Author[/header]", ratio=2, no_wrap=True)
    table.add_column("[header]Year[/header]", max_width=10, no_wrap=True)
    table.add_column("[header]Venue[/header]", ratio=3, no_wrap=True)
    table.add_column("[header]Citations[/header]",max_width=10, no_wrap=True)

    for i, entry in enumerate(rd.visible):
        global_index = rd.start + i
        # set the font to something if entry is selected, else standard
        if global_index == rd.current:
            style = "bold " + rd.config.current_color
        elif global_index in rd.selected:
            style = rd.config.select_color 
        elif global_index % 2 == 0:
            style = ""
        else:
            style = "dim"
        selection_arrow = "[bold]->[/bold]" if (global_index == rd.current) else ""
        # add row
        table.add_row(
            selection_arrow,
            str(global_index), 
            entry.title,
            entry.author,
            entry.year,
            entry.venue,
            entry.n_cit,
            style=style)
    return table

def selected_bar(rd:ResultData):
    color = rd.config.select_color
    pubs_strings = [f"[{color}]{p}[/{color}]" for p in sorted(rd.selected)]
    return "Selected publications : " + ", ".join(pubs_strings)

def footer_bar(config: Configuration):
    cmd_color = config.command_color
    comands_pair = [f"{k}: [bold {cmd_color}]{v}[/]" for k,v in config.cmds.items()]
    return ", ".join(comands_pair)

def make_layout() -> Layout:
    layout = Layout(name="root")
    layout.split(
        Layout(name="table"),
        Layout(name="selected"),
        Layout(name="footer")
    )
    layout["selected"].size = 3
    layout["footer"].size = 3
    return layout
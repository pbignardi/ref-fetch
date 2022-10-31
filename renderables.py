from rich.table import Table
from rich.box import SIMPLE_HEAD, SIMPLE_HEAVY
from data import Configuration, ResultData
from console import console


def res_table(rd: ResultData):
    """
    Function to return table with results
    Display table from rp.start to rp.start+rp.n_it
    """
    title = f"[info]Results for:[/info] [success]{rd.search}[/success]"

    table = Table(
        expand=True,
        show_lines=False,
        title=title,
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
    pass

def footer_bar(config: Configuration):
    return "footer"
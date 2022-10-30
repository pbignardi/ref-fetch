from rich.table import Table
from rich.box import SIMPLE_HEAD, SIMPLE_HEAVY
from data import ResultData, ResultParameters


def res_table(rd: ResultData, rp: ResultParameters):
    title = f"[info]Results for:[/info] [success]{rd.search}[/success]"

    table = Table(
        expand=True,
        show_lines=False,
        title=title,
        box=SIMPLE_HEAVY,
        row_styles=["dim", ""],
        show_footer=True
    )
    table.add_column("[magenta][Id][/magenta]", max_width=7)
    table.add_column("[header]Title[/header]", ratio=5)
    table.add_column("[header]Author[/header]", ratio=2)
    table.add_column("[header]Year[/header]", max_width=10)
    table.add_column("[header]Venue[/header]", ratio=3)
    table.add_column("[header]N. Citations[/header]",max_width=10)

    active = rd.results[rp.start:rp.start+rp.n_it]
    for i, entry in enumerate(active):
        # set the font to something if entry is selected, else standard
        color = "bold magenta" if (i in rd.selected) else ""
        # add row
        table.add_row(
            str(i), 
            entry.title,
            entry.author,
            entry.year,
            entry.venue,
            entry.n_cit,
            style=color)
    return table

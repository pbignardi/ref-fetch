from textwrap import wrap
from typing import Iterable
from abstract_result import AbstractResult
from scholarly_interface import ScholarlyResult, init_results, scholarly_search
from rich.prompt import Prompt
from rich.table import Table
from rich.theme import Theme
from rich.box import SIMPLE_HEAD, MINIMAL_HEAVY_HEAD, SIMPLE_HEAVY
from rich.live import Live
from getch import getch
from console import console

DEBUG = True

next_line_cmd = "n"
prev_line_cmd = "p"
quit_cmd = "q"


def result_table(
    q: Iterable[AbstractResult], 
    search_query: str,
    start: int) -> Table:
    
    end = start + 10
    table_title = f"[info]Results for:[/info] [success]{search_query}[/success]"

    results = Table(
        expand=True,
        show_lines=False,
        title= table_title,
        box=SIMPLE_HEAVY, 
        row_styles=["dim", ""],
        show_footer=True)
    results.add_column("[magenta][Id][/magenta]", max_width=7)
    results.add_column("[header]Title[/header]", ratio=5)
    results.add_column("[header]Author[/header]", ratio=2)
    results.add_column("[header]Year[/header]", max_width=10)
    results.add_column("[header]Venue[/header]", ratio=3)
    results.add_column("[header]N. Citations[/header]",max_width=10)
        
    pos = 0
    for entry in q:
        pos += 1
        if pos <= start:
            continue
        if pos > end:
            break
        results.add_row(
            str(pos), 
            entry.title,
            entry.author,
            entry.year,
            entry.venue,
            entry.n_cit)
    return results

def main():
    if DEBUG:
        import pickle
        with open("test_set", "rb") as f:
            q_res = pickle.load(f)
        search = "spacetime"
        
    else:
        search = Prompt.ask("Enter search query")
        console.print("[info]Connecting to proxy...[/info]")
        q = scholarly_search(search)
        q_res = init_results(q, 100)
    
    start = 0

    console.print(f"[info]Use [warning]{next_line_cmd}[/warning] and [warning]{prev_line_cmd}[/warning] to navigate the results[/info]")

    with Live(result_table(q_res, search, start), 
            refresh_per_second=10, 
            console=console) as live:
        while True:
            cmd = getch()
            if cmd == next_line_cmd:
                start += 1
                if start >= 100:
                    q_res = q_res + init_results(q, 1)
            if cmd == prev_line_cmd:
                start = max(0, start - 1)
            if cmd == quit_cmd:
                return

            live.update(
                result_table(q_res, search, start)
                )



if __name__ == "__main__":
    main()
from abstract_result import AbstractResult
from scholarly_interface import ScholarlyResult, scholarly_search
from rich.prompt import Prompt
from rich.table import Table
from rich.theme import Theme
from rich.box import SIMPLE_HEAD, MINIMAL_HEAVY_HEAD, SIMPLE_HEAVY
from rich.live import Live
from rich.console import group
from rich.layout import Layout
from getch import getch
from console import console
from data import ResultData, ResultParameters
from renderables import footer_bar, res_table

DEBUG = True

next_line_cmd = "n"
prev_line_cmd = "p"
select_cmd = "s"
quit_cmd = "q"


@group()
def result_updater(rd: ResultData, rp: ResultParameters):
    """
    Main updater function. Return renderable group for print in Live loop
    """
    # return the result table always
    yield res_table(rd, rp)
    # return the footer bar always
    yield footer_bar(rp)
    pass

def main():
    if DEBUG:
        import pickle
        with open("test_set", "rb") as f:
            q_res = pickle.load(f)
        search = "spacetime"
        rdata = ResultData(search, iter(q_res))
        
    else:
        search = Prompt.ask("Enter search query")
        console.print("[info]Connecting to proxy...[/info]")
        q = scholarly_search(search)
        rdata = ResultData(search, q)

    rpars = ResultParameters()

    with Live(result_updater(rdata, rpars), 
            auto_refresh=False, 
            console=console) as live:
        while True:
            cmd = getch()
            if cmd == next_line_cmd:
                rpars.start += 1
            if cmd == prev_line_cmd:
                rpars.start -= 1
            if cmd == quit_cmd:
                return

            live.update(result_updater(rdata, rpars), refresh=True)



if __name__ == "__main__":
    main()
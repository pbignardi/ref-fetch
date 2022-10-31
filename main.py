from abstract_result import AbstractResult
from scholarly_interface import ScholarlyResult, scholarly_search
from rich.prompt import Prompt
from rich.live import Live
from rich.console import group
from rich.layout import Layout
from getch import getch
from console import console
from data import ResultData, Configuration
from renderables import footer_bar, res_table
from typing import List


DEBUG = True

next_line_cmd = "n"
prev_line_cmd = "p"
select_cmd = "s"
quit_cmd = "q"


@group()
def result_updater(rd: ResultData):
    """
    Main updater function. Return renderable group for print in Live loop
    """
    # return the result table always
    yield res_table(rd)
    # return the footer bar always
    #yield footer_bar()
    pass

def main():
    config = Configuration()

    if DEBUG:
        import pickle
        with open("test_set", "rb") as f:
            q_res = pickle.load(f)
        search = "spacetime"
        rdata = ResultData(search, iter(q_res), config)
        
    else:
        search = Prompt.ask("Enter search query")
        console.print("[info]Connecting to proxy...[/info]")
        q = scholarly_search(search)
        rdata = ResultData(search, q, config)

    

    with Live(result_updater(rdata), 
            auto_refresh=False, 
            console=console) as live:
        while True:
            cmd = getch()
            if cmd == config.legal_cmds["next"]:
                rdata.start += 1
            if cmd == config.legal_cmds["previous"]:
                rdata.start -= 1
            if cmd == config.legal_cmds["quit"]:
                return

            live.update(result_updater(rdata), refresh=True)



if __name__ == "__main__":
    main()
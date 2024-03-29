import pandas as pd
from pathlib import Path
from pyrolite.util.pd import read_table

_datadir = (Path(__file__).parent / "../../data/").resolve()

def load_belts():
    return read_table(_datadir / "Prot-belts-testdata.xlsx", index_col=None)


def load_koms():
    return read_table(_datadir / "Koms-Test-data.xlsx", index_col=None)

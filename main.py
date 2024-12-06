import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths =glob.glob("Text_files/*.txt")

for filepath in filepaths:
    df = pd.re
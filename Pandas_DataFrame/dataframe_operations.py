import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from openpyxl import load_workbook
import csv
import pyarrow as pa
import pyarrow.parquet as pq

# To RENAME a column in dataframe
data = []
df = pd.DataFrame(data, columns=['TIMERNAME_ALL'])
df = df.rename(columns={'TIMERNAME_ALL':'TIMERNAME'}) # {'old_column':'new_column'}
#%%

import pandas as pd
import os
import glob
from typing import List

#%%
def extratc_excel(input_path: str) -> List[pd.DataFrame]:

    file_path = glob.glob(os.path.join(input_path,"*.xlsx"))

    dataframe_list = []

    for file in file_path:
        dataframe_list.append(pd.read_excel(file))

    return dataframe_list



if __name__ == "__main__":
    input_path = ".\data\input"
    df = extratc_excel(input_path)
    print(df)
# %%

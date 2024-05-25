from typing import List
import pandas as pd

def transf_data(dataframe: List[pd.DataFrame]) -> pd.DataFrame:
    """
    função que concatena todos os dataframe em um unico dataframe

    args
    dataframe: dataframe concatenado

    """
    return pd.concat(dataframe)
import os
import pandas as pd


def load_excel(dataframe: pd.DataFrame, name_file: str, output: str) -> str:
    """
    Função que realiza a leitura de arquivo do dataframa e salva em um unico arquivo.

    args:
    dataframe: dataframe extraido por extract 
    name_file: gera o nome do arquivo final
    output: caminho do arquivo final

    """ 
    if not os.path.exists(output):
        os.makedirs(output)
    
    dataframe.to_excel(f'{output}/{name_file}.xlsx', index = False)

    return "Arquivo Salvo!"

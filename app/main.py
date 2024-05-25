from pipe.extract import extratc_excel
from pipe.load import load_excel
from pipe.transform import transf_data


if __name__ == "__main__":
    extract_excel = extratc_excel('data/input')
    transf_data = transf_data(extract_excel)
    load_excel = load_excel(transf_data, 'arquivo', 'data/output')


## Git teste 25-05-2024


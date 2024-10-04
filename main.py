import os
from dotenv import load_dotenv
from puxar_planilhas_sharepoint import puxar_planilhas
from atualizacao_gsheet import atualizar_gsheet


# carregar .env 
load_dotenv()
ROOT = os.getenv('ROOT')
PATH_EXCEL = os.path.abspath(os.path.join(ROOT, 'inputs', 'portfolio.xlsx'))

def atualizar_google_sheet():
    puxar_planilhas()
    url = "https://docs.google.com/spreadsheets/d/1x7IUvZnXg2MH2k3QE9Kiq-_Db4eA-2xwFGuswbTDYjg/edit?usp=sharing"
    aba = "raw_portfolio"
    atualizar_gsheet(url, aba, PATH_EXCEL)
    print('Finalizado!')


atualizar_google_sheet()

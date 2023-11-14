from time import strftime
from typing import Any
from datetime import datetime



def Verf_date(num: int) -> Any:    
    if num < 10:
        return f"0{num}"
    elif num >= 10:
        return num   


def Datetime() -> str:
    try:
        tempo = strftime('%H:%M:%S')
        ano = datetime.today().year
        mes = Verf_date(datetime.today().month)
        dia = Verf_date(datetime.today().day)
    except:
        print("Erro ao carregar os dados!")
    else:
        return f'{dia}/{mes}/{ano} {tempo}'

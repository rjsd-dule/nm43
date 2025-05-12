import pandas as pd
import numpy as np
from datetime import datetime
import locale
import re
from typing import List


class FormatExcel:
    def __init__(self,path_excel):
        self.path_excel=path_excel
    
    def formatear_excel(self) -> pd.DataFrame:

        try:

            df=pd.read_excel(self.path_excel)
            df = df.dropna(how='all')
            df = df[~df.apply(lambda row: row.astype(str).str.strip().eq("").all(), axis=1)]

            cuenta = separator(df.iloc[0, 0])
            
            empresa = df.iloc[0, 1] if not pd.isna(df.iloc[0, 1]) else separator(df.iloc[1,0])

            fecha_inicial = df.iloc[0, 2] if not pd.isna(df.iloc[0, 2]) and isinstance(df.iloc[0, 2], (datetime, pd.Timestamp)) else fechaFormat(df.iloc[2, 0])[0]
                        
            fecha_final = df.iloc[0, 3] if not pd.isna(df.iloc[0, 2]) and isinstance(df.iloc[0, 2], (datetime, pd.Timestamp)) else fechaFormat(df.iloc[2, 0])[1]

            #print(f"cuenta > {cuenta} - empresa > {empresa} - fecha_inicial > {fecha_inicial} < - fecha_final > {fecha_final}")
            
            return df,cuenta,empresa,fecha_inicial,fecha_final
        
        except Exception as ex:
            print(f"[ERROR] Falló la lectura o el formateo del Excel: {ex}")
            return None


def separator(txt:str)-> str:

    if ":" in txt:

        newtxt=txt.split(":")

        print(newtxt)

        return newtxt[1]
    
    else:
        return txt

def fechaFormat(texto: str) -> List[datetime]:

    MESES_ES = {
    "ene": "01", "feb": "02", "mar": "03", "abr": "04", "may": "05", "jun": "06",
    "jul": "07", "ago": "08", "sep": "09", "oct": "10", "nov": "11", "dic": "12"
}

    # Extraer fechas con formato '01-ene-2022'
    fechas_raw = re.findall(r'\d{2}-[a-z]{3}-\d{4}', texto.lower())

    fechas_convertidas = []
    for f in fechas_raw:
        dia, mes_abrev, anio = f.split('-')
        mes_num = MESES_ES.get(mes_abrev)
        if mes_num:
            fecha_str = f"{anio}-{mes_num}-{dia} 23:25:30"
            fecha_dt = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
            fechas_convertidas.append(fecha_dt)

    return fechas_convertidas
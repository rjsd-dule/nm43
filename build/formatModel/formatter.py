# formatter.py
from datetime import datetime
from build.config.config import FORMATO_NUMERO_CANTIDAD, FORMATO_TEXTO_LONGITUD
import pandas as pd

def formatear_numero(numero: float, longitud: int) -> str:
    """
    Formatea el número a un string con el formato adecuado:
    - Longitud total de 'longitud' caracteres.
    - Dos decimales, sin puntos decimales.
    """
    return f"{numero:0{longitud}.2f}".replace('.', '')

def formatear_texto(texto: str, longitud: int) -> str:
    """
    Formatea el texto a la longitud especificada:
    - Si es más corto, lo rellena con espacios a la derecha.
    - Si es más largo, lo recorta.
    """
    #str(df[df['Crédito'].notna()].shape[0]).zfill(5)
    return str(texto).strip().ljust(longitud)[:longitud]

def formatear_cuenta(n_cuenta:str) -> str:
        print(f"varificando > {n_cuenta}")
        return n_cuenta.replace("-", "").ljust(10, '0')[:10]

def formatear_fecha(fecha: datetime) -> str:
    return fecha.strftime("%d%m%y")

def formatear_empresa(empresa) -> str:
    return empresa.upper().replace(",", "").ljust(26)[:26]


def zeros(n:int) -> str:
     return "0"*n

def formatear_importe(importe: float, longitud: int) -> str:
        importe_str = f"{abs(importe):013.2f}".replace(".", "")
        return importe_str.rjust(longitud, '0')[:longitud]

def formatear_referencia(referencia, longitud: int) -> str:
    if pd.isna(referencia) or (isinstance(referencia, str) and referencia.strip().lower() == 'nan'):
        return '0' * longitud
    return str(referencia).replace('.', '').rjust(longitud, '0')[:longitud]

def formatear_textobody(texto: str, longitud: int) -> str:
    return str(texto).strip().ljust(longitud,'0')[:longitud]
    #return str(texto).strip().ljust(longitud)[:longitud]

def clave_Debe_Haber(debe, haber) -> str:
    if pd.isna(debe) and not pd.isna(haber):
        return "2"
    elif not pd.isna(debe) and pd.isna(haber):
        return "1"
    else:
        #print(f"ERROR o ambos vacíos: debe=[{debe}] haber=[{haber}]")
        return "0"

def dbFormater(dh)-> str:
    #print(f"type {type(dh)}")
    # Si el monto es positivo: fue un abono (crédito = 1) a la cuenta. 
    # Si el monto es negativo (ej. -$ 20.00): fue un cargo (débito = 2) a la cuenta.
    valuedh=None

    if int(dh) != 0:
        valuedh = "1" if int(dh) > 0 else "2" 
    else:
        valuedh="0"

    #print(f"Debe {int(dh)} > {type(dh)} [{valuedh}]")

    return valuedh
    


def resolve_error_date(fecha) -> str:
    if fecha is None:
        return "000000"

    # Caso: ya es un datetime
    if isinstance(fecha, datetime):
        return fecha.strftime("%d%m%y")

    # Caso: es string pero hay que parsearlo
    if isinstance(fecha, str):
        fecha = fecha.strip()
        if not fecha:
            return "000000"

        formatos_validos = [
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d",
            "%d/%m/%Y",
            "%m/%d/%Y",
        ]

        for formato in formatos_validos:
            try:
                dt = datetime.strptime(fecha, formato)
                return dt.strftime("%Y-%m-%d").replace("-","")
            except (ValueError, TypeError):
                continue

    return "000000"

def numheader(path_excel:str)-> int:
    df_raw=pd.read_excel(path_excel,header=None)
    df_raw.dropna(how='all')
    file_header=None
    for i, fila in df_raw.iterrows():
        celda = str(fila[0]).strip().lower()  # solo la columna 0
        print(celda)
        if "fecha" in celda:
            file_header = i
            print(f" A Fila encontrada con 'Fecha': índice {file_header}")
            print(f" B Contenido de la fila: {fila.tolist()}")
            break
    if file_header is None:
        raise ValueError("No se encontró ninguna fila con la palabra 'Fecha' en la primera columna.")
    return file_header


def numheaderfooter(path_excel:str,word:str)-> int:
    df_raw=pd.read_excel(path_excel,header=None)
    df_raw.dropna(how='all')
    file_header=None
    for i, fila in df_raw.iterrows():
        for celda in fila:
            if word in str(celda).strip():
                file_header = i
                print(f"Fila encontrada con '{word}': índice {file_header}")
                print(f"Contenido de la fila: {fila.tolist()}")
                break
        if file_header is not None:
            break
    if file_header is None:
        raise ValueError(f"No se encontró ninguna fila con la palabra {word} en la primera columna.")
    return file_header
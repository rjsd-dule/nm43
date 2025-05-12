# calculos.py

import pandas as pd
from build.config.config import FORMATO_NUMERO_CANTIDAD, FORMATO_TEXTO_LONGITUD
from build.formatModel.formatter import formatear_numero
from build.formatModel.formatter import zeros,numheaderfooter

def analizar_df(path_excel: str):

    df_header = pd.read_excel(path_excel, skiprows=2)
    header="Débito" if "Débito" in df_header.columns else "Monto"
    file_header=numheaderfooter(path_excel,header)

    print(f"verificando numero de head {file_header}, el header es {header}")

    df=pd.read_excel(path_excel,header=file_header)
    if header=="Monto":
        df["Débito"]=df["Monto"].apply(lambda x: abs(x) if x < 0 else None)
        df["Crédito"]=df["Monto"].apply(lambda x: abs(x) if x > 0 else None)
        column_order = ["Fecha", "Descripción", "Débito", "Crédito", "Monto", "Saldo total"]
        df = df[column_order]

    print(df.head(3))
    total_debe = 0.0
    total_haber = 0.0

    for _, row in df.iterrows():

        debe = row.get("Débito",0)
        haber = row.get("Crédito",0)

        if pd.notna(debe):
            total_debe += debe
        if pd.notna(haber):
            total_haber += haber

    saldo_final_valor = df["Saldo total"].dropna().iloc[-1]
    codigo_saldo = "1" if saldo_final_valor < 0 else "2"

    codigo_registro="33"                                                                    # Código Registro
    clave_entidad=zeros(4)                                                                  # Clave de Entidad 
    clave_oficina=zeros(4)                                                                  # Clave de Oficina 
    n_cuenta=zeros(10)                                                                      # Nº de cuenta
    n_apunte_debe  = str(df[df['Débito'].notna()].shape[0]).zfill(FORMATO_TEXTO_LONGITUD)                                                                   # Nº apuntes Debe
    total_debe_fmt = formatear_numero(total_debe, FORMATO_NUMERO_CANTIDAD)                  # Total importes Debe 
    n_apunte_haber = str(df[df['Crédito'].notna()].shape[0]).zfill(FORMATO_TEXTO_LONGITUD)  # Nº apuntes Haber
    total_haber_fmt = formatear_numero(total_haber, FORMATO_NUMERO_CANTIDAD)                # Total importes Haber 
    codigo_saldo = "1" if saldo_final_valor < 0 else "2"                                    # Código Saldo final
    saldo_final_fmt = formatear_numero(abs(saldo_final_valor), FORMATO_NUMERO_CANTIDAD)     # Saldo final 
    libre="LIBR"

    return {
        "codigo_registro":codigo_registro,
        "clave_entidad":clave_entidad,
        "clave_oficina":clave_oficina,
        "n_cuenta":n_cuenta,
        "total_debe": total_debe_fmt,
        "total_haber": total_haber_fmt,
        "saldo_final": saldo_final_fmt,
        "codigo_saldo": codigo_saldo,
        "n_apunte_debe": n_apunte_debe,
        "n_apunte_haber": n_apunte_haber,
        "libre":libre
    }

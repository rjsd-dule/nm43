import pandas as pd
from build.formatModel.formatter import clave_Debe_Haber,zeros,numheader,dbFormater


def analizar_df_mov(path_excel: str) -> list:

    file_header= numheader(path_excel)

    df = pd.read_excel(path_excel, skiprows=file_header) 

    #print(df.head(3))
    fila_count = 0

    movimientos = []
    for _, row in df.iterrows():

        fila_count +=1

        try:
            
            codigo_registro22="22"
            libre="LIBR"
            clave_oficina_origne=zeros(4)
            fecha_operacion =row.get("Fecha", "") 
            fecha_valor = zeros(6)
            concepto_comun = zeros(2)
            concepto_propio = row.get("Transacción",zeros(3)) # no tiene 
            dh = clave_Debe_Haber(row.get("Débito", 0), row.get("Crédito", 0))
            clave_dh = dh if dh != "0" else dbFormater(row.get("Montoc",0)) # no tiene
            importe = row.get("Saldo total", 0)
            documento = zeros(10)
            referencia_1 = row.get("Referencia","SIN REFERENCIA") # no tiene
            referencia_2 = zeros(16)

            codigo_registro="23"
            codigo_data=zeros(2)
            concepto_1=row.get("Descripción", "SIN DESCRIPCIÓN")
            concepto_2=""

            mov = {
                "codigo_registro22":codigo_registro22,
                "libre":libre,
                "clave_oficina_origne":clave_oficina_origne,
                "fecha_operacion":fecha_operacion,
                "fecha_valor":fecha_valor,
                "concepto_comun":str(concepto_comun),
                "concepto_propio":str(concepto_propio),
                "clave_dh":str(clave_dh),
                "importe":importe,
                "documento":str(documento),
                "referencia_1":str(referencia_1),
                "referencia_2":str(referencia_2),
                "codigo_registro":str(codigo_registro),
                "codigo_data":str(codigo_data),
                "concepto_1":str(concepto_1),
                "concepto_2":str(concepto_2)
            }
            movimientos.append(mov)
        except Exception as e:
            print(f"Error procesando fila:\n{row}\nError: {e}")
    
    return movimientos
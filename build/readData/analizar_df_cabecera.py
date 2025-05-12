import pandas as pd
from build.config.config import DIVISA
from build.formatModel.formatter import zeros
from services.limpiar_excel import FormatExcel


def analizar_df(path_excel: str) :

    format=FormatExcel(path_excel)
    result=format.formatear_excel()

    if result is None:
        print("algo salio mal")
    else:
      df,cuenta,empresa,fecha_inicial,fecha_final=result

    codigo_registro="11"
    clave_entidad=zeros(4)
    clave_oficina=zeros(4)
    n_cuenta=cuenta 
    fecha_inicial=fecha_inicial 
    fecha_final=fecha_final
    clave_dh="2"
    saldo_inicial=zeros(14)
    divisa=DIVISA
    clave_saldo="2"
    modalidad_informacion="3"
    nombre_abreviado=zeros(26)
    empresa=empresa
    libre="LIB"


        #print(f"Varificanco lo zeros > {zeros(4)} > {len(zeros(4))}")
        #print(f"Varificanco lo zeros > {zeros(26)} > {len(zeros(26))}")

    
    return {
        "codigo_registro":codigo_registro,
        "clave_entidad":clave_entidad,
        "clave_oficina":clave_oficina,
        "n_cuenta":n_cuenta,
        "fecha_inicial":fecha_inicial,
        "fecha_final":fecha_final,
        "clave_dh":clave_dh,
        "saldo_inicial":saldo_inicial,
        "divisa":divisa,
        "clave_saldo":clave_saldo,
        "modalidad_informacion":modalidad_informacion,
        "nombre_abreviado":nombre_abreviado,
        "empresa":empresa,
        "libre":libre
    }
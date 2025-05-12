# main.py

from build.formatModel.modelo import RegistroFinal
from build.readData.calculos import analizar_df
from build.config.config import DIVISA

def leer_RegistroFinal(path_excel: str):
    # Llamamos a la función que hace el análisis de los datos
    datos = analizar_df(path_excel)

    # Creamos el objeto RegistroFinal con los datos analizados
    return RegistroFinal(
        codigo_registro=datos["codigo_registro"],
        clave_entidad=datos["clave_entidad"],
        clave_oficina=datos["clave_oficina"],
        n_cuenta=datos["n_cuenta"],
        n_apunte_debe=datos["n_apunte_debe"],
        total_importe_debe=datos["total_debe"],
        n_apuntes_haber=datos["n_apunte_haber"],
        total_importe_haber=datos["total_haber"],
        codigo_saldo_final=datos["codigo_saldo"],
        saldo_final=datos["saldo_final"],
        clave_divisa=DIVISA,
        libre=datos["libre"]
    )


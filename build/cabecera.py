from build.formatModel.modelo import RegistroCabecera
from build.config.config import DIVISA
from build.readData.analizar_df_cabecera import analizar_df

def leer_datos_excel(path_excel: str):
    
    datos=analizar_df(path_excel)
  
    return RegistroCabecera(
        codigo_registro=datos["codigo_registro"],
        clave_entidad=datos["clave_entidad"],
        clave_oficina=datos["clave_oficina"],
        n_cuenta=datos["n_cuenta"], 
        fecha_inicial=datos["fecha_inicial"], 
        fecha_final=datos["fecha_final"],
        clave_dh=datos["clave_dh"],
        saldo_inicial=datos["saldo_inicial"],
        divisa=DIVISA,
        clave_saldo=datos["clave_saldo"],
        modalidad_informacion=datos["modalidad_informacion"],
        nombre_abreviado=datos["nombre_abreviado"],
        empresa=datos["empresa"], 
        libre=datos["libre"]
        )
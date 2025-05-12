from build.formatModel.modelo import MovimientoNorma43
from build.readData.analizar_df_movimientos import analizar_df_mov

def leer_movimientos(path_excel: str):
    datos = analizar_df_mov(path_excel)

    movimientos = []

    for item in datos:
        movimiento = MovimientoNorma43(
            codigo_registro22=item["codigo_registro22"],
            libre=item["libre"],
            clave_oficina_origne=item["clave_oficina_origne"],
            fecha_operacion=item["fecha_operacion"],
            fecha_valor=item["fecha_valor"],
            concepto_comun=item["concepto_comun"],
            concepto_propio=item["concepto_propio"],
            clave_dh=item["clave_dh"],
            importe=item["importe"],
            documento=item["documento"],
            referencia_1=item["referencia_1"],
            referencia_2=item["referencia_2"],
            codigo_registro23=item["codigo_registro"],
            codigo_data=item["codigo_data"],
            concepto_1=item["concepto_1"],
            concepto_2=item["concepto_2"]
        )
        movimientos.append(movimiento)

    return movimientos

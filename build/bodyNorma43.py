import pandas as pd
from datetime import datetime
from dataclasses import dataclass


@dataclass
class MovimientoNorma43:
    fecha_operacion: str
    fecha_valor: str
    concepto_comun: str
    concepto_propio: str
    clave_dh: str       
    importe: float
    documento: str
    referencia_1: str
    referencia_2: str
    #Registros Complementarios
    codigo_registro: str
    codigo_data: str
    concepto_1: str
    concepto_2: str
    
    def formatear_registro_22(self) -> str:
        return(
            "22" +                                                  # Código de Registro
            "0000" +                                                # Libre (relleno, puede ser ceros o espacios según banco)
            "0000" +                                                # Clave de Oficina Origen
            resolve_error_date(self.fecha_operacion)+               # Fecha operación
            "000000" +                                              # Fecha de Valor
            self.formatear_texto(self.concepto_comun, 2) +          # Concepto común
            self.formatear_texto(self.concepto_propio, 3) +         # Concepto propio
            self.clave_dh +                                         # Clave Debe o Haber
            self.formatear_importe(self.importe,14) +               # Importe
            self.formatear_texto(self.documento, 10) +              # Nº de documento
            self.formatear_referencia(self.referencia_1, 12) +      # Referencia 1
            self.formatear_texto(self.referencia_2, 16)             # Referencia 2
        )

    def formatear_registro_23(self) -> str:
        return(
            self.codigo_registro +
            self.codigo_data +
            self.formatear_texto(self.concepto_1,38)+
            self.formatear_texto(self.concepto_2,38)
        )
    def formatear(self) -> str:
         return self.formatear_registro_22() + "\n" + self.formatear_registro_23()

    def formatear_importe(self, importe: float,longitud:int) -> str:
        importe_str = f"{abs(importe):013.2f}".replace(".", "")
        return importe_str.rjust(longitud, '0')[:longitud]
    
    def formatear_referencia(self,referencia, longitud: int) -> str:
        if pd.isna(referencia) or (isinstance(referencia, str) and referencia.strip().lower() == 'nan'):
            return '0' * longitud
        return str(referencia).replace('.', '').rjust(longitud, '0')[:longitud]
    
    def formatear_texto(self, texto: str, longitud: int) -> str:
        return str(texto).strip().ljust(longitud,'0')[:longitud]
    
    def formatear_fecha(self, fecha: datetime) -> str:
        return fecha.strftime("%d%m%y")
    
def leer_movimientos(path_excel: str) -> list:
    df = pd.read_excel(path_excel, skiprows=2) 

    # Limpieza de filas vacías
    #df = df.dropna(how='all')
    #df = df[~df.apply(lambda row: row.astype(str).str.strip().eq("").all(), axis=1)]
    #df.columns = [c.strip() for c in df.columns]

    #print(df.head(5))

    movimientos = []
    for _, row in df.iterrows():
        #print(f'f {row.get("Referencia", "")}')
        try:
            fecha_operacion =resolve_error_date(row.get("Fecha", "")) 
            fecha_valor = "000000"
            concepto_comun = "00"
            concepto_propio = row.get("Transacción")#row.get("Descripción", "SIN DESCRIPCIÓN")
            clave_dh = clave_Debe_Haber(row.get("Débito", 0),row.get("Crédito", 0)) #"1" if float(row.get("Crédito", 0)) < 0 else "2"
            importe = row.get("Saldo total", 0)
            documento = "0000000000"
            referencia1 = row.get("Referencia")
            referencia2 = "0000000000000000"
            codigo_registro="23"
            codigo_data="00"
            concepto_1=row.get("Descripción", "SIN DESCRIPCIÓN")
            concepto_2=""

            mov = MovimientoNorma43(
                fecha_operacion=fecha_operacion,
                fecha_valor=fecha_valor,
                concepto_comun=str(concepto_comun),
                concepto_propio=str(concepto_propio),
                clave_dh=str(clave_dh),
                importe=importe,
                documento=str(documento),
                referencia_1=str(referencia1),
                referencia_2=str(referencia2),
                codigo_registro=str(codigo_registro),
                codigo_data=str(codigo_data),
                concepto_1=str(concepto_1),
                concepto_2=str(concepto_2)
            )
            movimientos.append(mov)
        except Exception as e:
            print(f"Error procesando fila:\n{row}\nError: {e}")
    return movimientos

def clave_Debe_Haber(debe, haber) -> str:
    if pd.isna(debe) and not pd.isna(haber):
        return "2"
    elif not pd.isna(debe) and pd.isna(haber):
        return "1"
    else:
        print(f"ERROR o ambos vacíos: debe=[{debe}] haber=[{haber}]")
        return "0"  # o lanza una excepción si es inválido

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

    


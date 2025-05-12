# modelo.py
from datetime import datetime
from build.formatModel.formatter import formatear_cuenta,formatear_fecha,formatear_empresa,formatear_textobody,formatear_importe,formatear_referencia,resolve_error_date
from dataclasses import dataclass

""" Cabecera """

@dataclass
class RegistroCabecera:
    codigo_registro:str
    clave_entidad:str
    clave_oficina:str
    n_cuenta: str
    fecha_inicial: datetime
    fecha_final: datetime
    clave_dh: str
    saldo_inicial:str
    divisa:str
    clave_saldo:str
    modalidad_informacion:str
    nombre_abreviado:str
    empresa: str
    libre:str

    def formatear(self) -> str:
        print(f"Revisando que llega > {self.codigo_registro}")
        return (
            self.codigo_registro + 
            self.clave_entidad +
            self.clave_oficina +
            formatear_cuenta(self.n_cuenta) +
            formatear_fecha(self.fecha_inicial) +
            formatear_fecha(self.fecha_final) +
            self.clave_saldo +
            self.saldo_inicial +
            self.divisa +
            self.modalidad_informacion +
            formatear_empresa(self.empresa) +
            self.libre
        )
    
""" Movimiento """

@dataclass
class MovimientoNorma43:
    codigo_registro22:str
    libre:str
    clave_oficina_origne:str
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
    codigo_registro23: str
    codigo_data: str
    concepto_1: str
    concepto_2: str

    def formatear_registro_22(self) -> str:
        return(
            self.codigo_registro22 +                                # Código de Registro
            self.libre +                                            # Libre (relleno, puede ser ceros o espacios según banco)
            self.clave_oficina_origne +                             # Clave de Oficina Origen
            resolve_error_date(self.fecha_operacion)+               # Fecha operación
            self.fecha_valor +                                      # Fecha de Valor
            formatear_textobody(self.concepto_comun, 2) +           # Concepto común
            formatear_textobody(self.concepto_propio, 3) +          # Concepto propio
            self.clave_dh +                                         # Clave Debe o Haber
            formatear_importe(self.importe,14) +                    # Importe
            formatear_textobody(self.documento, 10) +               # Nº de documento
            formatear_referencia(self.referencia_1, 12) +           # Referencia 1
            formatear_textobody(self.referencia_2, 16)              # Referencia 2
        )
    
    def formatear_registro_23(self) -> str:
        return(
            self.codigo_registro23 +                 # Código de Registro
            self.codigo_data +                       # Código Dato 
            formatear_textobody(self.concepto_1,38)+ # Concepto 
            formatear_textobody(self.concepto_2,38)  # Concepto
        )
    # Unimos el registro principal de movimientos con su registro complementario.
    def formatear(self) -> str:
         registro1 = self.formatear_registro_22()
         registro2 = self.formatear_registro_23()
         registro_total = registro1 + "\n" + registro2

         return registro_total

    

""" Registro Finl """
@dataclass
class RegistroFinal:
    codigo_registro:str
    clave_entidad: str
    clave_oficina: str
    n_cuenta: str
    n_apunte_debe: str
    total_importe_debe: str
    n_apuntes_haber: str
    total_importe_haber: str
    codigo_saldo_final: str
    saldo_final: str
    clave_divisa: str
    libre: str

    def formatear(self) -> str:
        return (
            self.codigo_registro +
            self.clave_entidad +
            self.clave_oficina +
            self.n_cuenta +
            self.n_apunte_debe +
            self.total_importe_debe +
            self.n_apuntes_haber +
            self.total_importe_haber +
            self.codigo_saldo_final +
            self.saldo_final +
            self.clave_divisa +
            self.libre
        )

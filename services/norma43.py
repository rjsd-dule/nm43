#from cabeceraNorma43 import leer_datos_excel
from build.cabecera import leer_datos_excel
from build.movimiento import leer_movimientos
#from build.bodyNorma43 import leer_movimientos
from build.registro_final import leer_RegistroFinal
import os

# --- Programa principal para generar Norma 43 ---
def generar_norma_43(path_excel: str, output_dir: str = ".", nombre_archivo: str = None)-> str:
    try:
        base_name = nombre_archivo or os.path.splitext(os.path.basename(path_excel))[0]
        output_path = os.path.join(output_dir, base_name + ".txt")

        cabecera_head = leer_datos_excel(path_excel)    # Contrucion de la cabecera
        body_movimientos = leer_movimientos(path_excel) # Contrucion del movimiento
        registro_final = leer_RegistroFinal(path_excel) # Contrucion de registro final

        with open(output_path, "w", encoding="utf-8") as f:
            
            f.write(cabecera_head.formatear() + "\n")
            
            for i, mov in enumerate(body_movimientos, start=1):
                linea = mov.formatear()
                f.write(linea + "\n")
                if i <= 1: 
                    print(f"Movimiento generado ({len(linea)}): {linea}")
                    
            f.write(registro_final.formatear() + "\n")

        print(f"Archivo generado exitosamente: {output_path}")

        return output_path
    except Exception as e:
        print(f"[ERROR] Fallo al generar norma 43: {e}")
        return ""
    
    

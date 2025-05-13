import pandas as pd
import os
from werkzeug.utils import secure_filename
from services.norma43 import generar_norma_43
from build.formatModel.formatter import numheader

def process_uploaded_file(file, upload_folder):
    filename = secure_filename(file.filename)

    filepath = os.path.join(upload_folder, filename)
    
    try:

        file.save(filepath)
        file_header= numheader(filepath)

        df = pd.read_excel(filepath,skiprows=file_header)
        df['Saldo total']=pd.to_numeric(df['Saldo total'],errors='coerce')

    except Exception as e:
        os.remove(filepath)
        return None, None, f"El archivo no es un Excel válido o está dañado. {e}"

    output_path = generar_norma_43(filepath, upload_folder) # 3
    return df, output_path, None

def deletefile():
    upload_folder = 'uploads'
    if os.path.exists(upload_folder):
        for file in os.listdir(upload_folder):
            file_path = os.path.join(upload_folder, file)
            os.remove(file_path)
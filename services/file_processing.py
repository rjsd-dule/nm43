import pandas as pd
import os
from werkzeug.utils import secure_filename
from services.norma43 import generar_norma_43

def process_uploaded_file(file, upload_folder):
    filename = secure_filename(file.filename)

    filepath = os.path.join(upload_folder, filename)

    print(f" upload_folder {upload_folder}")
    print(f"filename {filename} > {file.filename}")
    
    try:

        file.save(filepath)
        df = pd.read_excel(filepath)

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
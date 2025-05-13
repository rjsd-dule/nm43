from flask import request, render_template
from config import UPLOAD_FOLDER
from services.file_validation import allowed_file
from services.file_processing import process_uploaded_file,deletefile
from services.paginator import paginate_df
import os

def handle_upload():
    deletefile()
    if 'file' not in request.files:
        return render_template('index.html', error="No se recibió archivo.")

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error="Ningún archivo seleccionado.")
    
    if not allowed_file(file.filename):
        return render_template('index.html', error="Tipo de archivo no permitido. Solo se aceptan archivos Excel.")
    print("#4")
    df, output_path, error = process_uploaded_file(file, UPLOAD_FOLDER) # 2
    if error:
        print(f"error > {error}")
        return render_template('index.html', error=error)
    print("#5")

    page = request.args.get('page', 1, type=int)
    paginated_df, total_pages = paginate_df(df, page)

    full_table = df.to_html(classes='table table-striped', table_id='resultTable', index=False)

    return render_template('table.html',
                           tables=[paginated_df.to_html(classes='table table-striped', index=False)],
                           full_table=full_table,
                           page=page,
                           total_pages=total_pages,
                           archivo_generado=os.path.basename(output_path),
                           df=df)

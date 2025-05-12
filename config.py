import os

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'xls', 'xlsx'}
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    # Render the main page
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    files = request.files.getlist('file')
    for file in files:
        if file:
            filename = secure_filename(file.filename)
            folder_name = determine_folder(filename)  # Use AI-based sorting logic
            folder_path = os.path.join(app.config['UPLOAD_FOLDER'], folder_name)
            os.makedirs(folder_path, exist_ok=True)
            file_path = os.path.join(folder_path, filename)
            file.save(file_path)
    return jsonify({'message': 'Files uploaded and sorted successfully'})

def determine_folder(filename):
    # Placeholder for AI-based sorting logic
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return 'images'
    elif filename.lower().endswith('.pdf'):
        return 'pdfs'
    else:
        return 'others'

@app.route('/files', methods=['GET'])
def list_files():
    uploads_dir = app.config['UPLOAD_FOLDER']
    files_structure = {}

    for root, dirs, files in os.walk(uploads_dir):
        for file in files:
            path = os.path.relpath(root, uploads_dir)
            if path not in files_structure:
                files_structure[path] = []
            files_structure[path].append(file)

    # Make sure to reference 'files.html', not '/files'
    return render_template('files.html', files_structure=files_structure)


if __name__ == '__main__':
    app.run(debug=True)

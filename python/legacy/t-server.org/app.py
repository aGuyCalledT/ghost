from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)
directory_path = '.' # aktuelles Verzeichnis

@app.route('/list_files')
def list_files():
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    return jsonify(files)

@app.route('/<filename>')
def download_file(filename):
    return send_from_directory(directory_path, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
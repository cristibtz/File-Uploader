from flask import Blueprint, render_template, request, flash, redirect, current_app, send_file, after_this_request, url_for
from werkzeug.utils import secure_filename
from .models import Files
from .create_code import create_code
from . import db
import os, random

upload = Blueprint('upload', __name__)
download = Blueprint('download', __name__)

@upload.route("/", methods=["GET", "POST"])
def upload_file():
    UPLOAD_DIR = current_app.config['UPLOAD_FOLDER']
    if request.method == "POST":
        if 'file' not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash("No selected file")
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            file_code = create_code(filename)

            #Check if file is already in directory
            if Files.query.filter_by(filename=filename).first():
                #Find extension and add number to filename
                filename, extension = os.path.splitext(filename)
                random_number = random.randint(1, 1000)
                filename = filename + f"_{random_number}" + extension

            file.save(os.path.join(UPLOAD_DIR, filename))
            new_file=Files(filename=filename, file_code=file_code)
            db.session.add(new_file)
            db.session.commit()
            flash("File uploaded") 
            return redirect(url_for('upload.upload_file'))

    return render_template("home.html")

@upload.errorhandler(413)
def request_entity_too_large(error):
    return "File is too large" 

@download.route("/", methods=["GET"])
def show_files():
    DOWNLOAD_DIR = current_app.config['UPLOAD_FOLDER']
    directory = os.listdir(DOWNLOAD_DIR)
    return render_template("downloads.html", directory=directory)

@download.route("/<filename>", methods=["GET"])
def download_files(filename):
    DOWNLOAD_DIR = current_app.config['UPLOAD_FOLDER']
    path = DOWNLOAD_DIR + "/" + filename

    @after_this_request
    def delete_file(response):
        try:
            file_entry = Files.query.filter_by(filename=filename).first()
            if file_entry and filename != ".gitkeep":
                os.remove(path)
                db.session.delete(file_entry)
                db.session.commit()
        except Exception as e:
            flash("Error")
        
        return response

    return send_file(path, as_attachment=True)

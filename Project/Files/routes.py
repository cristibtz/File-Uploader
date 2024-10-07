from flask import Blueprint, render_template, request, flash, redirect, current_app, send_file, after_this_request, url_for
from werkzeug.utils import secure_filename
from .models import Files
from . import db
import os

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
            file.save(os.path.join(UPLOAD_DIR, filename))
            new_file=Files(filename=filename, file_code="x")
            db.session.add(new_file)
            db.session.commit()
            flash("File uploaded") 
            return redirect(url_for("upload.upload_file"))

    return render_template("home.html")

@upload.app_errorhandler(413)
def handle_413(error):
    flash("File is too large")
    return redirect(request.url), 413

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


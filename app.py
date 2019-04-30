import os
import flask

from flask import Flask, render_template, redirect, url_for, \
    request, send_from_directory, flash, send_file
from werkzeug import secure_filename
import faceMorph

from config import Config

app = Flask(__name__, static_url_path='')
app.config.from_object(Config)


@app.route('/<filename>', methods=['GET'])
def get_file(filename):
    """ Taking a string of filename as input
    
    """
    return send_file(filename, as_attachment=True,
                     mimetype='image/jpg', last_modified=True)


@app.route('/<filename>', methods=['GET'])
def retrieve_file(filename):
    return send_file('static'/filename, as_attachment=True,
                     mimetype='image/jpg', last_modified=True)


@app.route('/<filename>', methods=['GET', 'POST'])
def download_file(filename):
    return send_file(filename, as_attachment=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file1' not in request.files:
            flash('No file01 part')
            return redirect(request.url)

        if 'file2' not in request.files:
            flash('No file02 part')
            return redirect(request.url)
        file1 = request.files['file1']
        file2 = request.files['file2']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file1.filename == '':
            flash('No selected file01')
            return redirect(request.url)

        if file2.filename == '':
            flash('No selected file02')
            return redirect(request.url)

        morph_rate = int(request.values['morph1'])/100

        #work on this to make it similar to our part
        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
            filename1 = secure_filename(file1.filename)
            filename2 = secure_filename(file2.filename)
            save_to1 = (os.path.join(app.config['UPLOAD_FOLDER'], filename1))
            save_to2 = (os.path.join(app.config['UPLOAD_FOLDER'], filename2))
            file1.save(save_to1)
            file2.save(save_to2)

            morph_result = faceMorph.make_morph(save_to1, save_to2, morph_rate)
            if (type(morph_result) != str):
                flash("The model cannot learn one of the images points. Make sure you upload a clear human face like the examples in about page")
                return render_template('index.html', morph="warning.jpg", filename="warning.jpg",  f1_name=filename1.split(".")[0],
                                       f2_name=filename2.split(".")[0])
            return render_template('index.html', morph=morph_result,
                                   filename=morph_result, f1=filename1, f2=filename2,
                                   f1_name=filename1.split(".")[0],
                                   f2_name=filename2.split(".")[0])

    return render_template('index.html')


# allowed image types
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

# is file allowed to be uploaded?


def allowed_file(filename):
    """Taking a string as the input and check filename extension
        Return true if filename have correct extensions
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

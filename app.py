#hopefully this works
from flask import Flask, render_template, redirect, url_for, request, send_from_directory, flash, send_file
import flask
import os
from werkzeug import secure_filename
import faceMorph


from flask import Flask
from config import Config

app = Flask(__name__, static_url_path='')
app.config.from_object(Config)



@app.route('/<filename>', methods = ['GET'])
def get_file(filename):
    #print(filename)
    return send_file(filename, as_attachment=True, mimetype='image/jpg', last_modified=True)
    #return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

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

        #work on this to make it similar to our part
        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename) :
            filename1 = secure_filename(file1.filename)
            filename2 = secure_filename(file2.filename)
            save_to1=(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
            save_to2=(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
            file1.save(save_to1)
            file2.save(save_to2)
            
            #need a if statement to coorperate with Morph botton(p.s need to get Morph botton work)
            Morph_result= faceMorph.makeMorph(save_to1,save_to2)
            #print(filename1)
            
            return render_template('index.html/about', morph= Morph_result, filename = Morph_result, f1=filename1, f2 =filename2)
            
    return render_template('index.html')

# allowed image types
ALLOWED_EXTENSIONS = set(['jpg','jpeg'])
app.config['ALLOWED_EXTENSIONS']=ALLOWED_EXTENSIONS

# is file allowed to be uploaded?
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

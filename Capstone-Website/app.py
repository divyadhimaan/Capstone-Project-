from flask import Flask
import pickle
from flask import render_template
app = Flask(__name__)

model = pickle.load(open('../Code_Directory/Verification_Phase/SVM/model.pkl','rb'))

from flask import render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import urllib.request
import os
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['SECRET_KEY'] = 'asldfkjlj'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/reload')
def reload_page():
    dirc = 'static/uploads'
    for f in os.listdir(dirc):
        os.remove(os.path.join(dirc, f))

    return redirect('/')

@app.route('/process', methods=['POST'])
def process_image():
    pass

@app.route('/predict', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    # print(file)
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded')
        return render_template('home.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)

# @app.route("/about")
# def about():
#     return render_template("about.html")


# @app.route("/upload", methods=['GET', 'POST'])
# def upload_image():
#     return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)

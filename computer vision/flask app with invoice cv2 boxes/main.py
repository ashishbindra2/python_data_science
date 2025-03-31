import base64
from os import path
from os import makedirs

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from werkzeug.utils import secure_filename

from img_process_util import image_detect

UPLOAD_FOLDER = './static/uploads'
OUTPUT_FOLDER = './static/output'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload folder exists
if not path.exists(UPLOAD_FOLDER):
    makedirs(UPLOAD_FOLDER)
    
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route("/", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
  
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        
        filename = secure_filename(file.filename)
        filepath = path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save the file
        file.save(filepath)
        
      
        return redirect(url_for('select',  filename=filename))
    return render_template('index.html', name = "Ashish")


@app.route('/select',methods = ['GET', 'POST'])
def select():
    
    # img_base64 = request.args.get('img_base64')
    filename = request.args.get('filename')
    filepath = path.join(app.config['UPLOAD_FOLDER'], filename) 
    output_path = path.join(app.config['OUTPUT_FOLDER'], 'detect_'+filename) 

    print("path", filepath)
    
    # Read the file and convert to Base64 for displaying
    with open(filepath, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
    
    if request.method == 'POST':
        detact_type = request.form.get("type")    
        print("post call",detact_type)
        
        image_detect(filepath,output_path, level = detact_type)
         # Read the file and convert to Base64 for displaying
        with open(output_path, "rb") as img_file:
            encoded_image_detected = base64.b64encode(img_file.read()).decode('utf-8')
            
        return render_template('display.html', filename = filename, encoded_image = img_base64,
                               output_path= output_path,encoded_image_detected=encoded_image_detected)
    return render_template('select.html', filename = filename, encoded_image = img_base64)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1',)
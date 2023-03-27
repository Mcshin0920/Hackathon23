from flask import Flask, render_template, request
app = Flask(__name__)
import GPT
import os
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
@app.route('/')
def index():
    return render_template('index.html')


'''
@app.route('/solve/', methods = ['GET', 'POST'])
def upload_file():
   who = request.form.get('equation')
   print('test'+str(who))
   if request.method == 'POST':
      f = request.files['file']
      f.save((f.filename))
      return 'file uploaded successfully'
'''
@app.route('/solve/', methods=['POST'])
def my_form_post():
    text = request.form['equation']
    if text !='':
        processed_text = text.lower()
        answer = GPT.textlatexsolver(processed_text)
        return render_template('index.html', result_message=answer);
    else:
        
        file1 = request.files['file1']
        print(file1.filename)
        answer=GPT.picturelatexsolver(file1)
        print("test")
        return render_template('index.html', result_message=answer);

    

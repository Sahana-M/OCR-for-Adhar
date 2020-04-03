import os
from flask import  Flask, flash, request, redirect, render_template, send_file
import main
import json
import cv2
import numpy as np
import urllib
import config as cfg

app = Flask(__name__, template_folder='./template')


@app.route('/')
def home():
    return render_template('home.html')


#GETING DETAILS FROM AADHAR
@app.route('/get_adhar', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file_url = json.loads(request.data)["file"]
        response = urllib.request.urlopen(file_url)
        file = response.read()    
        npimg = np.fromstring(file, np.uint8)
        file = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        extracted_text = main.steps(file)
        return extracted_text
    return redirect('/')


if __name__ == "__main__":
    app.run()



    
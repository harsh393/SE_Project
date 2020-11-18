import os
from flask import Flask, render_template, request, session
from PIL import Image
import numpy as np
from Metrics import f1,recall
from keras.models import load_model
import sys
from keras.utils import CustomObjectScope
import pandas as pd

model = sys.argv[1]

def weighted_loss(y_true, y_pred):
    return K.mean((weights[:,0]*(1-y_true))(weights[:,1]**(y_true))*K.binary_crossentropy(y_true, y_pred), axis=-1)

def process(img):
    image = np.array(Image.open(img))
    nor_image = image//255
    pil_image = Image.fromarray(image)
    #pil_image = pil_image.resize((224,224))
    pil_image = pil_image.resize((182,268))
    return pil_image
    
    #return (np.array(Image.open(img).resize((200,300),Image.NEAREST))/255.).reshape(1,300,200,3)

def prediction(im):
 #y = pd.read_csv('train.csv').drop(['Id', 'Genre'],axis=1)
 #labels = list(y)
 labels=['Horror','Romance','Adventure','Documentary']
 with CustomObjectScope({'weighted_loss': weighted_loss}):
    model = load_model('genres_1997_2017_g4_r100_e50_v1_lr0.0001')
 #pred = model.predict(np.array(im).reshape(1,224,224,3))
 pred = model.predict(np.array(im).reshape(1,182,268,-1))
 #model = load_model(model,custom_objects={'recall':recall,'f1':f1})
 genre = ['Horror','Romance','Adventure','Documentary']
 #preds = model.predict(im)
 most_likely = pred[0].argsort()[-4:][::-1]
 classes = []
 for i in range(len(most_likely)):
    classes.append(labels[i])
 return classes
 #probs = np.round(preds*100.0,2)
 #return probs

app = Flask(__name__,static_folder='images')
app.secret_key = 'abcd'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
#    session['model'] = load_m()
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT,'images/')

    if not os.path.isdir(target):
        os.mkdir(target)

    f = request.files.get('file')
    filename = f.filename
    destination = '/'.join([target,filename])
    f.save(destination)
    session['img'] = filename
    return render_template('complete.html',image_name=filename)

@app.route('/predict', methods=['POST'])
def predict():
    img = session.get('img',None)
    im = process('images/' + img)
    result = prediction(im)
    return render_template('predict.html',pred=result,image_name=img)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
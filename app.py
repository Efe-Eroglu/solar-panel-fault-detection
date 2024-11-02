import os
from flask import Flask, render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png'}

# Eğer klasör yoksa oluştur
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Modeli yükleme
model = load_model('model/solar_panel_fault_detection_model.keras')

# Sınıf etiketleri
class_labels = ['Bird-Drop', 'Clean', 'Dusty', 'Electrical-Damage', 'Physical-Damage', 'Snow-Covered']

def allowed_file(filename):
    """Dosya uzantısını kontrol eder."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def predict_image(image_path):
    """Görüntüyü yükler, ön işler ve modelle tahmin yapar."""
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
  
    predictions = model.predict(img_array)
    predicted_class = class_labels[np.argmax(predictions)]
    
    return predicted_class

@app.route('/classify')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        prediction = predict_image(file_path)
        
        return jsonify({
            "prediction": prediction,
            "image_url": url_for('static', filename=f'uploads/{filename}')
        })
    else:
        return jsonify({"error": "Allowed file types are jpg, jpeg, png"})

if __name__ == '__main__':
    app.run(debug=True)

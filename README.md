# Plant Disease Detection Project

## 1. Introduction
Plant disease detection is an essential application in the agricultural sector. This project utilizes image processing and machine learning techniques to analyze leaf images and determine whether the plant is healthy or diseased.

## 2. Literature Survey
Several approaches exist for plant disease detection, including traditional visual inspections, deep learning models, and image processing techniques. Our project focuses on using OpenCV and machine learning algorithms for analysis.

## 3. Technical Requirements
- Python 3.x
- Flask
- OpenCV
- NumPy
- skimage
- Vue.js
- Bootstrap

## 4. Project Description
The project involves uploading an image of a plant leaf, processing it using OpenCV, and determining its health status based on disease index calculations.

## 5. System Design
1. **Frontend**: Vue.js-based interface for image upload and displaying results.
2. **Backend**: Flask API for processing images and returning results.
3. **Processing**: OpenCV and NumPy for image processing.

## 6. Source Code

### Backend (Flask API)
```python
from flask import Flask, request, jsonify
import cv2
import numpy as np
from skimage import filters

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def process_image():
    file = request.files['image']
    if not file:
        return jsonify({'error': 'No file uploaded'})

    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    disease_index = np.mean(thresh) / 255.0
    status = 'Diseased' if disease_index < 0.5 else 'Healthy'
    affected_area_percentage = np.mean(thresh) * 100 / 255

    return jsonify({
        'affected_area_percentage': affected_area_percentage,
        'disease_index': disease_index,
        'num_diseased_regions': np.sum(edges > 0),
        'status': status
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### Frontend (Vue.js)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Plant Disease Detection</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
  <link rel="stylesheet" href="/static/css/style.css">
  <style>
    body {
      background-color: #f8f9fa;
    }
    .container {
      max-width: 600px;
    }
    .card {
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .btn-primary {
      width: 100%;
    }
    .image-preview {
      max-height: 300px;
      object-fit: cover;
      border-radius: 8px;
    }
  </style>
</head>
<body>
  <div id="app" class="container mt-5">
    <div class="card p-4">
      <h2 class="text-center mb-4">🌱 Plant Disease Detection</h2>
      
      <form @submit.prevent="uploadImage">
        <div class="form-group">
          <label for="image">📸 Upload a plant leaf image:</label>
          <input type="file" class="form-control-file" id="image" @change="handleFileUpload">
        </div>
        <button type="submit" class="btn btn-primary">🔍 Detect Disease</button>
      </form>

      <!-- Loading Spinner -->
      <div v-if="loading" class="text-center mt-3">
        <div class="spinner-border text-primary" role="status">
          <span class="sr-only">Processing...</span>
        </div>
      </div>

      <!-- Results Section -->
      <div v-if="result" class="mt-4 text-center">
        <h4 class="font-weight-bold">🩺 Diagnosis:</h4>
        <p><strong>🌿 Affected Area:</strong><span v-html="result.affected_area_percentage.toFixed(2)"></span></p>
        <p><strong>🧬 Disease Index:</strong><span v-html="result.disease_index.toFixed(4)"></span></p>
        <p><strong>🦠 Diseased Regions:</strong><span v-html="result.num_diseased_regions"></span></p>
        <p><strong>Diseased Status:</strong> 
          <span v-html="result.status"></span>
          <span v-if="result.status === 'Healthy'"> ✅</span>
          <span v-else> ⚠️</span>
        </p>
 
        <img :src="imageUrl" alt="Uploaded image" class="img-thumbnail image-preview mt-3" v-if="imageUrl">
      </div>
    </div>
  </div>

  <!-- Vue.js -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
  <script src="/static/js/app.js"></script>
</body>
</html>

```

### JavaScript (Vue.js Logic)
```javascript
new Vue({
  el: '#app',
  data: {
    imageFile: null,
    imageUrl: '',
    result: null
  },
  methods: {
    handleFileUpload(event) {
      this.imageFile = event.target.files[0];
      this.imageUrl = URL.createObjectURL(this.imageFile);
    },
    uploadImage() {
      let formData = new FormData();
      formData.append('image', this.imageFile);
      fetch('/upload', { method: 'POST', body: formData })
        .then(response => response.json())
        .then(data => this.result = data)
        .catch(error => console.error('Error:', error));
    }
  }
});
```

## 7. UI Design And Outputs
- The user uploads an image.
- The system processes the image and determines its status.
- Results display affected area percentage, disease index, and diseased regions count.
- A visual indicator (emoji) represents the status.

## 8. Benefits of Project
- Helps farmers detect diseases early.
- Reduces dependency on expert inspections.
- Provides a cost-effective solution for monitoring plant health.

## 9. Conclusion
This project demonstrates an image-processing-based approach to plant disease detection. Future improvements may include integrating deep learning models for more accurate predictions.

## 10. Bibliography
- OpenCV documentation: https://docs.opencv.org/
- Vue.js documentation: https://vuejs.org/
- Flask documentation: https://flask.palletsprojects.com/

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/plant-disease-detection.git
   cd plant-disease-detection
   ```
2. Install dependencies:
   ```bash
   pip install flask opencv-python numpy scikit-image
   ```
3. Run the Flask server:
   ```bash
   python app.py
   ```
4. Open `index.html` in a browser to access the UI.


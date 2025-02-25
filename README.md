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
  <title>Plant Disease Detection</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>
<body>
  <div id="app" class="container mt-5">
    <h1 class="mb-4">Plant Disease Detection</h1>
    <form @submit.prevent="uploadImage">
      <div class="form-group">
        <label for="image">Upload a plant leaf image:</label>
        <input type="file" class="form-control-file" id="image" @change="handleFileUpload">
      </div>
      <button type="submit" class="btn btn-primary">Detect Disease</button>
    </form>
    <div v-if="result" class="mt-4">
      <h3>Result: {{ result.status }}
        <span v-if="result.status === 'Diseased'">&#x1F621;</span>
        <span v-else>&#x1F604;</span>
      </h3>
      <p><strong>Affected Area Percentage:</strong> {{ result.affected_area_percentage.toFixed(2) }}%</p>
      <p><strong>Disease Index:</strong> {{ result.disease_index.toFixed(2) }}</p>
      <p><strong>Number of Diseased Regions:</strong> {{ result.num_diseased_regions }}</p>
      <img :src="imageUrl" alt="Uploaded image" class="img-thumbnail" v-if="imageUrl">
    </div>
  </div>
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


# Plant Disease Detection

## Introduction
This project detects plant diseases by analyzing images of leaves. It utilizes OpenCV, NumPy, and Flask for backend processing, and Vue.js with Bootstrap for the frontend.

## Literature Survey
Plant diseases significantly impact agricultural productivity. Computer vision-based approaches help automate disease detection using image processing and machine learning techniques.

## Technical Requirements
- Python 3.x
- Flask
- OpenCV
- NumPy
- Vue.js
- Bootstrap

## Project Description
This system allows users to upload a leaf image, processes it using OpenCV, and determines if the plant is diseased based on detected features.

## System Design
1. **Frontend:** Vue.js & Bootstrap-based UI for user interaction.
2. **Backend:** Flask API processes the uploaded image and returns results.
3. **Image Processing:** OpenCV detects diseased regions.
4. **Output:** Displays disease status, affected area percentage, and an image preview.

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-repository/plant-disease-detection.git
cd plant-disease-detection
```

### 2. Install Dependencies
```bash
pip install flask opencv-python numpy
```

### 3. Run the Flask Server
```bash
python app.py
```
The server will start at `http://127.0.0.1:5000`

### 4. Open `index.html`
Open the HTML file in a browser or use a local server to serve static files.

## Source Code

### Backend (`app.py`)
```python
from flask import Flask, request, jsonify
import cv2
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    result = process_image(filepath)
    return jsonify(result)

def process_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    affected_area_percentage = np.mean(thresh) * 100 / 255.0
    disease_index = 1 - (affected_area_percentage / 100.0)
    status = 'Diseased' if disease_index > 0.5 else 'Healthy'
    return {
        "affected_area_percentage": affected_area_percentage,
        "disease_index": disease_index,
        "num_diseased_regions": 1,
        "status": status
    }

if __name__ == '__main__':
    app.run(debug=True)
```

### Frontend (`index.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Plant Disease Detection</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
</head>
<body>
    <div id="app" class="container mt-5">
        <h1>Plant Disease Detection</h1>
        <form @submit.prevent="uploadImage">
            <input type="file" class="form-control-file" @change="handleFileUpload">
            <button type="submit" class="btn btn-primary mt-2">Detect Disease</button>
        </form>
        <div v-if="result" class="mt-4">
            <h3>Result: {{ result.status }} <span v-html="result.status === 'Diseased' ? '⚠️' : '✅'"></span></h3>
            <p><strong>Affected Area:</strong> {{ result.affected_area_percentage }}%</p>
            <p><strong>Disease Index:</strong> {{ result.disease_index }}</p>
            <p><strong>Diseased Regions:</strong> {{ result.num_diseased_regions }}</p>
            <img :src="imageUrl" class="img-thumbnail" v-if="imageUrl">
        </div>
    </div>

    <script src="/static/js/app.js"></script>
</body>
</html>
```

### JavaScript (`app.js`)
```javascript
new Vue({
    el: '#app',
    data: {
        image: null,
        imageUrl: '',
        result: null
    },
    methods: {
        handleFileUpload(event) {
            this.image = event.target.files[0];
            this.imageUrl = URL.createObjectURL(this.image);
        },
        uploadImage() {
            let formData = new FormData();
            formData.append('image', this.image);
            fetch('/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => { this.result = data; })
            .catch(error => console.error('Error:', error));
        }
    }
});
```

## UI Design and Outputs
- **Simple Bootstrap-based form** for file upload.
- **Vue.js dynamic rendering** to show the results.
- **Emoji indicator** for disease status.

## Benefits of the Project
- Automated plant disease detection.
- Reduces manual inspection effort.
- Helps farmers and researchers in quick analysis.

## Conclusion
This project provides a simple yet effective way to detect plant diseases using image processing techniques.

## Bibliography
- OpenCV Documentation
- Vue.js Guide
- Flask Documentation
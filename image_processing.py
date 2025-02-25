import cv2
import numpy as np
from skimage import measure

def process_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return 'Error: Unable to read image.'
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Otsu Thresholding
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Calculate disease index
    disease_index = np.mean(thresh) / 255.0
    status = 'Diseased' if disease_index < 0.5 else 'Healthy'
    
    # Count the number of diseased regions
    labels = measure.label(thresh, connectivity=2, background=0)
    num_regions = len(np.unique(labels)) - 1  # Excluding background
    
    # Calculate percentage of diseased area
    total_pixels = thresh.size
    diseased_pixels = np.sum(thresh == 0)  # Black pixels in binary image
    affected_area_percentage = (diseased_pixels / total_pixels) * 100
    
    return {
        'status': status,
        'disease_index': disease_index,
        'num_diseased_regions': num_regions,
        'affected_area_percentage': affected_area_percentage
    }

# Example usage
result = process_image('leaf.jpg')
print(result)

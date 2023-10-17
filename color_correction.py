import cv2
import numpy as np

def correct_colors(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("L'image n'a pas pu être chargée.")
        return

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    hsv_image[:, :, 1] = hsv_image[:, :, 1] * 1.5  # Augmentation de 50% de la saturation

    # Reconvertir l'image en espace colorimétrique BGR
    corrected_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    # Enregistrement de l'image résultante
    cv2.imwrite("C:/Users/USER/Desktop/PC4/pc4_result.jpg", corrected_image)

if __name__ == "__main__":
    image_path = r'C:/Users/USER/image.jpg'  
    correct_colors(image_path)

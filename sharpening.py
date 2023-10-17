# sharpening.py
import cv2
import numpy as np

def sharpen_image(image_path):
    image = cv2.imread(image_path)

    # Algorithme d'amélioration de la netteté (exemple : filtre de renforcement)
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # Enregistrez l'image résultante
    cv2.imwrite("pc2_result.jpg", sharpened_image)

if __name__ == "__main__":
    image_path="C:/Users/User/3.jpg"
    sharpen_image(image_path)


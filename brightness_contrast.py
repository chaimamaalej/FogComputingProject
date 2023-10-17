import cv2


def adjust_brightness_contrast(image_path):
    # Charger l'image

    image = cv2.imread(image_path)
    # Appliquer l'algorithme
    if image is None:
        print(
            f"Erreur: Impossible de charger l'image à partir de {image_path}")
        return

    image = cv2.convertScaleAbs(image, alpha=1.5, beta=10)
    # Enregistrer l'image résultat
    cv2.imwrite("pc3_result.jpg", image)

    print("Ajustement de la luminosité et du contraste terminé. Image enregistrée sous pc3_result.jpg")


if _name_ == "_main_":
    image_path = "C:/Users/User/Desktop/PC3/image.jpg"
    adjust_brightness_contrast(image_path)
import cv2
import numpy as np
import os

# Dossier où se trouvent les images résultantes sur chaque PC client
result_folder = "C:\\wamp\\www\\uploads\\uploaded"

# Obtenez la liste des noms de fichiers des images résultantes
result_files = [os.path.join(result_folder, file) for file in os.listdir(result_folder) if file.endswith(".jpg")]

# Assurez-vous que vous avez récupéré des fichiers d'image
if not result_files:
    print("Aucun fichier d'image résultante n'a été trouvé dans le dossier.")
    exit()

# Charger les images résultantes depuis chaque PC client
images = [cv2.imread(file) for file in result_files]


for i in range(1, len(images)):
    if images[i].shape != images[0].shape:
        print("Toutes les images doivent avoir la même taille.")
        exit()

# Fusionnez les images en calculant la moyenne de chaque pixel
result_image = np.mean(images, axis=0).astype(np.uint8)

# Enregistrez l'image finale
cv2.imwrite("C:\\wamp\\www\\uploads\\uploaded\\final_result.jpg", result_image)

from PIL import Image
import matplotlib.pyplot as plt

def hola():
    print("Que pasa tron")

def visualize():
    img = Image.open("C:\Users\domin\Desktop\Brain-Tumor-Semantic-Segmentation\Brain-Tumor-Semantic-Segmentation\data\train\2_jpg.rf.fded76c07e967829600f3509288fdfe0.jpg")
    plt.imshow(img)
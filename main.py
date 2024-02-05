from PIL import Image
import matplotlib.pyplot as plt

def hola():
    print("Que pasa tron")

def visualize(path):
    img = Image.open(path)
    plt.imshow(img)
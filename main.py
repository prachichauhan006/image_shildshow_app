import tkinter as tk 
import time 
from PIL import Image, ImageTk

# Main window 
root = tk.Tk()
root.title("photo slideshow album")
root.geometry("900x900")

# list of image paths

image_paths = [
    
    r"C:\Users\prach\Downloads\web2.webp",
    r"C:\Users\prach\Downloads\web3.webp",
            
]

image_size = (700, 700)
images = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize(image_size)
    images.append(img)
    
# convertt PIL images into tkinter compatible image 
final_images = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)
    
# label widget to keep images

image_label = tk.Label(root)
image_label.pack(pady = 30)

#slideshow function

def start_slideshow():
    for photo in final_images:
        image_label.config(image = photo)
        image_label.image = photo
        root.update()
        time.sleep(3)
        
#button 
play_button = tk.Button(
    root,
    text = "Play the slideshow",
    font = ("Arial", 40),
    command = start_slideshow
)


play_button.pack(pady= 40)

root.mainloop()
#Replace your-device-ID-goes-here with your actual device ID
#and replace your-access-token-goes-here with your actual access token

#Importing libraries 
from tkinter import *
import tkinter.font
from tkinter import filedialog
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os


#initilising tkinter GUI
win = Tk()

#Image size according to imported model 
img_width, img_height = 224, 224

#loading and compiling the model
model = load_model('covid19.model')
model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])


#Function that ask the user to input an image and then make predction from the model
def UploadPhoto():
    
    root = Tk()
    root.withdraw()
    
    #Ask the user to open a file    
    file_path = filedialog.askopenfilename(title = "Select a photo")
    
    #Resizing the image to fit the model and convert the image to array
    img = image.load_img(file_path, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    
    #Stack the array vertically
    images = np.vstack([x])

    #predicting the input image from the model
    classes = model.predict(images, batch_size=10)
    
    #Find largest predicted probability
    final = np.argmax(classes)
        
    #Test positive call function online with an argument 1  
    if final == 1:
        os.system('curl https://api.particle.io/v1/devices/your-device-ID-goes-here/covidtest -d access_token=your-access-token-goes-here -d "args=1"')


    #Test negative call function online with an argument 0
    else:
        os.system('curl https://api.particle.io/v1/devices/your-device-ID-goes-here/covidtest -d access_token=your-access-token-goes-here -d "args=0"')

#Function to close the GUI  
def close():
    win.destroy()


#Creating the GUI 
win.title("Detecting Covid-19 from an x-ray image | Moe Hdaib")
myfont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")


photoButton = Button(win, text = "Upload a photo", font = myfont, command= UploadPhoto, bg = '#2E86C1', height = 1, width = 25)
photoButton.grid(row=1, column =0)

exitButton = Button(win, text = "Exit", font = myfont, command= close, bg = '#A93226', height = 1, width = 10)
exitButton.grid(row=2, column =0)

canvas = Canvas(win, width=500, height=500)
canvas.grid(row=0, column =0)

canvas.create_text(250,20, text="Moe Hdaib - 218388869", font=("Courier", 27))
canvas.create_text(250,60, text="SIT210", font=("Courier", 27))

canvas.create_text(250,400, text="Upload an x-ray chest image from the upload button", font=("Courier", 12))
canvas.create_text(250,430, text="and wait for the LED lights for results.", font=("Courier", 12))




win.mainloop()
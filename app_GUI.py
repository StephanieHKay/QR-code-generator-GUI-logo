import pyqrcode      #to create qr png files
from tkinter import *     #import everything to create basic GUI
from PIL import Image #to add central logo

#general central logo
import requests
from io import BytesIO


#create GUI title
root = Tk()
root.title("QR Code Generator")

#ensure GUI central method
window_width =350
window_height = 250
root.geometry(f'{window_width}x{window_height}')
root.eval('tk::PlaceWindow . center')

#label
lb=Label(root, text="Enter a link to generate a QR code")
lb.grid(row=0, padx=40)
lb2=Label(root, text="Save this QR code as?")
lb2.grid(row=2, padx=40)
lb3=Label(root, text="Add a central logo into the QR code?\nPaste image web link")
lb3.grid(row=4, padx=40)

#input field
entry_variable = StringVar()
Entry(root, textvariable=entry_variable).grid(row=1, padx=20, pady=5)

entry_variable2 = StringVar()
Entry(root, textvariable=entry_variable2).grid(row=3, padx=20, pady=5)

entry_variable3 = StringVar()
Entry(root, textvariable=entry_variable3).grid(row=5, padx=20, pady=5)


#button - on clicking will input weblink and name(without spaces) and generate code with title and size
def clicked():    
    input_string = entry_variable.get()
    input_string2 = entry_variable2.get()
    input_string2= input_string2.replace(" ", "_")
    url=pyqrcode.create(input_string)
    logo_link = entry_variable3.get().strip()
    if len(logo_link)<=4:
         url.png(f"{input_string2}_SKH_QR.png", scale=12, module_color='#000087')
         print("New QR code generated")
    
    elif len(logo_link) > 4:   
        with open(f"{input_string2}_SKH_QR.png", "wb") as generatedQ:
            url.png(generatedQ, scale=12, module_color='#000087')
          
        img= Image.open(f"{input_string2}_SKH_QR.png")
        width, height = img.size
        img=img.convert("RGBA")
        logo_size = 80

        response = requests.get(logo_link)
        logo = Image.open(BytesIO(response.content))

            
        #covert logo to RGBA format
        new_logo = logo.convert("RGBA")
      
    
        #determine logo position within QR code
        xmin = ymin = int((width / 2) - (logo_size / 2))        
        xmax = ymax = int((width / 2) + (logo_size / 2))
              
        new_logo = new_logo.resize((xmax - xmin, ymax - ymin))
        
        #paste logo into centre of QR code using logo as transparency mask
        img.paste(new_logo, (xmin, ymin, xmax, ymax), new_logo)
        img.show()   
        img.save(f"{input_string2}_SKH_QR.png")
        print("New QR code generated")


Button(root, text= "Get my QR code",command=clicked).grid(row=6, padx=20, pady=30)

#execute tkinter
root.mainloop()

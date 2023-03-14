from fastapi import FastAPI, Request, Form
from main.caeser_cracker import CaeserCracker
from fastapi.templating import Jinja2Templates
import schedule
import time


app = FastAPI()    #Creating a FastAPI instance
templates = Jinja2Templates(directory="templates/") #Creating a template object with the .html file in templates directory

@app.get("/")
def form_post(request: Request):
    
    return templates.TemplateResponse('first_page.html', context ={'request':request}) # Returning the template response on application launch

@app.post("/")
def form_post(request: Request, e_message : str = Form(None), message : str = Form(None), key : int = Form(None), crypt : str = Form(None)):
    
    if (crypt == 'Encrypt' and message != None and key!= None):   
        
        #If the user clicks on the Encrypt button, create a CeaserCracker object and call the caeser_cipher() method to encrypt the message,
        #based on the provided key

        Ceaser_obj = CaeserCracker(message,key)
        encrypted_message = Ceaser_obj.caesar_cipher()
        return templates.TemplateResponse('first_page.html', context ={'request':request, 'cc_message':encrypted_message}) 
    
    elif (e_message != None):

        #If the user clicks on the Decrypt button, create a CeaserCracker object and call the caeser_decipher() method to decrypt the message,
        #using 'brute force attack'
        Ceaser_obj = CaeserCracker(e_message, shift = 0)
        decrypted_message = Ceaser_obj.caesar_decipher()
        return templates.TemplateResponse('first_page.html', context ={'request':request, 'd_message':decrypted_message})
    
    else:
        return templates.TemplateResponse('first_page.html', context ={'request':request, 'message': " ***Please do not keep any field empty while using encryption or decryption*** "})




    
  
        
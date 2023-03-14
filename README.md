# Caeser-Cracker
This app which demonstrates "brute force attack" in cryptography, allows the user to enter an encrypted message (Ceaser cypher encryption) and then displays the most relevant decrypted information. It uses the "pyspellchecker" package of python to select the most human understandable information from a list of all (26) possible decrypted messages. The User has the option to enter their own encrypted message or simply use the encryption feature in the app to create one.
 
Instructions for usage:

Clone or download the repository

Navigate to "/Caeser_Cracker" directory and run the command "pip install -r requirements.txt" to install the dependencies

Run the command "python -m uvicorn main.app:app --reload" to launch the application

Navigate to the link "http://127.0.0.1:8000" to use the application

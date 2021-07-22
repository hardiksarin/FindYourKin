import json
from flask import Flask,jsonify
from flask import request
import pymongo
from pymongo import MongoClient
import RegisterUser
import FindUser

app =Flask(__name__)

@app.route('/ping')
def Ping_Server():
    return("Server Functioning Normally!")



@app.route('/RegisterUser', methods=['Post'])
def Register_User():
    try:
        User_Data = request.json
        RegisterUser.InsertClient(User_Data['missing_people'][0]['mp_id'],User_Data['missing_people'][0]['mp_name'],
        User_Data['missing_people'][0]['age'],User_Data['missing_people'][0]['gender'],User_Data['missing_people'][0]['mp_contact'],
        User_Data['missing_people'][0]['mp_address'],User_Data['missing_people'][0]['mp_physicalAppearance'],User_Data['missing_people'][0]['image_matrix']
        )
        return("User Registred Succesfully")
    except:
          raise Exception("Sorry, Missing Person Can't be Registred")

@app.route('/FindUser', methods=['Post'])
def Find_User():
    try:
        User_Data = request.json
        a = FindUser.FindClient(User_Data['image_matrix'])
        aadhar_json = json.dumps(a)
        return(aadhar_json)
    except:
          raise Exception("Sorry, Missing Person Can't be Found")

    

    
app.run(host='0.0.0.0', port=5000)
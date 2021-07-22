from os import path
import os
from deepface.basemodels import Facenet
import pymongo
import MongoConnection
import base64 
import shutil
from deepface import DeepFace

##Insert Clients
def InsertClient(Aadhar,Name,Age,Sex,Contact,Address,PhysicalAppearance,ImgPath):
    myclient = client = pymongo.MongoClient("mongodb+srv://aman:baman@cluster0.xmegs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mydb = myclient["mydatabase"]
    mycol = mydb["MISSPER"]
    png_recovered = base64.b64decode(ImgPath)
    f = open(f'{Aadhar}.jpg', "wb")
    f.write(png_recovered)
    f.close()

    

    embeddings =  MongoConnection.Embedd(path.abspath("temp.jpg"))
    mydict = { "_id":Aadhar, "mp_name": Name,"age":Age ,"gender":Sex,"mp_contact":Contact,"mp_address": Address,
    "mp_physicalAppearance":PhysicalAppearance  ,"embedding":embeddings}
    shutil.copy(f'{Aadhar}.jpg', '/home/ubuntu/kin/FindYourKin/Test/Test')
    try:
        os.remove("C:\\Users\\sarin\\Music\\KIN\\Test\\representations_facenet.pkl")
        DeepFace.find(img_path = path.abspath("temp.jpg"), db_path = "C:\\Users\\sarin\\Music\\KIN\\Test", model_name = "Facenet")

        x = mycol.insert_one(mydict)
        return(x)

    except:
        DeepFace.find(img_path = path.abspath("temp.jpg"), db_path = "C:\\Users\\sarin\\Music\\KIN\\Test", model_name = "Facenet")
        x = mycol.insert_one(mydict)
        return(f'MISSPER Already Registred with id : {Aadhar}')






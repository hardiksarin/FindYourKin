from os import path
import deepface
from deepface import DeepFace
import pymongo
import base64 
import shutil
import MongoConnection
from pathlib import Path
def FindClient(ImgPath):
    myclient = pymongo.MongoClient("mongodb+srv://aman:baman@cluster0.xmegs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mydb = myclient["mydatabase"]
    mycol = mydb["MISSPER"]
    png_recovered = base64.b64decode(ImgPath)
    f = open(f'temp.jpg', "wb")
    f.write(png_recovered)
    f.close()
    df = DeepFace.find(img_path = path.abspath("temp.jpg"), db_path = "/home/ubuntu/kin/FindYourKin/Test", model_name = "Facenet")
    dl = df['identity'].tolist()
    identities = []
    for i in dl:
        identities.append(Path(i).stem)

    jsons = {}
    for i in identities:
        a = mycol.find({"_id":f'{i}'})
        for j in a:
            jsons[i] = j
    return(jsons)
  
    
    



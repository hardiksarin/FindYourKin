# from pymongo import MongoClient
import os 
from deepface import DeepFace
import deepface
from tensorflow.python.ops.gen_data_flow_ops import PriorityQueue
# connection = "mongodb://127.0.0.1:27017"
 
# client = MongoClient(connection)
 
# database = 'deepface'; 
# collection = 'deepface'
 #"VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"

# for model in models:
# #    result = DeepFace.verify("img1.jpg", "img2.jpg", model_name = model)
#    obj = DeepFace.analyze(img_path = IMG1_PATH, actions = ['age', 'gender', 'race', 'emotion'])

# #    df = DeepFace.find(img_path = IMG1_PATH, db_path = IMG2_PATH, model_name = model,enforce_detection=False,distance_metric="euclidean_l2")
#    print(obj["age"]," years old ",obj["dominant_race"]," ",obj["dominant_emotion"]," ", obj["gender"])
def Embedd(Path1):
    obj = DeepFace.represent(Path1, model_name = 'Facenet')
    return(obj)



    




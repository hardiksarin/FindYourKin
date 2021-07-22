import requests
import os
import base64


from random import randint
from IndianNameGenerator import *

# def random_with_N_digits(n):
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)
# directory = 'C:\\Users\\sarin\\Music\\KIN\\TestDB'
# for filename in os.listdir(directory):
#     f = os.path.join(directory, filename)
#     # checking if it is a file
#     if os.path.isfile(f):
#       with open(f, "rb") as img_file:
#          imgfile64 = base64.b64encode(img_file.read())
url = 'http://192.168.0.4:5000/RegisterUser'
# myobj = {
#    "missing_people":[
#       {
#          "mp_id": random_with_N_digits(12),
#          "mp_name":randomPunjabi(),
#          "age": 29,
#          "gender": "male",
#          "mp_contact":"8963055884",
#          "mp_address":"kanpur",
#          "mp_physicalAppearance":{
#             "color_of_clothes":"blue",
#             "heigt":6.4,
#             "weight":15.0,
#             "height_characteristics":[],
#             "body_type":[],
#             "complexion":[],
#             "hair_charachteristics":[]
#          },
#          "image_matrix":"imgfile64"
#       }
#    ]
# }
myobj = {
   "missing_people":[
      {
         "mp_id": "123232323",
         "mp_name":randomPunjabi(),
         "age": 29,
         "gender": "male",
         "mp_contact":"8963055884",
         "mp_address":"kanpur",
         "mp_physicalAppearance":{
            "color_of_clothes":"blue",
            "heigt":6.4,
            "weight":15.0,
            "height_characteristics":[],
            "body_type":[],
            "complexion":[],
            "hair_charachteristics":[]
         },
         "image_matrix":"imgfile64"
      }
   ]
}
print(myobj)
x = requests.post(url,json=myobj)

print(x.text)


      
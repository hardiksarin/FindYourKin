
from traceback import print_tb
from deepface import DeepFace
import pandas as pd
df = DeepFace.find(img_path = "temp.jpg", db_path = "C:\\Users\\sarin\\Music\\KIN\\TestDB")
print(df)
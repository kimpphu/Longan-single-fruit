from roboflow import Roboflow
import os

SECRET_KEY = os.environ.get("SECRET_KEY")
rf = Roboflow(api_key=SECRET_KEY)
project = rf.workspace("bda").project("longan-single-fruit-counting")
dataset = project.version(1).download("yolov8", location="datasets")



from flask import *
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from app import app



prediction_key = "c5ef913d5b3d473a8cfb7a83d1f67006"
publish_iteration_name = "drunk"
ENDPOINT = "https://sober.cognitiveservices.azure.com"
projectId = "b44187a6-7620-43d0-8266-ece7d1988f68"
# prediction_key = "your-prediction key"
# publish_iteration_name = "classifyModel"
# ENDPOINT = "your-endpoint"
# projectId = "your project id"

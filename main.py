#the modules

from urllib import response
import requests


#the constants

WORKOUT_ID = "5ea00b72"
WORKOUT_KEY= "dc2ad9c047d8e54ccc01842889623cc7"
WORKOUT_END="https://trackapi.nutritionix.com/v2/natural/exercise"

#user input in simple language

gender=input("Enter your gender: ")
age=int(input("Enter your age: "))
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in cm: "))
user_input=input("Enter what exercise you did: ")

#making the request

params={"query":user_input,"gender":gender.lower(),"age":age,"weight_kg":weight,"height_cm":height}
headers={"x-app-id":WORKOUT_ID,"x-app-key":WORKOUT_KEY,"x-remote-user-id":"0"}
response=requests.post(url=WORKOUT_END,json=params,headers=headers)
print(response.json())


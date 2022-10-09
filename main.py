# from playsound import playsound

# playsound("C:\\Users\\USER\\Desktop\\diagnosis\\introaudio.mp3")




symptoms = {
    "allergies": "eye irritation, runny nose, stuffy nose, puffy watery eye",
    "cold":"really cold",
    "diarrhea":" yeah diarrhea",
    "headaches":"",
    "stomach aches": ""
}

illness = str(input("Enter allergies, cold, diarrhea, headaches,stomach aches \n"))

print(symptoms[illness])


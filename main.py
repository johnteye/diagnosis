# from playsound import playsound
# playsound('C:\\Users\\USER\\Desktop\\diagnosis\\introaudio.mp3')


allergies_symptoms = ['eye irritation', 'runny nose', 'stuffy nose', 'puffy eyes', 'watery eyes', 'sneezing', 'inflamed throat', 'itchy nose']

allergies_causes = ['foods(nuts, eggs, milk, soy, shellfish, wheat)', 'pollen', 'mold', 'latex', 'pet dander']

allergies_treatment = ['Antihistamines', 'Decongestants', 'Anti-inflammatory agents', 'allergy shots']

cold_flu_symptoms = ['fever', 'headache', 'fatigue', 'dry cough', 'runny nose', 'stuffy nose', 'sore throat', 'cough', ]

cold_flu_causes = ['inflammation fo the membranes in the nose and throat']

cold_flu_treatment = ['drink lots of fluids', 'eat a well-balanced diet', 'seek prescriptions for antiboitics']

diarrhea_symptoms = ['watery stools', 'frequent bowels', 'nausea', 'bloating', 'abdomenal pains', 'fever', 'bloody stools']

diarrhea_causes = ['bacterial infection', 'viral infection', 'stress or panic attacks', 'food intolerance', 'menstrual cramps']

diarrhea_treatment = ['do not drink clear liquids for 24hrs', 'avoid caffeine and alcohol', 'avoid milk-based or very sweet foods']

malaria_symptoms = ['fever', 'chills', 'tiredness', 'headache', 'nausea', 'vomiting', 'diarrhea']

malaria_causes = ['mosquito bites', 'organ transplant', 'a transfusion']

malaria_treatment = ['antimalaria drugs']


user_symptoms = input("Enter your symptoms? \n").split(",")
print(user_symptoms)
if set(user_symptoms).issubset(set(allergies_symptoms)):
    print("Likely to have allergic reactions")
else:
    print("Likely to have cold or flu")

from __future__ import print_function
from playsound import playsound
from ast import Break

allergies_symptoms = ['eye irritation', 'runny nose', 'stuffy nose', 'puffy eyes', 'watery eyes', 'sneezing', 'inflamed throat', 'itchy nose']

allergies_causes = ['foods(nuts, eggs, milk, soy, shellfish, wheat)', 'pollen', 'mold', 'latex', 'pet dander']

allergies_treatment = ['Antihistamines', 'Decongestants', 'Anti-inflammatory agents', 'allergy shots']

cold_flu_symptoms = ['fever', 'headache', 'fatigue', 'dry cough', 'runny nose', 'stuffy nose', 'sore throat', 'cough', ]

cold_flu_causes = ['inflammation of the membranes in the nose and throat']

cold_flu_treatment = ['drink lots of fluids', 'eat a well-balanced diet', 'seek prescriptions for antiboitics']

diarrhea_symptoms = ['watery stools', 'frequent bowels', 'nausea', 'bloating', 'abdomenal pains', 'fever', 'bloody stools']

diarrhea_causes = ['bacterial infection', 'viral infection', 'stress or panic attacks', 'food intolerance', 'menstrual cramps']

diarrhea_treatment = ['do not drink clear liquids for 24hrs', 'avoid caffeine and alcohol', 'avoid milk-based or very sweet foods']

malaria_symptoms = ['fever', 'chills', 'tiredness', 'headache', 'nausea', 'vomiting', 'diarrhea']

malaria_causes = ['mosquito bites', 'organ transplant', 'a transfusion']

malaria_treatment = ['antimalaria drugs']


print(''' 

 ______  _________ _______  _______  _        _______  _______ _________ _______ 
(  __  \ \__   __/(  ___  )(  ____ \( (    /|(  ___  )(  ____ \\__   __/(  ____ \
| (  \  )   ) (   | (   ) || (    \/|  \  ( || (   ) || (    \/   ) (   | (    \/
| |   ) |   | |   | (___) || |      |   \ | || |   | || (_____    | |   | (_____ 
| |   | |   | |   |  ___  || | ____ | (\ \) || |   | |(_____  )   | |   (_____  )
| |   ) |   | |   | (   ) || | \_  )| | \   || |   | |      ) |   | |         ) |
| (__/  )___) (___| )   ( || (___) || )  \  || (___) |/\____) |___) (___/\____) |
(______/ \_______/|/     \|(_______)|/    )_)(_______)\_______)\_______/\_______)
                                                                                 ''')
playsound('C:\\Users\\USER\\Desktop\\diagnosis\\introaudio.mp3')

user_symptoms = input("Enter your symptoms? \n").split(",")


# def knowCauses(disease):
#     know_causes = input(f"Would you like to know the causes of {disease} \n Y/N: ")
#     if know_causes == "Y":
#         print(malaria_causes)
#     else:
#         Break()





if set(user_symptoms).issubset(set(allergies_symptoms)):
    print("Likely to have allergic reactions")
    know_causes = input("Would you like to know the causes of allergic reactions \n Y/N: ")
    if know_causes == "Y":
        print(*allergies_causes,sep='\n')
    else:
        Break()
    know_treatment = input("Would you like to know the treatment of allergic reactions \n Y/N: ")
    if know_treatment == "Y":
        print(*allergies_treatment,sep='\n')
    else:
        Break()
    
elif set(user_symptoms).issubset(set(cold_flu_symptoms)):
    print("Likely to have cold or flu")
    know_causes = input("Would you like to know the causes of cold and flu \n Y/N: ")
    if know_causes == "Y":
        print(*cold_flu_causes,sep='\n')
    else:
        Break()

    know_treament = input("Would you like to know the treatment of cold and flu \n Y/N: ")
    if know_treament == "Y":
        print(*cold_flu_treatment,sep='\n')
    else:
        Break()


elif set(user_symptoms).issubset(set(diarrhea_symptoms)):
    print("Likely to have diarrhea")
    know_causes = input("Would you like to know the causes of diarrhea \n Y/N: ")
    if know_causes == "Y":
        print(*diarrhea_causes,sep='\n')
    else:
        Break()

    know_treament = input("Would you like to know the treatment of diarrhea \n Y/N: ")
    if know_treament == "Y":
        print(*cold_flu_treatment,sep='\n')
    else:
        Break


elif set(user_symptoms).issubset(set(malaria_symptoms)):
    print("Likely to have malaria")
    know_causes = input("Would you like to know the causes of malaria \n Y/N: ")
    if know_causes == "Y":
        print(*malaria_causes,sep='\n')
    else:
        Break()
    

    know_treament = input("Would you like to know the treatment of malaria \n Y/N: ")
    if know_treament == "Y":
        print(*malaria_treatment,sep='\n')
    else:
        Break()
else:
    print("Consult a Doctor")


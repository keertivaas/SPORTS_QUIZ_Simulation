from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image
import requests
from io import BytesIO

subscription_key = "4cd80ea06718484bace4a11cc08cc561"
client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))

quiz = {"Who are famous for the chant '49 undefeated' ?" : "Arsenal",
         "Where was 2018 FIFA Worldcup held?" : "Russia",
         "Didier Drogba played for which PL Team? " : "Chelsea",
         "Which club is nicknamed 'The toffees' ? " : "Everton",
         "Which Manager is famous for 'Third Season Syndrome' ?" : "Jose Mourinho",
         "Who recently became the world's most expensive goalkeeper? " : "Kepa Arrizabalaga",
         "Name the passing type possession game invented by Barca : " : "Tiki Taka",
         "Name the martial art form turned footbal style used by Brazilians during the Pele era. " : "Joga Bonito" ,
         "Against which team did Robert Lewandowski score 5 goals in 9 minutes ? " : "Wolfsburg",
         "Eden Hazard, Romelu Lukaku and Kevin de Bruyne play for which Country ? " : "Belgium",
         "Which PL team's owner recently passed away in a Helicopter crash? " : "Leicester City" ,
         "Which PL team is famous for Pressing style of football? " : "Liverpool",
         "Who is the current Real madrid Manager?" : "Santiago Solari",
         "Cristiano Ronaldo currently plays for which football team? " : "Juventus",
         "Which team has the home ground Anfield? " : "Liverpool",
         "Which team has the home ground Old Trafford? " : "Manchester United",
         "Which was the first team to win the Premier League on Goal difference?" : "Manchester City",
         "For which team did Pep Guardiola play? " : "Barcelona",
         "What is the famous clash between Barcelona and Real Madrid called as?" : "El clasico",
         "Liverpool and which team play the Merseyside derby?" : "Everton"}

def topic_quiz(topic):
    qno = 1
    score=0
    quiz_tuple = tuple(topic.items())
    for field in quiz_tuple:
        question, answer = field
        csp=1
        for i in answer:
            if i==' ':
                csp+=1
        print("{0}. {1} \n Hint : No of letters : {2}\n No of words : {3}".format(qno, question, len(answer)- (csp-1),csp))
        userans = input()
        qno+=1
        if answer.lower() == userans.lower():
            print("Correct answer.")
            score+=1
        else:
            print("Incorrect answer.")

        search_term = answer
        image_results = client.images.search(query=search_term)

        if image_results.value:
            image_result = image_results.value[0]
        else:
            print("No image results returned!")

        url=image_result.thumbnail_url
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.show()


    print("\nTotal score : {}".format(score))
    return

print("\nWelcome to the Quiz!! It is about Football and would require your guessing of one or 2 words.")
print("Certain clues will be provided. After you answer, the image of the correct answer will be displayed.")
print("\nSo let's do this...")
input()

topic_quiz(quiz)    




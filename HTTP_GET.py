import requests

def getTopicCount(topic):
    response = requests.get(f"https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page={topic}")
    if response.ok == True:
        reponse_Text = response.text

        number_of_times_article =0
        for word in reponse_Text:
            if topic in reponse_Text:
                number_of_times_article += 1

        page_source_json_format = response.json()
        
        page_source_json_format['parse']['title']
        pageId_webpage = page_source_json_format['parse']['pageid']

    return number_of_times_article

getTopicCount("pain")


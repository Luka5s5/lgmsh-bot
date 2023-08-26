import requests

def get_temp():

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":"Omsk"}

    headers = {
	"X-RapidAPI-Key": "c445daea10msh5b5ff9b7eb43209p1d9b0fjsn532338796b01",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()['current']['temp_c']

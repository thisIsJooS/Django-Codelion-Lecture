from django.shortcuts import render
import requests
import json

my_id = '3e8fec258632c29ded041b22fa92dfea'

def home(request):
    url = f'https://api.themoviedb.org/3/trending/all/day?api_key={my_id}'
    response = requests.get(url)

    resdata = response.text
    obj = json.loads(resdata) # json 객체를 파이썬 객체로 변환
    obj = obj['results']
    
    return render(request, 'index.html', {'obj': obj})
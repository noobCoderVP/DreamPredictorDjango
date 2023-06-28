from django.shortcuts import render
import json
import os

# Create your views here.


def readJson():
    infile = open(os.path.dirname(__file__) + '\db.json', 'r')
    matches = json.load(infile)
    matches = matches['data']['matchList']
    print(type(matches))
    matches.sort(key=lambda x: x['dateTimeGMT'])
    return matches


def Matches(request):
    matches = readJson()
    return render(request, 'matches.html', {'matches': matches})
    # c75f8952-74d4-416f-b7b4-7da4b4e3ae6e

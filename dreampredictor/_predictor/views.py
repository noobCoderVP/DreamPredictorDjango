from django.shortcuts import render
import os
import json

import numpy as np
import pandas as pd
import math
from sklearn.linear_model import LinearRegression
# Create your views here.


def Predictor(request):
    ID = request.GET.get('id', '')
    m = {'494e1d55-324c-42ee-850b-8de25f27f547': ['DC', 'GT'],
         '08629a55-7d6e-4b82-8157-10c1d1eb4d02': ['CSK', 'LSG']}

    if ID not in m.keys():
        return render(request, 'predictor.html', {'predictions': []})
    else:
        squads = open(os.path.dirname(__file__) + '\squads.json', 'r')
        squads = json.load(squads)

        players = open(os.path.dirname(__file__) + '\players.json', 'r')
        players = json.load(players)

        team1 = squads[m[ID][0]]
        team2 = squads[m[ID][1]]

        df = pd.read_csv(os.path.dirname(__file__) + '\data.csv', sep='\t')
        X = df[['first', 'second', 'third', 'fourth', 'fifth']]
        X = X.values
        Y = df['final']
        Y = Y.values

        regr = LinearRegression()
        regr.fit(X, Y)

        predictions = []

        for i in team1:
            predictions.append({
                'name': i,
                'score': math.floor(regr.predict(np.array(players[i]).reshape(1, -1)))
            })

        for i in team2:
            predictions.append({
                'name': i,
                'score': math.floor(regr.predict(np.array(players[i]).reshape(1, -1)))
            })

        predictions.sort(key=lambda x: x['score'], reverse=True)
        for i in range(len(predictions)):
            predictions[i]['SR'] = i + 1

        return render(request, 'predictor.html', {'predictions': predictions})

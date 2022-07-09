import pandas as pd
from flask import Flask
from flask import render_template, request
import DL_model


app = Flask(__name__)

@app.route('/')
@app.route('/PUBG')
def win_perc():
    heals = request.args.get('heals') # 뒤의 string heals는 html에서 label for에 들어가는 친구
    boosts = request.args.get('boosts')
    totalKills = request.args.get('totalKills')
    totalDistance = request.args.get('totalDistance')
    teamSize = request.args.get('teamSize')

    if heals == None:
        return render_template('PUBG.html', Output = '')

    input = pd.DataFrame({
        'heals': [float(heals)],
        'boosts': [float(boosts)],
        'totalKills': [float(totalKills)],
        'totalDistance': [float(totalDistance)],
        'teamSize': [float(teamSize)]
    })

    model_output = DL_model.model.predict(input)[0][0]

    return render_template('PUBG.html', Output = model_output)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
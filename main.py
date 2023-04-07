from flask import Flask, render_template, request
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import psycopg2

from db_models import ProductionData  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://raymond_user:uTjEw5jK2Ks2@iot-data.cn3ljizzlmy8.ap-south-1.rds.amazonaws.com:5432/raymond_plant_performance'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    try:
        db.session.execute('SELECT 1')
        return 'Connection successful!'
    except:
        return 'Connection failed.'

@app.route('/upload', methods=['POST'])
def upload():    
    file = request.files['file']   
    sheet_name = request.form['sheet_name']
    df = pd.read_excel(file, sheet_name=sheet_name)   
    for index, row in df.iterrows():
      data = ProductionData(
          date=row['Date'],
          total_steam=row['Total Steam'],
          finishing=row['Finishing'],
          weaving=row['Weaving'],
          recombing=row['Recombing'],
          grey_combing=row['Grey Combing'],
          dyeing=row['Dyeing'],
          spinning=row['Spinning'],
          sludge_drier=row['Sludge Drier'],
          ws=row['W/S'],
          pc_dyg=row['Pc Dyg'],
          tfo=row['TFO'],
          steaming_mc=row['Steaming m/c'],
        #   unmetered=row['Unmetered'],
          unmetered_percentage=row['Unmetered %age'],
          dm_water=row['DM Water'],
          recovery_percentage=row['Recovery %']
      )
      print(data)
    table = df.to_html(classes='table table-striped')    
    return render_template('table.html', table=table)

if __name__ == '__main__':
    app.run(debug=True)

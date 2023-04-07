from flask import Flask, render_template, request
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_models import db,ProductionData  

engine = create_engine('http://iot-data.cn3ljizzlmy8.ap-south-1.rds.amazonaws.com/raymond_vapi_plant_performance')

# create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
          unmetered=row['Unmetered'],
          unmetered_percentage=row['Unmetered %age'],
          dm_water=row['DM Water'],
          recovery_percentage=row['Recovery %']
      )
      session.add(data)
      session.commit()
      session.close()
    table = df.to_html(classes='table table-striped')    
    return render_template('table.html', table=table)

if __name__ == '__main__':
    app.run(debug=True)

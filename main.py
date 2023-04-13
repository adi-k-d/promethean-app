from flask import Flask, jsonify,request,render_template
from db_models import db,SteamConsumption,WaterConsumption
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
import pandas as pd
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://adityakd:59XrsGxjZKfNrGw9@appsmith.sensomak.com:5432/raymond_vapi_plant_performance'
db.init_app(app)
DB_URI = 'postgresql://adityakd:59XrsGxjZKfNrGw9@appsmith.sensomak.com:5432/raymond_vapi_plant_performance'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine('postgresql://adityakd:59XrsGxjZKfNrGw9@appsmith.sensomak.com:5432/raymond_vapi_plant_performance')
Session = sessionmaker(bind=engine)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/steam_consumption')
def get_steam_consumption():
    steam_data = SteamConsumption.query.all()
    results = [
        {
            'id': data.id,
            'date': datetime.strptime(data.date.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'),
            'total_steam': data.total_steam,
            'finishing': data.finishing,
            'weaving': data.weaving,
            'recombing': data.recombing,
            'grey_combing': data.grey_combing,
            'dyeing': data.dyeing,
            'spinning': data.spinning,
            'sludge_drier': data.sludge_drier,
            'w_s': data.w_s,
            'pc_dyg': data.pc_dyg,
            'tfo': data.tfo,
            'steaming_m_c': data.steaming_m_c,
            'unmetered': data.unmetered,
            'unmetered_percentage': data.unmetered_percentage,
            'dm_water': data.dm_water,
            'recovery_percentage': data.recovery_percentage
        } for data in steam_data]
    return jsonify(results)


@app.route('/steam_consumption/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Retrieve the uploaded file from the form data
        file = request.files['file']
        
        # Parse the Excel file using a library like Pandas
        
        df = pd.read_excel(file, sheet_name='MAIN')
        
        # Open a database session and bulk-insert the data into the SteamConsumption table
        session = Session()
        for _, row in df.iterrows():
            if not pd.isna(row['Date']):
                steam_consumption = SteamConsumption(
                    # date=datetime.strptime(row['Date'], "%y-%m-%d").strftime("%Y-%m-%d %H:%M:%S"),
                    date=row['Date'], 
                    total_steam=row['Total Steam'],
                    finishing=row['Finishing'],
                    weaving=row['Weaving'],
                    recombing=row['Recombing'],
                    grey_combing=row['Grey Combing'],
                    dyeing=row['Dyeing'],
                    spinning=row['Spinning'],
                    sludge_drier=row['Sludge Drier'],
                    w_s=row['W/S'],
                    pc_dyg=row['Pc Dyg'],
                    tfo=row['TFO'],
                    steaming_m_c=row['Steaming m/c'],
                    unmetered=row['Unmetered '],
                    unmetered_percentage=row['Unmetered %age'],
                    dm_water=row['DM Water'],
                    recovery_percentage=row['Recovery %']
                )
                session.add(steam_consumption)
        session.commit()
        session.close()
        
    # Render the upload form template
    return render_template('upload.html')

@app.route('/water_consumption')
def get_water_consumption():
   water_data = WaterConsumption.query.all()
   results = []
   if len(water_data) == 0:  # check if there are no results
       return jsonify(results)  # return empty list if there are no results
   else:
       data = []
       for row in water_data:
           row_dict = {}
           for column in row.__table__.columns:
               row_dict[column.name] = str(getattr(row, column.name))
           data.append(row_dict)
       return jsonify(data)
      
       
    

    

@app.route('/water_consumption/upload', methods=['GET', 'POST'])
def upload_water_consumption():
    if request.method == 'POST':
        # Retrieve the uploaded file from the form data
        file = request.files['file']
        
        # Parse the Excel file using a library like Pandas
        df = pd.read_excel(file, sheet_name='MAIN')
        
        # Open a database session and bulk-insert the data into the WaterConsumption table
        session = Session()
        for _, row in df.iterrows():
            if not pd.isna(row['Date']):
                water_consumption = WaterConsumption(
                    date=row['Date'],

                    river=row['River'],
                    process=row['Process'],
                    drinking=row['Drinking'],
                    # finishing_return=row["Finishing Return"],
                    # piece_dying_return=row['Piece Dying Return'],
                    total_return=row['Total Return'],
                    drinking_school=row['Drinking School'],
                    etp=row['ETP'],
                    weaving=row['Weaving'],
                    old_finishing=row['Old finishing'],
                    new_finishing=row['New finishing'],
                    total_fsg=row['Total fsg'],
                    piece_dyeing=row['Piece Dyieng'],
                    dyeing=row['Dyeing'],
                    wool_scoring=row['Wool scoring'],
                    folding=row['Folding'],
                    recombing=row['Recombing'],
                    drinking_ro=row['Drinking RO'],
                    spinning=row['Spinning'],
                    boiler=row['Boiler'],
                    engg_drinking=row['Engg. Drinking'],
                    grey_combing=row['Grey combing'],
                    regeneration=row['Regeneration'],
                    total_process_return=row['Total = Process - Return'],
                    all_process_total=row['All process total'],
                    canteen=row['canteen'],
                    run_hr_m_small_pump = row['Run hr m (Small pump)'],
                    run_hr_m_big_pump = row['Run hr m        (Big pump)'],
                    rain_water_kl_small_pump = row['rain water KL(small pump)'],
                    rain_water_kl_big_pump = row['rain water KL(BIG pump)'],
                    total_rain_water_kl = row['TOTAL RAIN WATER(KL)'],
                    c = row['C'],
                    d = row['D'],
                    opening = row['Opening'],
                    salt_consumption = row['Salt Consumption'],
                    salt_balance = row[' Salt Balance'],
                    alum_bricks_stock = row['Alum Bricks  Stock'],
                    con = row['con'],
                    balance = row['balance'],
                    powder_consumption = row['Powder Consumption'],
                    powder_balance = row['Powder Balance '],
                    utility = row['Utility'],
                    production = row['Production'],
                    diff = row['Diff'],
                    hardness = row['Hardness'],
                    tds = row['TDS'],

                )
                session.add(water_consumption)
        session.commit()
        session.close()
    return render_template('upload.html')

   


@app.route('/check-connection', methods=['GET'])
def check_connection():
    # Try to create a SQLAlchemy engine and connect to the Postgres database
    try:
        engine = create_engine(DB_URI)
        conn = engine.connect()
        conn.close()
        return 'Connection successful!'
    except OperationalError as e:
        return f'Connection failed: {e}'

if __name__ == '__main__':
    app.run(debug=True,port=8080)

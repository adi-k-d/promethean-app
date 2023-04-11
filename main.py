from flask import Flask, jsonify,request,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
import pandas as pd


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://adityakd:59XrsGxjZKfNrGw9@appsmith.sensomak.com:5432/raymond_vapi_plant_performance'
DB_URI = 'postgresql://adityakd:59XrsGxjZKfNrGw9@appsmith.sensomak.com:5432/raymond_vapi_plant_performance'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = create_engine('postgresql://username:password@localhost/dbname')
Session = sessionmaker(bind=engine)

class SteamConsumption(db.Model):
    __tablename__ = 'steam_consumption'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    total_steam = db.Column(db.Float)
    finishing = db.Column(db.Float)
    weaving = db.Column(db.Float)
    recombing = db.Column(db.Float)
    grey_combing = db.Column(db.Float)
    dyeing = db.Column(db.Float)
    spinning = db.Column(db.Float)
    sludge_drier = db.Column(db.Float)
    w_s = db.Column(db.Float)
    pc_dyg = db.Column(db.Float)
    tfo = db.Column(db.Float)
    steaming_m_c = db.Column(db.Float)
    unmetered = db.Column(db.Float)
    unmetered_percentage = db.Column(db.Float)
    dm_water = db.Column(db.Float)
    recovery_percentage = db.Column(db.Float)

class WaterConsumption(db.Model):
    __tablename__ = 'water_consumption'
    id = db.Column(db.Integer, primary_key=True)
    consumption_date  = db.Column(db.Date)
    river = db.Column(db.Float)
    process = db.Column(db.Float)
    drinking = db.Column(db.Float)
    finishing_return = db.Column(db.Float)
    piece_dying_return = db.Column(db.Float)
    total_return = db.Column(db.Float)
    drinking_school = db.Column(db.Float)
    etp = db.Column(db.Float)
    weaving = db.Column(db.Float)
    old_finishing = db.Column(db.Float)
    new_finishing = db.Column(db.Float)
    total_fsg = db.Column(db.Float)
    piece_dyeing = db.Column(db.Float)
    dyeing = db.Column(db.Float)
    wool_scoring = db.Column(db.Float)
    folding = db.Column(db.Float)
    recombing = db.Column(db.Float)
    drinking_ro = db.Column(db.Float)
    spinning = db.Column(db.Float)
    boiler = db.Column(db.Float)
    engg_drinking = db.Column(db.Float)
    grey_combing = db.Column(db.Float)
    regeneration = db.Column(db.Float)
    total_process_return = db.Column(db.Float)
    all_process_total = db.Column(db.Float)
    canteen = db.Column(db.Float)
    run_hr_m_small_pump = db.Column(db.Float)
    run_hr_m_big_pump = db.Column(db.Float)
    rain_water_kl_small_pump = db.Column(db.Float)
    rain_water_kl_big_pump = db.Column(db.Float)
    total_rain_water_kl = db.Column(db.Float)
    c = db.Column(db.Float)
    d = db.Column(db.Float)
    opening = db.Column(db.Float)
    salt_consumption = db.Column(db.Float)
    salt_balance = db.Column(db.Float)
    alum_bricks_stock = db.Column(db.Float)
    balance = db.Column(db.Float)
    con = db.Column(db.Float)
    powder_consumption = db.Column(db.Float)
    powder_balance = db.Column(db.Float)
    utility = db.Column(db.Float)
    production = db.Column(db.Float)
    diff = db.Column(db.Float)
    hardness = db.Column(db.Float)
    tds = db.Column(db.Float)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/steam_consumption')
def get_steam_consumption():
    steam_data = SteamConsumption.query.all()
    results = [
        {
            'id': data.id,
            'date': data.date,
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
            steam_consumption = SteamConsumption(
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
   for data in water_data:
       result_dict = {}
       for column in WaterConsumption.table.columns:        
        result_dict[column.name] = getattr(data, column.name)
        results.append(result_dict)
        return jsonify(results)


    

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
            water_consumption = WaterConsumption(
                consumption_date=row['Date'],
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
    app.run(debug=True)

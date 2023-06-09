from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
    date  = db.Column(db.Date)
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
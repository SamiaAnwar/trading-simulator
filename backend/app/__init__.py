from flask import Flask
from app.routes import app_routes, scheduled_update
from apscheduler.schedulers.background import BackgroundScheduler

def create_app():
    app = Flask(__name__) 
    app.register_blueprint(app_routes)
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_update, 'interval', days=1)
    scheduler.start()
    return app 
from flask import Flask
from server.config import app, db
from server.controllers import guest_controller, episode_controller, appearance_controller, auth_controller

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
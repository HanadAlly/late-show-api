from server.config import db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

def seed_data():
    with db.app.app_context():
        db.drop_all()
        db.create_all()

        # Seed Guests
        guests = [
            Guest(name='John Doe', occupation='Actor'),
            Guest(name='Jane Smith', occupation='Comedian'),
            Guest(name='Alice Johnson', occupation='Musician')
        ]
        db.session.bulk_save_objects(guests)
        db.session.commit()
        # Seed Episodes
        episodes = [
            Episode(date='2025-06-01', number=1),
            Episode(date='2025-06-02', number=2)
        ]
        db.session.bulk_save_objects(episodes)
        db.session.commit()

        # Seed Appearances
        appearances = [
            Appearance(rating=4, guest_id=1, episode_id=1),
            Appearance(rating=5, guest_id=2, episode_id=1),
            Appearance(rating=3, guest_id=3, episode_id=2)
        ]
        db.session.bulk_save_objects(appearances)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
from server.config import db

class Appearance(db.Model):
    __tablename__ = 'appearances'
    __table_args__ = {'extend_existing': True}  # Add this to prevent redefinition error

    id = db.Column(db.Integer, primary_key=True)
    _rating = db.Column(db.Integer, nullable=False)  # Store rating internally
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'guest_id': self.guest_id,
            'episode_id': self.episode_id
        }

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value
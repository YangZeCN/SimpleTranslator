from extensions import db, bcrypt

# Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), default='User')
    description = db.Column(db.String(200), default='')

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'description': self.description
        }

class AgentConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(80), nullable=False)
    api_key = db.Column(db.String(200), nullable=True)
    base_url = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(200), nullable=True)
    editable = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'provider': self.provider,
            # 'api_key': self.api_key,
            'base_url': self.base_url,
            'description': self.description,
            'editable': self.editable
        }

from flask import Flask, request, jsonify
from flask_cors import CORS
from extensions import db, bcrypt, create_app
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, load_app_config
from models import User, AgentConfig
from extensions import db, create_app
import os, sys, logging
from agent import AgentApi 

app = create_app()

# 设置日志记录
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)


class StreamToLogger:
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.level, line.rstrip())

    def flush(self):
        pass

use_stream = os.getenv('USE_STREAM', 'false').lower() == 'true'

if use_stream:
    print('use stream logger')
    stdout_logger = logging.getLogger('STDOUT')
    stderr_logger = logging.getLogger('STDERR')
    sys.stdout = StreamToLogger(stdout_logger, logging.INFO)
    sys.stderr = StreamToLogger(stderr_logger, logging.ERROR)


def set_password(password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

def create_tables():
    db.create_all()
    if User.query.count() > 0:
        app.logger.warning('Devices found, skip initializing database...')
        return
    app.logger.info('No devices found, initializing database...')
    # Init Admin User   
    admin = User(username='admin', password=set_password('admin123'), description='Administrator')

    agents = [ 
        AgentConfig(
            provider='OpenAI',
            api_key=os.getenv('OPENAI_API_KEY', ''),
            base_url='https://api.openai.com/v1',
            description='OpenAI GPT-3.5/4/5',
            editable=False
        ),
        AgentConfig(
            provider='DeepSeek',
            api_key=os.getenv('DEEPSEEK_API_KEY', ''),
            base_url='https://api.deepseek.com',
            description='DeepSeek AI Model',
            editable=False
        ),
        AgentConfig(
            provider='Custom',
            api_key='',
            base_url='',
            description='Custom LLM Provider',
            editable=True
        )
    ]

    # save to database
    db.session.add(admin)
    db.session.add_all(agents)
    db.session.commit()

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    print(f'Registering user {data["username"]}...')
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "User already exists"}), 400

    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        print(f'User {data["username"]} logged in successfully.')
        return jsonify({"message": "Login successful"}), 200
    else:
        print(f'Login failed for user {data["username"]}.')
        return jsonify({"message": "Invalid credentials"}), 401
    
@app.route('/api/agents', methods=['GET'])
def get_agents():
    agents = AgentConfig.query.all()
    return jsonify([agent.to_dict() for agent in agents]), 200

@app.route('/api/agents/<int:agent_id>', methods=['PUT'])
def update_agent(agent_id):
    data = request.json
    agent = AgentConfig.query.get(agent_id)
    if not agent:
        return jsonify({"message": "Agent not found"}), 404

    agent.provider = data.get('provider', agent.provider)
    agent.api_key = data.get('api_key', agent.api_key)
    agent.base_url = data.get('base_url', agent.base_url)
    agent.description = data.get('description', agent.description)
    agent.editable = data.get('editable', agent.editable)

    db.session.commit()
    return jsonify({"message": "Agent updated successfully"}), 200

@app.route('/api/config', methods=['GET'])
def get_app_config():
    app_config = load_app_config()
    return jsonify(app_config), 200

@app.route('/api/translate', methods=['POST'])
def translator():
    data = request.json
    prompt = data.get('prompt', '')
    provider = data.get('provider', '')
    model_name = data.get('model', '')
    mode = data.get('mode', 'translate')
    target_lang = data.get('target_lang', 'zh')
    agentConfig = AgentConfig.query.filter_by(provider=provider).first()
    if not agentConfig:
        return jsonify({"message": "Agent not found"}), 404
    app_config = load_app_config()
    model_configs = [m for m in app_config.models if m.name == model_name and provider in m.providers]
    if not model_configs:   
        return jsonify({"message": "Model not found for the specified provider"}), 404
    model_config = model_configs[0]
    agentApi = AgentApi(agent_config=agentConfig, model_config=model_config)
    try:
        result = agentApi.translate_text_with_mode(text=prompt, mode=mode, target_lang=target_lang)
        return jsonify({"result": result}), 200
    except Exception as e:
        app.logger.error(f"Translation error: {e}")
        return jsonify({"message": "Translation failed", "error": str(e)}), 500

with app.app_context():
    create_tables()

if __name__ == '__main__':
    app.run(debug=True)


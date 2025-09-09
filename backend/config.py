import os
from dataclasses import dataclass
from typing import List
import yaml


DB_PATH = os.path.join(os.path.dirname(__file__), 'db', 'config.db')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

APP_CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.yml')

@dataclass
class ModelConfig:
    name: str
    providers: List[str]
    max_tokens: int
    temperature: float


@dataclass
class AppConfig:
    models: List[ModelConfig]


def load_app_config() -> AppConfig:
    with open(APP_CONFIG_PATH, "r") as f:
        raw = yaml.safe_load(f)
        models = [ModelConfig(**model) for model in raw["models"]]
        return AppConfig(models=models)

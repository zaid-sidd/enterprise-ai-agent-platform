import os

import psycopg
from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://agent_user:agent_password@localhost:5432/agent_platform",
)


def get_connection():
    return psycopg.connect(DATABASE_URL)
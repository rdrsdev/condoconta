import os

PROJECT_NAME = "Randerson project"
VERSION = "0.1"

API_PREFIX = os.environ.get("API_PREFIX", "")

DEBUG = os.environ.get("DEBUG", True)

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_SCHEME = os.environ.get("DB_SCHEME", "")

EMAIL_USER = os.environ.get("EMAIL_USER", "exemplo@email.com.br")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD", "senha")
EMAIL_HOST = os.environ.get("EMAIL_HOST", "")

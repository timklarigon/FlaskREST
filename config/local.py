from mongoengine import connect, register_connection


class Config:
    MONGODB_HOST = "127.0.0.1"
    MONGODB_PORT = 5000
    MONGODB_USER = "admin"
    MONGODB_PWD = "password"
    MONGODB_DB = 'flask_rest'
    REDIS_SERVER = 'localhost'

system_config = Config()
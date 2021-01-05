class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/smilecook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

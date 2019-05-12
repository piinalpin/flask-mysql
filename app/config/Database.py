class DbConfig:
    def __init__(self):
        self.DB_USERNAME = "<YOUR_USERNAME>"
        self.DB_PASSWORD = "<YOUR_PASSWORD>"
        self.DB_HOST = "localhost"
        self.DB_PORT = 3306
        self.DB_NAME = "<YOUR_DATABASE_NAME>"

    def getUri(self):
        return "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(self.DB_USERNAME, self.DB_PASSWORD, self.DB_HOST,
                                                              self.DB_PORT, self.DB_NAME)

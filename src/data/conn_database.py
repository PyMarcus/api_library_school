import mysql.connector
from mysql.connector import errorcode
from initFileReader import InitFileReader


class DataBaseConn:
    def __init__(self, host, user, password, database):
        """
        Connect with sql database
        :param host:
        :param user:
        :param password:
        :param database:
        """
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    @property
    def host(self):
        return self.__host

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @property
    def database(self):
        return self.__database

    def connect(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print(f"Conectado com sucesso ao banco {self.database}")
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database não existe")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Senha incorreta")
            else:
                print(error)
        else:
            return conn


if __name__ == '__main__':
    # debug

    db = DataBaseConn(
        host=InitFileReader.readFile('../settings/data_conn.ini', 'desenv')['host'],
        user=InitFileReader.readFile('../settings/data_conn.ini', 'desenv')['user'],
        password=InitFileReader.readFile('../settings/data_conn.ini', 'desenv')['password'],
        database=InitFileReader.readFile('../settings/data_conn.ini', 'desenv')['database']
    )
    db.connect()

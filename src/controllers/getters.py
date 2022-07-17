import time
from conn_database import DataBaseConn
from initFileReader import InitFileReader


def con(local='../settings/data_conn.ini', env="desenv"):
    """
    starts database connection
    local: init file path
    env: enviroment [desenv] or [production]
    :return: database connection
    """
    host, password, user, database = '', '', '', ''
    """
    for key, value in InitFileReader.readFile(local, env):
        if key == 'host':
            host = value
        if key == 'password':
            password = value
        if key == 'user':
            user = value
        if key == 'database':
            database = value
    """
    """
    db = DataBaseConn(
        host=host,
        user=user,
        password=password,
        database=database
    )
    """
    db = DataBaseConn(
        host="127.0.0.1",
        user="",
        password="",
        database="Biblio"
    )
    return db.connect()


class Getters:

    last_id = 10000
    init_id = 0

    def __init__(self):
        ...

    def getStudents(self, **kwargs) -> dict:
        """
        Returns all students
        :param kwargs:
        :return:
        """

        conn = con(local='../settings/data_conn.ini', env="desenv")
        cursor = conn.cursor()
        start = time.time()
        cursor.execute(
            f"""
            SELECT 
                *
            FROM 
                Aluno
            WHERE 
                matricula > {self.init_id} AND matricula < {self.last_id};
            """
        )
        end = time.time()
        response = cursor.fetchall()
        object_json = dict()
        object_json['time_to_exec'] = end - start
        for items in response:
            if self.init_id == self.last_id:
                self.last_id += 10000  # query limit
                break
            object_json[items[0]] = list(items[1:])
            self.init_id += 1
        conn.close()
        return object_json

    def getStudentsForId(self, id: str or int) -> dict:
        """
        Search student for id
        :param id:
        :return: dict
        """
        conn = con(local='../settings/data_conn.ini', env="desenv")
        cursor = conn.cursor()
        start = time.time()
        sql = f"""
            SELECT 
                *
            FROM 
                Aluno
            WHERE
                matricula = {id};
        """
        end = time.time()
        data = dict()
        data["time_to_exec"] = end - start
        cursor.execute(sql)

        for item in cursor.fetchall():
            data[item[0]] = item[1:]
            conn.close()
            return data

    def getStudentsForName(self, name: str) -> dict:
        """
        Search student for the name
        :param name:
        :return: dict
        """
        conn = con(local='../settings/data_conn.ini', env="desenv")
        cursor = conn.cursor()
        start = time.time()
        sql = f"""
            SELECT 
                *
            FROM 
                Aluno
            WHERE
                nome = '{name}';
        """
        end = time.time()
        data = dict()
        data["time_to_exec"] = end - start
        cursor.execute(sql)

        for item in cursor.fetchall():
            data[item[0]] = item[1:]
            conn.close()
            return data

    def getStudentsForEmail(self, email: str) -> dict:
        """
        Search student for the email
        :param email:
        :return: dict
        """
        conn = con(local='../settings/data_conn.ini', env="desenv")
        cursor = conn.cursor()
        start = time.time()
        sql = f"""
            SELECT 
                *
            FROM 
                Aluno
            WHERE
                email = '{email}';
        """
        end = time.time()
        data = dict()
        data["time_to_exec"] = end - start
        cursor.execute(sql)

        for item in cursor.fetchall():
            data[item[0]] = item[1:]
            print(data)
            conn.close()
            return data

    def getStudentsByDate(self, date: str) -> dict:
        """
        Search student by date
        :param date: 2022-02-01, for example
        :return: dict
        """
        conn = con(local='../settings/data_conn.ini', env="desenv")
        cursor = conn.cursor()
        start = time.time()
        sql = f"""
            SELECT 
                *
            FROM 
                Aluno
            WHERE
                data_nascimento = '{date}';
        """
        end = time.time()
        data = dict()
        data["time_to_exec"] = end - start
        cursor.execute(sql)

        for item in cursor.fetchall():
            data[item[0]] = item[1:]
            print(data)
            conn.close()
            return data

    def getBooks(self, **kwargs) -> dict:
        """
        Returns all books
        :param kwargs:
        :return:
        """

        conn = con(local='../settings/data_conn.ini', env="desenv")
        cursor = conn.cursor()
        start = time.time()
        cursor.execute(
            f"""
            SELECT 
                *
            FROM 
                Livros
            WHERE 
                registro > {self.init_id} AND registro < {self.last_id};
            """
        )
        end = time.time()
        response = cursor.fetchall()
        object_json = dict()
        object_json['time_to_exec'] = end - start
        for items in response:
            if self.init_id == self.last_id:
                self.last_id += 10000  # query limit
                break
            object_json[items[0]] = list(items[1:])
            self.init_id += 1
        conn.close()
        return object_json

    def getBooksId(self, id: str or int) -> dict:
        """
        Search books by id
        :param id:
        :return: dict
        """
        conn = con(local='../settings/data_conn.ini', env="desenv")
        cursor = conn.cursor()
        start = time.time()
        sql = f"""
            SELECT 
                *
            FROM 
                Livros
            WHERE
                registro = {id};
        """
        print(sql)
        end = time.time()
        data = dict()
        data["time_to_exec"] = end - start
        cursor.execute(sql)

        for item in cursor.fetchall():
            data[item[0]] = item[1:]
            conn.close()
            return data

    def getBooksQueryParameters(self, id: int, status: str) -> dict:
        """
        Search books by id
        :param id:
        :return: dict
        """
        conn = con(local='../settings/data_conn.ini', env="desenv")
        cursor = conn.cursor()
        start = time.time()
        sql = f"""
            SELECT 
                *
            FROM 
                Livros
            WHERE
                registro = {id} and status = {status};
        """
        print(sql)
        end = time.time()
        data = dict()
        data["time_to_exec"] = end - start
        cursor.execute(sql)
        for item in cursor.fetchall():
            data[item[0]] = item[1:]
            conn.close()
            return data


if __name__ == '__main__':
    g = Getters().getStudents()
    g = Getters().getStudentsForName("Aluno1")
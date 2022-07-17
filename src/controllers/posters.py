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


class Posters:
    def __init__(self):
        ...

    def posterStudent(self, values: dict) -> None:
        """
        Insert data on the table Alunos
        :param values:
        :return:
        """
        conn = con(local='../settings/data_conn.ini', env="desenv")
        cursor = conn.cursor()
        lista = ''
        for index, v in enumerate(values.values()):
            if index != len(values) - 1:
                lista += f"{v}" + ','
            else:
                lista += f"{v}"
        sql = """
            INSERT INTO
                Aluno(nome, email, data_nascimento)
            VALUES
                (%s, %s, %s);
        """
        print(sql)
        try:
            cursor.execute(sql, tuple(lista.split(',')))
            print(cursor.execute(sql, tuple(lista.split(','))))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    Posters().posterStudent({"nome": "nomo",
    "email": "nomo@gmail.com",
    "data_nascimento": "2022-02-05"})

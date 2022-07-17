import configparser


class InitFileReader:
    """
    Read and choice enviroment from init file specificated
    """
    @staticmethod
    def readFile(file_path: str = "../settings/data_conn.ini", enviroment: str = "desenv") -> 'ItemsView[str, str]':
        """
        read .init file
        enviroment desenv or production
        :return: dict
        """
        file = configparser.ConfigParser()
        file.read(file_path)
        return file[enviroment].items()

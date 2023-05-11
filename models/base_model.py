import psycopg2


class BaseModel():
    @staticmethod
    def cone_db():
        """
        This method will connect to DB
        :return:
        """
        conn = psycopg2.connect(
        database='machine_learning_1',
        user='postgres', 
        password='qwertz',
        host='localhost',
        port='5432'
        )
        return conn
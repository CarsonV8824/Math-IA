import csv
import sqlite3

class DataHandling:
    def __init__(self, database="src/data/MathIA.db") -> None:
        self.data:list[tuple] = [()]
        self.total = 0
        
        # init private methods
        self.__get_data_from_csv()

        self.__make_database(database=database)
        self.__insert_in_database(self.data)
        self.__sort_database()

    def __get_data_from_csv(self) -> None:
        with open("src/data/data.csv") as f:
            file = csv.reader(f)

            for index, line in enumerate(file):
                if index < 1:
                    continue
                else:
                    self.data.append(line)
                    self.total = index
                    
    def __make_database(self, database="src/data/MathIA.db"):
        self.connection:sqlite3.Connection = sqlite3.Connection(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS math_ia(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class TEXT,
            hour_of_class INTEGER,
            favorite_subject TEXT,
            best_class INTEGER
        );
        """)
    
    def __insert_in_database(self, data:list[tuple]) -> None:
        for index, line in enumerate(data):
            try:
                sql_query = f'''INSERT INTO math_ia (class, hour_of_class, favorite_subject, best_class)
                VALUES (?,?,?,?)
                '''
                self.cursor.execute(sql_query, (line[1], line[2], line[3], 1 if line[4].lower() == "yes" else 0))
                self.connection.commit()
            except Exception as e:
                print(f"csv not formatted correctly one line {index+1}. Error {e}")

    def __sort_database(self) -> None:
        sql_query = f"SELECT * from math_ia ORDER BY hour_of_class ASC"
        self.cursor.execute(sql_query)
        self.connection.commit()

    def get_all_data(self) -> list[tuple]:
        self.cursor.execute("SELECT * FROM math_ia")
        data = self.cursor.fetchall()
        return data
    
    def __del__(self) -> None:
        self.connection.close()


if __name__ == "__main__":
    data = DataHandling()
    print(data.get_all_data())
            
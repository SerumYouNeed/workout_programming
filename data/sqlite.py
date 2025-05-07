import sqlite3


class SQLHandler:
    def __init__(self):
        try:
            self.connection = sqlite3.connect("data.db")
            cursor = self.connection.cursor()

            with open("data/schema.sql", "r") as schema_file:
                sql_script = schema_file.read()

            cursor.executescript(sql_script)
            cursor.close()

        except sqlite3.Error as error:
            pass
            # print(f'Error while reading sql script', error)

    def read_all_exercises(self):
        cursor = self.connection.cursor()
        query = "SELECT DISTINCT exercise FROM exercises;"
        try:
            cursor.execute(query)
            exercises_list = []
            ex = cursor.fetchall()
            for i in ex:
                exercises_list.append(i[0])
            # connection.close()
        except sqlite3.Error as error:
            print(f"Error while reading exercises list", error)
            cursor.close()
        return sorted(exercises_list)

    def read_all_muscles(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT DISTINCT muscle FROM exercises;")
        tup = cursor.fetchall()
        muscles = []
        for m in tup:
            muscles.append(m[0])
        return sorted(muscles)

    def read_multiplier_muscle(self, exercise):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT multiplier, muscle FROM exercises WHERE exercise == ?", (exercise,)
        )
        tup = cursor.fetchall()
        return tup

    def check_if_exists(self, muscle, exercise):
        sqlite_check_query = """SELECT muscle, exercise
                                FROM exercises 
                                WHERE muscle == ? AND exercise == ?"""
        data_tuple = (muscle, exercise)
        cursor = self.connection.cursor()
        cursor.execute(sqlite_check_query, data_tuple)
        if_exist = cursor.fetchall()
        cursor.close()
        return if_exist

    def new_exercise(self, muscle, exercise, weight):
        cursor = self.connection.cursor()
        sqlite_insert_query = """INSERT INTO exercises
                          (id, muscle, exercise, multiplier) 
                           VALUES 
                          (NULL, ?, ?, ?)"""
        data_tuple = (muscle, exercise, weight)
        cursor.execute(sqlite_insert_query, data_tuple)
        self.connection.commit()
        cursor.close()

    def check_add_correctly(self, muscle, exercise, weight):
        """
        This function check if exercise has been added correctly
            Args:
                muscle (string): what muscle was chosen
                exercise (string): name of the exercise
                weight (int): multiplier. How much work a muscle must do. 0.1 - almost no effort, 1 - muscle is main mover.

            Returns:
                if_exist (list of tuples): [ (muscle, exercise, weight) ]"""
        sqlite_check_query = """SELECT muscle, exercise, multiplier
                                FROM exercises 
                                WHERE muscle == ? AND exercise == ? AND multiplier == ?"""
        data_tuple = (muscle, exercise, weight)
        cursor = self.connection.cursor()
        cursor.execute(sqlite_check_query, data_tuple)
        if_exist = cursor.fetchall()
        cursor.close()
        return if_exist

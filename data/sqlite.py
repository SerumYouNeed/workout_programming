import sqlite3

class SQLHandler:
    def __init__(self):
        try:
            self.connection = sqlite3.connect('data.db')
            cursor = self.connection.cursor()

            with open('data/schema.sql', 'r') as schema_file:
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
            print(f'Error while reading exercises list', error)
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
        cursor.execute("SELECT multiplier, muscle FROM exercises WHERE exercise == ?", (exercise,) )
        tup = cursor.fetchall()
        return tup 
   
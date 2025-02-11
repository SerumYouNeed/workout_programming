import customtkinter as ctk
import csv

class SaveButton(ctk.CTkButton):
    def __init__(self, master):
        super().__init__(master)

    def create_csv_plan(self):

        with open('workout_plan.csv', mode='w') as csv_file:
            fieldnames = ['day', 'exercise', 'sets']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for k in master.master.daily_routines.keys():
                writer.writerow({'day':k})
                for i in master.master.daily_routines[k]:
                    writer.writerow({'exercise': i.keys(), 'sets': i.values()})
import customtkinter as ctk
import csv

class SaveButton(ctk.CTkButton):
    def __init__(self, master):
        super().__init__(master)
        self.plan = master.daily_routines

        def create_csv_plan():

            with open('workout_plan.csv', mode='w') as csv_file:
                fieldnames = ['day', 'exercise', 'sets']
                
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

                for i in self.plan.keys():
                    writer.writerow({'day':i})
                    for k, v in self.plan[i].items():
                        writer.writerow({'exercise': k, 'sets': v})

        btn = ctk.CTkButton(master=master, 
                            text="Save",
                            width=100,
                            height=22,
                            font=("Helvatica", 15),
                            text_color="white",
                            fg_color="gray15",
                            corner_radius=8,
                            hover_color="gray18",
                            command=create_csv_plan)
        btn.grid(row=3, column=1, columnspan=2)
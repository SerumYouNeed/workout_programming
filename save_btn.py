import customtkinter as ctk
from reportlab.pdfgen import canvas
import csv

class SaveButton(ctk.CTkButton):
    def __init__(self, master):
        super().__init__(master)
        self.plan = master.daily_routines

        # Nonactive function. Create csv version of a plan.
        def create_csv_plan():
            with open('workout_plan.csv', mode='w') as csv_file:
                fieldnames = ['day', 'exercise', 'sets']    
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for i in self.plan.keys():
                    writer.writerow({'day':i})
                    for k, v in self.plan[i].items():
                        writer.writerow({'exercise': k, 'sets': v})

        def create_pdf():
            # A4 pagesize
            c = canvas.Canvas("workout_plan.pdf", pagesize=(595.27, 841.89)) 
            for i in self.plan.keys():
                c.drawString(50, 780, i)    
                for k, v in self.plan[i].items():
                    c.drawString(50, 780, f'{k}: {v}')
            # finnish page
            c.showPage()
            # save to pdf
            c.save()

        btn = ctk.CTkButton(master=master, 
                            text="Save",
                            width=100,
                            height=22,
                            font=("Helvatica", 15),
                            text_color="white",
                            fg_color="gray15",
                            corner_radius=8,
                            hover_color="gray18",
                            command=create_pdf)
        btn.grid(row=3, column=1, columnspan=2)
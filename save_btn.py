import customtkinter as ctk
from reportlab.pdfgen import canvas
import csv

class SaveButton(ctk.CTkButton):
    def __init__(self, master):
        super().__init__(master)
        self.plan = master.daily_routines
        self.start_point_x = 50
        self.start_point_y = 780

        # Nonactive function. Create csv version of a plan.
        def create_csv_plan():
            with open('workout_plan.csv', mode='w') as csv_file:
                fieldnames = ['day', 'exercise', 'sets']    
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for i in self.plan.keys():
                    for k, v in self.plan[i].items():
                        writer.writerow({'day':i})
                        writer.writerow('day' i'exercise': k, 'sets': v})

        def create_pdf():
            # A4 pagesize
            c = canvas.Canvas("workout_plan.pdf", pagesize=(595.27, 841.89))
            c.setFont('Helvetica-Bold', 25, leading = None)
            c.drawString(self.start_point_x, self.start_point_y, 'Personal workout:')
            self.start_point_y -= 5
            c.line(self.start_point_x, self.start_point_y, self.start_point_x + 250, self.start_point_y)     
            self.start_point_y -= 50
            for i in self.plan.keys():
                ex_nr = 1
                c.setFont('Helvetica-Bold', 25, leading = None)
                c.drawString(self.start_point_x, self.start_point_y, i)
                self.start_point_y -= 40     
                for k, v in self.plan[i].items():
                    c.setFont('Helvetica', 18, leading = None)
                    if v == 1:
                        c.drawString(self.start_point_x, self.start_point_y, f'{ex_nr}. {k} - {v} set')
                    else:
                        c.drawString(self.start_point_x, self.start_point_y, f'{ex_nr}. {k} - {v} sets')
                    ex_nr += 1
                    self.start_point_y -= 30     
            self.start_point_y -= 40     
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
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from reportlab.pdfgen import canvas
import csv


class SaveButton(ctk.CTkButton):
    def __init__(self, master):
        super().__init__(master)
        self.plan = master.daily_routines
        self.start_point_x = 50
        self.start_point_y = 780

        def create_csv_plan(file_name):
            filename = f"{file_name}.csv"
            with open(filename, mode="w") as csv_file:
                fieldnames = ["day", "exercise", "sets"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for i in self.plan.keys():
                    for k, v in self.plan[i].items():
                        writer.writerow({"day": i, "exercise": k, "sets": v})

        def create_pdf(file_name):
            filename = f"{file_name}.pdf"
            # A4 pagesize
            c = canvas.Canvas(filename, pagesize=(595.27, 841.89))
            c.setFont("Helvetica-Bold", 25, leading=None)
            c.drawString(self.start_point_x, self.start_point_y, "Personal workout:")
            self.start_point_y -= 5
            c.line(
                self.start_point_x,
                self.start_point_y,
                self.start_point_x + 250,
                self.start_point_y,
            )
            self.start_point_y -= 50
            for i in self.plan.keys():
                ex_nr = 1
                c.setFont("Helvetica-Bold", 25, leading=None)
                c.drawString(self.start_point_x, self.start_point_y, i)
                self.start_point_y -= 40
                for k, v in self.plan[i].items():
                    c.setFont("Helvetica", 18, leading=None)
                    if v == 1:
                        c.drawString(
                            self.start_point_x,
                            self.start_point_y,
                            f"{ex_nr}. {k} - {v} set",
                        )
                    else:
                        c.drawString(
                            self.start_point_x,
                            self.start_point_y,
                            f"{ex_nr}. {k} - {v} sets",
                        )
                    ex_nr += 1
                    self.start_point_y -= 30
            self.start_point_y -= 40
            # finnish page
            c.showPage()
            # save to pdf
            c.save()

        def type_file_name():
            dialog = ctk.CTkInputDialog(
                text="Enter a <name>. Program will create two files for you: \n<name>.pdf\n<name>.csv\nYou can find them in the location of the program.",
                title="Name your file",
            )
            return dialog.get_input()

        def show_checkmark():
            CTkMessagebox(
                title="Great!",
                message="Your workout was successfully saved.",
                icon="check",
                option_1="Thanks",
            )

        def callback_btn():
            file_name = type_file_name()
            create_csv_plan(file_name)
            create_pdf(file_name)
            show_checkmark()

        btn = ctk.CTkButton(
            master=master, text="Save", font=("", 15), command=callback_btn
        )
        btn.grid(row=3, column=1, columnspan=2)

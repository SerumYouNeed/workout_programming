import customtkinter as ctk
from data.sqlite import SQLHandler
from CTkMessagebox import CTkMessagebox


class ToplevelWindowAddExercise(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x700")
        self.grid_columnconfigure((0, 1), weight=1)

        self.sql_handler = SQLHandler()
        self.muscle_list = self.sql_handler.read_all_muscles()

        self.label = ctk.CTkLabel(
            self, text="Create a name of your exercise.", font=("", 18), wraplength=200
        )
        self.label.grid(column=0, row=0, padx=20, pady=20, sticky="E")
        self.entry = ctk.CTkEntry(self, placeholder_text="Exercise name")
        self.entry.grid(column=1, row=0, padx=20, pady=20, sticky="W")

        self.label_musc = ctk.CTkLabel(
            self,
            text="What muscle are you going to train? If more that one, add another exercise with the same name but different muscle and multiplier.",
            font=("", 18),
            wraplength=200,
        )
        self.label_musc.grid(column=0, row=1, padx=20, pady=20, sticky="E")
        self.musc = ctk.CTkComboBox(
            self, values=self.muscle_list, font=("", 18), dropdown_font=("", 18)
        )
        self.musc.grid(column=1, row=1, padx=20, pady=20, sticky="W")

        self.label_mult = ctk.CTkLabel(
            self,
            text="Set the multiplier from 0.1 (exercise has almost no impact for given muscle group) to 1 (indicate that chosen muscle is main mover during that exercise).",
            font=("", 18),
            wraplength=200,
        )
        self.label_mult.grid(column=0, row=2, padx=20, pady=20, sticky="E")
        self.mult = ctk.CTkSlider(self, from_=0.1, to=1, number_of_steps=10)
        self.mult.grid(column=1, row=2, padx=20, pady=20, sticky="W")

        def btn_create():
            name = self.entry.get()
            muscle = self.musc.get()
            multiplier = self.mult.get()
            if (name != "") and (muscle != ""):
                if self.sql_handler.check_if_exists(muscle, name) == []:
                    self.sql_handler.new_exercise(muscle, name, multiplier)
                    ex_added = self.sql_handler.check_add_correctly(
                        muscle, name, multiplier
                    )
                    if (muscle, name, multiplier) in ex_added:
                        CTkMessagebox(
                            title="Create exercise",
                            message="Your exercise was successfully added.",
                            icon="check",
                            option_1="OK",
                        )

                    else:
                        CTkMessagebox(
                            title="Ups...",
                            message="Something went wrong.",
                            icon="cancel",
                        )

                else:
                    CTkMessagebox(
                        title="Create exercise",
                        message="It seems your exercise is already on the list.",
                        icon="warning",
                    )
            else:
                CTkMessagebox(
                    title="Create exercise",
                    message="All options must be filled and checked",
                    icon="warning",
                )

        btn = ctk.CTkButton(self, text="Create", font=("", 15), command=btn_create)

        btn.grid(column=0, columnspan=2, row=3, pady=40)


class ChoiceFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.configure(fg_color="transparent")

        self.toplevel_window_add_exercise = None

        self.sql_handler = SQLHandler()
        self.exercises_list = self.sql_handler.read_all_exercises()

    def create_widgets(self, parent):
        def ex_callback(ex):
            parent.exercise = ex
            lst = self.sql_handler.read_multiplier_muscle(ex)
            # loop sets muscle_multiplier dict
            for i in range(len(lst)):
                parent.muscle_multiplier[lst[i][1]] = lst[i][0]

        def set_callback(set):
            if set == None:
                CTkMessagebox(
                    title="Message",
                    message="All options must be filled before adding.",
                    icon="warning",
                )
            else:
                parent.sets = int(set)

        def new_exercise():
            if (
                self.toplevel_window_add_exercise is None
                or not self.toplevel_window_add_exercise.winfo_exists()
            ):
                # create window if its None or destroyed
                self.toplevel_window = ToplevelWindowAddExercise(self)
            else:
                self.toplevel_window_add_exercise.focus()

        combo_ex = ctk.CTkComboBox(
            master=self,
            values=self.exercises_list,
            command=ex_callback,
            font=("", 18),
            dropdown_font=("", 18),
            width=230,
        )
        combo_ex.grid(column=1, row=0, padx=15, pady=10, sticky="W")
        combo_ex_lbl = ctk.CTkLabel(self, text="Pick exercise:", font=("", 18, "bold"))
        combo_ex_lbl.grid(column=0, row=0, padx=15, sticky="E")

        combo_set = ctk.CTkComboBox(
            master=self,
            values=["1", "2", "3", "4", "5"],
            command=set_callback,
            font=("", 18),
            dropdown_font=("", 18),
            width=70,
        )
        combo_set.grid(column=1, row=1, padx=15, pady=10, sticky="W")
        combo_set_lbl = ctk.CTkLabel(self, text="Woking sets:", font=("", 18, "bold"))
        combo_set_lbl.grid(column=0, row=1, padx=15, sticky="E")

        add_exercise_lbl = ctk.CTkLabel(
            self, text="Add new exercise to the list:", font=("", 18, "bold")
        )
        add_exercise_lbl.grid(column=0, row=2, padx=15, sticky="E")
        add_exercise_btn = ctk.CTkButton(
            self, text="New exercise", font=("", 15), command=new_exercise
        )
        add_exercise_btn.grid(column=1, row=2, padx=15, pady=10, sticky="W")

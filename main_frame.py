import customtkinter as ctk
from empty_frame import EmptyFrame
from data.sqlite import SQLHandler


class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.set_appearance_mode("dark")
        self.grid(row=0, column=0, sticky="ewns")

        self.sql_handler = SQLHandler()

    def create_widgets(self, parent):
        grittings = ctk.CTkLabel(
            self, text="Welcome in the workout creator!", font=("", 29, "bold")
        )
        instructions = ctk.CTkLabel(self, font=("", 18), wraplength=700)
        frecquency_q = ctk.CTkLabel(
            self, text="How many days are you going to train?", font=("", 22)
        )

        def nextBtn_callback():
            parent.number_of_training_days = int(frecquency_selector.get())
            parent.switch_frame(EmptyFrame)

        next_btn = ctk.CTkButton(
            self, text="Next", font=("", 15), command=nextBtn_callback
        )

        def combobox_callback(choice):
            match choice:
                case "1":
                    instructions.configure(
                        text="One day a week is usually not enough - but hey, it is still better than none. Try to train full body on each training sesion."
                    )
                case "2":
                    instructions.configure(
                        text="For two training days it is highly recomended to perform two full body training. In this case each muscle will be trained two times per week. You can stimulate muscles from diffrent angles - say, perform flat bench press on day one and incline on day two."
                    )
                case "3":
                    instructions.configure(
                        text="Three days split can be aranged as 3 x FBW, or you can create two routines A/B - like upper/lower, push/pull, torso/limbs, front/rear - and train A/B/A in first week, then B/A/B in second. Traing will be a tad longer then in four days per week but much more versatile then one and two days per week."
                    )
                case "4":
                    instructions.configure(
                        text="Four days split can be aranged as 4 x FBW, or you can create two routines A/B - like upper/lower, push/pull, torso/limbs, front/rear - and train A/B/A/B."
                    )
                case "5":
                    instructions.configure(
                        text="Five days FBW split is hard to maintain, but if your recovery is ok you can try it. Training each muscle more than twice a week can be really challenging."
                    )
                case "6":
                    instructions.configure(
                        text="Only if everything in your life is about GAINS. Remember, even pros do not workout everyday. It is really, really hard to maintain that kind of routine."
                    )
                case "7":
                    instructions.configure(
                        text="Really...? Do you REALLY want to go to the gym every day? Give me a break."
                    )
            instructions.pack(pady=30, padx=30, ipady=15, ipadx=15, fill="both")

        frecquency_selector = ctk.CTkComboBox(
            self,
            values=["1", "2", "3", "4", "5", "6", "7"],
            font=("", 18),
            dropdown_font=("", 18),
            width=70,
            command=combobox_callback,
        )

        # place widgets
        grittings.pack(pady=50)
        frecquency_q.pack(pady=15)
        frecquency_selector.pack(pady=15)
        next_btn.pack()

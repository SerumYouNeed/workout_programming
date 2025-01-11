import customtkinter as ctk
from empty_frame import EmptyFrame
from data.sqlite import SQLHandler



class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        self.grid(row=0, column=0, sticky="ewns")
        self.sql_handler = SQLHandler()


    def create_widgets(self, parent):
        # create widgets
        grittings = ctk.CTkLabel(self, 
                                 text="Welcome in workout creator!",
                                 fg_color="black",
                                 text_color="white",
                                 font=("Helvatica", 27))
        instructions = ctk.CTkLabel(self, 
                                 text_color="white",
                                 font=("Helvatica", 16),
                                 bg_color="gray18",
                                 corner_radius=8, 
                                 width=500,
                                 wraplength=500,
                                 justify="left")
        frecquency_q = ctk.CTkLabel(self, 
                                 text="Training days:",
                                 fg_color="black",
                                 text_color="white",
                                 font=("Helvatica", 22))
        def nextBtn_callback():
            parent.number_of_training_days = int(frecquency_selector.get())
            # self.sql_handler.create_exercise_set_table(parent.number_of_training_days)
            parent.switch_frame(EmptyFrame)
                    
        next_btn = ctk.CTkButton(self,
                                 text="Next",
                                 font=("Helvatica", 15),
                                 text_color="white",
                                 fg_color="gray15",
                                 corner_radius=8,
                                 hover_color="gray18",
                                 command=nextBtn_callback) 
               
        def combobox_callback(choice):
            match choice:
                case "1":
                    instructions.configure(text="One day a week is usually not enough - but hey, it is still better that none.\nPick max 7 exercises from dropdown menu below. Number of exercises is not random.\nYou can pick less and adjust later.")
                case "2":
                    instructions.configure(text="For two training days it is highly recomended to perform two full body training.\nIn this case each muscle will be trained two times per week.\nYou can stimulate muscles from diffrent angles - say, perform flat bench press on day one and incline on day two.")
                case "3":
                    instructions.configure(text="Three days split can be aranged as 3 x FBW, or you can create two routines A/B - like upper/lower, push/pull, torso/limbs, front/rear - and train A/B/A in first week, then B/A/B in second.\nTraing will be a tad longer then in four days per week but much more versatile then one and two days per week.")
                case "4":
                    instructions.configure(text="Four days split can be aranged as 4 x FBW, or you can create two routines A/B - like upper/lower, push/pull, torso/limbs, front/rear - and train A/B/A/B.\nTraining each muscle twice a week is a sweet spot. You can add some volume and not stuck in the gym for hours.")
                case "5":
                    instructions.configure(text="Five days FBW split is hard to maintain, but if your recovery is ok you can try it.\nYou can create routines like upper/lower, push/pull, torso/limbs, front/rear, push/pull/legs.\nTraining each muscle more than twice a week can be really challenging.")
                case "6":
                    instructions.configure(text="Only if everything in your life is about GAINS.\nRemember, even pros do not workout everyday.\nIt is really, really hard to maintain that kind of routine. Anyway, you will spend so much time in the gym that you can perform nearly every kind of workout.")
                case "7":
                    instructions.configure(text="Really...? Do you REALLY want to go to the gym every day? Give me a break.")
            instructions.pack(pady=30, padx=30, ipady=15, ipadx=15, fill="both")

        frecquency_selector = ctk.CTkComboBox(self, 
                                              values=["1", "2", "3", "4", "5", "6" , "7"], 
                                              command=combobox_callback)

        # place widgets
        grittings.pack(pady=50)
        frecquency_q.pack(pady=15)
        frecquency_selector.pack(pady=15)
        next_btn.pack()


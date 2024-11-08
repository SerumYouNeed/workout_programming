import customtkinter as ctk
from programming_frame1 import ProgrammingFrame1, ProgrammingFrame2

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.configure(fg_color="black")
        self.grid(row=0, column=0, sticky="ewns")

    def create_widgets(self, parent):
        # create the grid
        self.rowconfigure((0,1,2), weight=1)
        self.columnconfigure((0,1), weight=1)

        # create widgets
        self.next_frame = ProgrammingFrame1(self)
        grittings = ctk.CTkLabel(self, 
                                 text="Welcome in workout creator!",
                                 fg_color="black",
                                 text_color="white",
                                 font=("Helvatica", 27))
        instructions = ctk.CTkTextbox(self, 
                                 fg_color="black",
                                 text_color="white",
                                 font=("Helvatica", 16),
                                 wrap="word",
                                 bg_color="gray18",
                                 corner_radius=8)
        frecquency_q = ctk.CTkLabel(self, 
                                    text="Training days:",
                                    fg_color="black",
                                    text_color="white",
                                    font=("Helvatica", 22))
        next_btn = ctk.CTkButton(self,
                                 text="Next",
                                 font=("Helvatica", 15),
                                 text_color="white",
                                 fg_color="gray15",
                                 corner_radius=8,
                                 hover_color="gray18") 
               
        def combobox_callback(choice):
            match choice:
                case "1":
                    instructions.insert("0.0", "One day a week is usually not enough - but hey, it is steel better that none. Pick max 7 exercises from dropdown menu below. Number of exercises is not random. That way you should cover all your major muscle groups. You can pick less and adjust later - but more will not give you better gains. One thing for sure: you will spent more than two hours in the gym meanwhile much of your sets will be counterproductive.")
                    instructions.grid(row=2, column=0, columnspan=2)
                    # parent.switch_frame(ProgrammingFrame1)
                case "2":
                    instructions.insert("0.0", "For two training days it is highly recomended to perform two full body training. In this case each muscle will be trained two times per week. You can stimulate muscles from diffrent angles - say, perform flat bench press on day one and incline on day two.")
                    instructions.grid(row=2, column=0, columnspan=2)
                    # parent.switch_frame(ProgrammingFrame2)
                case "3":
                    instructions.insert("0.0", "Three days split can be aranged as a 3 x FBW, or you can create two routines A/B - like upper/lower, push/pull, torso/limbs, front/rear - and train A/B/A in first week, then B/A/B in second. Traing will be a tad longer then in four days per week but much more versatile then one and two days per week.")
                    instructions.grid(row=2, column=0, columnspan=2)
                case "4":
                    instructions.insert("0.0", "Four days split can be aranged as 4 x FBW, or you can create two routines A/B - like upper/lower, push/pull, torso/limbs, front/rear - and train A/B/A/B. Training each muscle twice a week is a sweet spot. You can add some volume and not stuck in the gym for hours.")
                    instructions.grid(row=2, column=0, columnspan=2)
                case "5":
                    instructions.insert("0.0", "Five days FBW split is hard to maintain, but if your recovery is ok you can try it. You can create routines like upper/lower, push/pull, torso/limbs, front/rear, push/pull/legs. Training each muscle more than twice a week can be really challenging.")
                    instructions.grid(row=2, column=0, columnspan=2)
                case "6":
                    instructions.insert("0.0", "Only if everything in your life is about GAINS. Remember that even pros do not workout everyday. It is really, really hard to maintain that kind of routine. Anyway, you will spend so much time in the gym that you can perform nearly every kind of workout.")
                    instructions.grid(row=2, column=0, columnspan=2)
                case "7":
                    instructions.insert("0.0", "Really...? Give me a break.")
                    instructions.grid(row=2, column=0, columnspan=2)

        frecquency_selector = ctk.CTkComboBox(self, 
                                              values=["1", "2", "3", "4", "5", "6" , "7"], 
                                              command=combobox_callback)

        # place widgets
        # Sticky pin frame to east, west, north, south 
        grittings.grid(row=0, column=0, columnspan=2)
        frecquency_q.grid(row=1, column=0, sticky="e")
        frecquency_selector.grid(row=1, column=1, sticky="w")
        next_btn.grid(row=3, column=0, columnspan=2)




        

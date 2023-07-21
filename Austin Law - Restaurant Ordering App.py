"""
Restaurant Ordering App
Written by Austin Law

Note: Make sure you have CustomTkinter installed to ensure the program runs as intended.
This can be done by typing "pip3 install customtkinter" in the command prompt when ran as administrator.

You would also want to make sure that pillow is installed. 
This is done by typing "pip install --upgrade pip" and "pip install --upgrade Pillow" 
into the command prompt to install the 
"""

# Importing the Modules
import customtkinter
from tkinter import *
from PIL import Image, ImageTk

class TopNavBar(customtkinter.CTkFrame):
    global indicate, dessert_indicator, hide_indicate
    def __init__(self, master):
        super().__init__(master)
        # ---------------------------------- Widgets ---------------------------------- #
        # region | Buttons for the Top Navigation Bar
        main_btn = customtkinter.CTkButton(self, text="Mains", 
                                           font=customtkinter.CTkFont(family="Calibri", size=35), 
                                           fg_color="transparent", text_color="black", hover_color="gray",
                                           command=lambda: indicate(main_indicator))
        main_btn.grid(column=0, row=0, padx=10, pady=10, sticky='we')

        appetisers_btn = customtkinter.CTkButton(self, text="Appetisers", font=customtkinter.CTkFont(family="Calibri", size=35), 
                                           fg_color="transparent",text_color="black", hover_color="gray", command=lambda: indicate(appetisers_indicator))
        appetisers_btn.grid(column=1, row=0, padx=10, pady=10, sticky='we')

        dessert_btn = customtkinter.CTkButton(self, text="Desserts", font=customtkinter.CTkFont(family="Calibri", size=35), 
                                           fg_color="transparent",text_color="black", hover_color="gray", command=lambda: indicate(dessert_indicator))
        dessert_btn.grid(column=2, row=0, padx=10, pady=10, sticky='we')
        # endregion

        # region | Frames which would act as an indicator for the buttons
        main_indicator = customtkinter.CTkFrame(self, corner_radius=5, height=6, width=100, fg_color="black")
        main_indicator.grid(row=0, column=0, sticky='s',pady=5)
        
        appetisers_indicator = customtkinter.CTkFrame(self, corner_radius=5, height=6, width=175, fg_color="white")
        appetisers_indicator.grid(row=0, column=1, sticky='s',pady=5)

        dessert_indicator = customtkinter.CTkFrame(self, corner_radius=5, height=6, width=140, fg_color="white")
        dessert_indicator.grid(row=0, column=2, sticky='s',pady=5)
        # endregion

        # region | Function for the indicator
        def hide_indicate():                    # Changes the indicators white to match the background of the top navigation frame
            main_indicator.configure(fg_color="white")
            appetisers_indicator.configure(fg_color="white")
            dessert_indicator.configure(fg_color="white")

        def indicate(fr):
            hide_indicate()                     # Calls the function to hide all indicators
            fr.configure(fg_color="black")      # The indicator associated with the button will turn black in color
        # endregion


class MainsSelection(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # region | Label for the Mains Page
        title = customtkinter.CTkLabel(self, text="Mains", 
                                       font=customtkinter.CTkFont(size=50, weight="normal", 
                                                                  underline=True, family="Calibri"), text_color="white")
        title.grid(column=0, row=0, pady= 10, padx=35, sticky="nw")
        # endregion

        
        # ---------------------------------- Frames ---------------------------------- #
        dfl = 6               # Number of display frames
        # List to store widgets 
        main_frames_list = []
        # Loop that runs depending on the dfl value divided by the desired number of columns
        for make_list in range((round(dfl/3))):
            main_frames_list.append([])        # Appends empty list into the main list 


        # Loop that runs for for however long the dfl value is
        for main_frame in range(dfl):
            self.rowitem = customtkinter.CTkFrame(self, corner_radius=10, width=300)        # Creates a base frame for the item display

            # ---------- If Conditions ---------- #
            # Conditioned to only run when the display frame value is less than 3
            if main_frame < 3:
                self.rowitem.grid(column=0 + main_frame, row=1, sticky="nsew", pady=20, padx=15)     # Grids the frame to row 1 and increases by 1 in columns
                main_frames_list[0].append(self.rowitem)
            # Conditioned to run when the display frame value is more or equal to 3
            if main_frame >= 3:
                self.rowitem.grid(column=0 + (main_frame - 3), row=2, sticky="nsew", pady=20, padx=15)   # Grids the frame to row 2 and would subtract 3 to reset the column position
                main_frames_list[1].append(self.rowitem)
        
        # ---------------------------------- Images ---------------------------------- #
        # Cutlet Image
        cutlet = customtkinter.CTkImage(Image.open("Images/Cutlet.jpg"), size=(275, 200))               # Imports image 
        cutlet_imgbtn = customtkinter.CTkButton(main_frames_list[0][0], image=cutlet, text="",       # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")          # Font Configuration
        cutlet_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                       # Gridding for the image button

        """cutlet_img = customtkinter.CTkLabel(display_frames_list[0][0], image=cutlet, text="")
        cutlet_img.grid(row=0, column=0, sticky="news", pady=20, padx=20)"""

        # Lasagna Image
        lasagna = customtkinter.CTkImage(Image.open("Images/Lasagna.jpg"), size=(275, 200))             # Imports image 
        lasagna_imgbtn = customtkinter.CTkButton(main_frames_list[0][1], image=lasagna, text="",     # Puts the image in a button
                                                 fg_color='transparent', hover_color="#333333")         # Font Configuration
        lasagna_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                      # Gridding the image button

        """lasagna_img = customtkinter.CTkLabel(display_frames_list[0][1], image=lasagna, text="")
        lasagna_img.grid(row=0, column=0, sticky="news", pady=20, padx=20)"""

        # Burger Image
        burger = customtkinter.CTkImage(Image.open("Images/Burger.jpg"), size=(275, 200))               # Imports image 
        burger_imgbtn = customtkinter.CTkButton(main_frames_list[0][2], image=burger, text="",       # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")          # Font Configuration
        burger_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                       # Gridding the image button

        """burger_img = customtkinter.CTkLabel(display_frames_list[0][2], image=burger, text="")
        burger_img.grid(row=0, column=0, sticky="news", pady=20, padx=20)"""

        # ----------------------------- Buttons / Labels ----------------------------- #
        # Cutlet Button / Label
        cutlet_lbl = customtkinter.CTkButton(main_frames_list[0][0], text="Chicken Cutlet \n Price: $21.99", 
                                            font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        cutlet_lbl.grid(row=1, column=0, sticky='new', pady=(5,10), padx=10)

        # Lasagna Button / Label
        lasagna_lbl = customtkinter.CTkButton(main_frames_list[0][1], text="Lasagna \n Price: $15.00", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        lasagna_lbl.grid(row=1, column=0, sticky='new', pady=(5,10), padx=10)

        # Burger Button / Label
        burger_lbl = customtkinter.CTkButton(main_frames_list[0][2], text="Beef Burger \n Price: $13.00", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        burger_lbl.grid(row=1, column=0, sticky='new', pady=(5,10), padx=10)

        # Testing a add to order Button
        ato_btn = customtkinter.CTkButton(main_frames_list[0][0], text = "+", width=40,
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        ato_btn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Restaurant Ordering App")
        self.attributes('-fullscreen', True)     # Sets the window to fullscreen

        # ---------------------------- Grid Configuration ---------------------------- #
        self.grid_columnconfigure((0,1), weight=1)

        # ---------------------------------- Frames ---------------------------------- #
        # Top Navigation Bar
        self.TopNavBarFrame = TopNavBar(self)
        self.TopNavBarFrame.grid(column=0, row=0, sticky='nwes', columnspan=2)
        self.TopNavBarFrame.configure(corner_radius=0, height=75, fg_color="white")

        # Menu Selection
        self.MainsSelectionFrame = MainsSelection(self)
        self.MainsSelectionFrame.grid(column=0, row=1, sticky='news', columnspan=2)
        self.MainsSelectionFrame.configure(height=1500, corner_radius=0)
        
        # Order List
        self.order_list = customtkinter.CTkFrame(self, corner_radius=0,  width=500, fg_color='blue')
        self.order_list.grid(column=2, row=0, rowspan= 2, sticky='nsew')


app=App()
app.mainloop()
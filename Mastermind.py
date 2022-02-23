# Importing inbuilt Python functions
from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk



# declaring global variables and global lists. Since these are important and used in many places, they need to be global.
global chances 
global chosen_list 
global game_list
global b_list
global w_list
global row1_ans_list


# Assigning values to global variables and lists. 
color_list = ["blue", "red", "green3", "yellow", "saddle brown", "turquoise2", "hot pink", "dark violet"]
row1_ans_list = []
b_list = []
w_list = []
game_list = []
chances = 12


# Defining the function 'get_random_color()'
# This function selects 5 random colors from color_list. These 5 colors are the answer for the game.
# Input = None
# Output = The list holding the 5 colors
def get_random_colors():
    global color_list 
    random_list = []
    while True:
        item = random.choice(color_list)
        if item not in random_list:
            random_list.append(item)
        if len(random_list) == 5:
            break

        
    return random_list

# Defining the function 'play_game'
# This is the main function of the program. 
# Input = color of the button that is being pressed
# Output = None
def play_game(button_color):

    global chances
    global game_list
    global b_list
    global w_list

    if chances == 0:
        messagebox.showmessage('Oh no!', "game over!")
        return    
    
    row_list = game_list[chances - 1]
    for label in row_list:
        if label.cget("background") == button_color:
            messagebox.showerror("Error", "You already used this color")
            return

    for label in row_list:
        if label.cget("background") == "gray70":
            label.config(background = button_color, relief = "solid")
            break
        
   
    if row_list[4].cget("background") != "gray70":
        blacks = get_num_blacks(row_list)
        whites = get_num_whites(row_list)
        b_list[chances - 1].config(text = blacks)
        w_list[chances - 1].config(text = whites)

        if blacks == 5:
            messagebox.showinfo(":D", "You win! You're a mastermind now!")
            reveal_color()
            return
        
        chances -= 1

    if chances == 0:
        messagebox.showerror("Oh no!", "Game over! Better luck next time")
        reveal_color()
        reset_game()

    
        
        
        
        
# Defining the function 'get_num_blacks'
# This function calculates the number of blacks.
# Input = list of labels that display user input
# Output = number of blacks
def get_num_blacks(list_of_labels):
    num_blacks = 0
   
    for i in range(0, len(list_of_labels)):
        if list_of_labels[i].cget("background") == chosen_list[i]:
            num_blacks += 1

    return num_blacks

# Defining the function 'get_num_whites'
# This function calculates the number of whites.  
# Input = list of labels that display user input
# Output = number of whites
def get_num_whites(list_of_labels):
    num_whites = 0
    for i in range(0, len(list_of_labels)):
        if list_of_labels[i].cget("background") != chosen_list[i] and list_of_labels[i].cget("background") in chosen_list:
            num_whites += 1

    return num_whites

# Defining the function 'reveal_color'
# This function reveals the color to the user.  
# Input = None
# Output = None
def reveal_color():
    global row1_ans_list
    global chosen_list
    for i in range(0, len(row1_ans_list)):
        row1_ans_list[i].config(background = chosen_list[i], text = "")
        
    
# Defining the function 'clear_game_board'
# This function clears the current row.  
# Input = None
# Output = None
def clear_game_board():
    row_list = game_list[chances - 1]
    for label in row_list:
        label.config(background = "gray70", relief = "solid")

# Defining the function 'reset_game'
# This function starts a new game 
# Input = None
# Output = None
def reset_game():
    global chances
    global game_list
    global b_list
    global w_list
    global color_list
    global chosen_list
    global row1_ans_list
    chances = 12
    for row_list in game_list:
        for label in row_list:
            label.config(background = "gray70", relief = "solid")

    for b in b_list:
        b.config(text = "")

    for w in w_list:
        w.config(text = "")

    for color in chosen_list:
        chosen_list = get_random_colors()
   

    for label in row1_ans_list:
        label.config(background = "white", text = "?", relief = "solid")
      
# Defining the function 'rules'
# This function shows the rules of the game.  
# Input = None
# Output = None
def rules():
    messagebox.showinfo("RULES", """Rules of the game: \n GOAL : To guess the correct sequence of 5 unique colors.
    Each guess results in feedback narrowing down the possibilities of the sequence. You must get 5 blacks to win \n CHANCES :
    You have 12 tries \n BLACKS : Correct color, correct position \n WHITES : correct color, wrong position \n WARNING :
    You cannot repeat a color in a single try""")

# Defining the function 'draw_game_board'
# This function draws the whole layout.  
# Input = None
# Output = None
def draw_game_board():    
    title_label = Label(window, background = "black", text = "M A S T E R M I N D", fg = "white", font = "helvetica, 15")
    title_label.grid(row = 0, column = 1, columnspan = 8, pady = 5)
    #---------------------------------------------------START ROW 1---------------------------------------------------------------
    row1_label0 = Label(window, background = "white", text = "#", width = 3, relief = "sunken")
    row1_label0.grid(row = 1, column = 1, padx = 5, pady = 10)

    row1_ans_color1 = Label(window, background = "white", width = 3, height = 1, text = "?", relief = "solid")
    row1_ans_color1.grid(row = 1, column = 2, padx = 5, pady = 10)
    row1_ans_list.append(row1_ans_color1)

    row1_ans_color2 = Label(window, background = "white", width = 3, height = 1, text = "?", relief = "solid")
    row1_ans_color2.grid(row = 1, column = 3, padx = 5, pady = 10)
    row1_ans_list.append(row1_ans_color2)

    row1_ans_color3 = Label(window, background = "white", width = 3, height = 1, text = "?", relief = "solid")
    row1_ans_color3.grid(row = 1, column = 4, padx = 5, pady = 10)
    row1_ans_list.append(row1_ans_color3)

    row1_ans_color4 = Label(window, background = "white", width = 3, height = 1, text = "?", relief = "solid")
    row1_ans_color4.grid(row = 1, column = 5, padx = 5, pady = 10)
    row1_ans_list.append(row1_ans_color4)

    row1_ans_color5 = Label(window, background = "white", width = 3, height = 1, text = "?", relief = "solid")
    row1_ans_color5.grid(row = 1, column = 6, padx = 5, pady = 10)
    row1_ans_list.append(row1_ans_color5)

    row1_blackcount = Label(window, background = "white", width = 3, height = 1, text = "B", relief = "sunken")
    row1_blackcount.grid(row = 1, column = 7, padx = 5, pady = 10)

    row1_whitecount = Label(window, background = "white", width = 3, height = 1, text = "W", relief = "sunken")
    row1_whitecount.grid(row = 1, column = 8, padx = 5, pady = 10)
    #-------------------------------------------------------END ROW 1---------------------------------------------------------------------------------------
    #------------------------------------------------------START GUESS ----------------------------------------------------------------------------------------
    # creating labels on a loop
    for i in range(0, chances):
        row_num = i + 2
        colors_list = []
        Label(window, background = "white", width = 3, text = chances - i, relief = "sunken").grid(row = row_num, column = 1, padx = 5, pady = 2)
        for j in range(0, 5):
            col_num = j + 2
            colors_list.append(Label(window, background = "gray70", width = 3, height = 1, relief = "solid"))
            colors_list[j].grid(row = row_num, column = col_num, padx = 5, pady = 2)
        game_list.append(colors_list)

        b_list.append(Label(window, background = "black", fg = "white", width = 3, height = 1, relief = "sunken"))
        b_list[i].grid(row = row_num, column = 7, padx = 5, pady = 2)

        w_list.append(Label(window, background = "white", width = 3, height = 1, relief = "sunken"))
        w_list[i].grid(row = row_num, column = 8, padx = 5, pady = 2)
            

   

    #-------------------------------------------------------END GUESS---------------------------------------------------------------------------------------
    #Label(window, width = 40, background = "light blue").grid(row = 14, column = 0, columnspan = 14, padx = 5, pady = 5)



    #-------------------------------------------------------------------------------------------------------------------------------------------------
    #empty_label15 = Label(window, width = 2, background = "light blue").grid(row = 15, column = 0, padx = 15, pady = 20 )

    blue_button = Button(window, width = 3, height = 1, bg = "blue", command = lambda : play_game("blue"))
    blue_button.grid(row = 15, column = 1, pady = 10)


    red_button = Button(window, width = 3, height = 1, bg = "red", fg = "white", command = lambda : play_game("red"))
    red_button.grid(row = 15, column = 2)


    yellow_button = Button(window, width = 3, height = 1, bg = "green3", command = lambda : play_game("green3"))
    yellow_button.grid(row = 15, column = 3)


    yellow_button = Button(window, width = 3, height = 1, bg = "yellow", command = lambda : play_game("yellow"))
    yellow_button.grid(row = 15, column = 4)

    sb_button = Button(window, width = 3, height = 1, bg = "saddle brown", command = lambda : play_game("saddle brown"))
    sb_button.grid(row = 15, column = 5)

    turq2_button = Button(window, width = 3, height = 1, bg = "turquoise2", command = lambda : play_game("turquoise2"))
    turq2_button.grid(row = 15, column = 6)

    hp_button = Button(window, width = 3, height = 1, bg = "hot pink", command = lambda : play_game("hot pink"))
    hp_button.grid(row = 15, column = 7)

    dv_button = Button(window, width = 3, height = 1, bg = "dark violet", command = lambda : play_game("dark violet"))
    dv_button.grid(row = 15, column = 8)
    #-------------------------------------------Row 16-----------------------------------------------
    #empty_label16 = Label(window, width = 2, background = "light blue").grid(row = 16, column = 0, padx = 15, pady = 20)

    rules_button = Button(window, width = 6, height = 1, text = "rules", bg = "white", command = rules)
    rules_button.grid(row = 16, column = 1, columnspan = 3)
    
    reset_button = Button(window, width = 8, height = 1, text = "new game", bg = "white", command = reset_game)
    reset_button.grid(row = 16, column = 4, columnspan = 2, pady = 5)

    clear_button = Button(window, width = 6, height = 1, text = "clear", bg = "white", command = clear_game_board)
    clear_button.grid(row = 16, column = 6, columnspan = 3, pady = 5)

    #-------------------------------------------Row 17------------------------------------------------
    reveal_ans_button = Button(window, width = 7, height = 1, text = "cheat", bg = "white", command = reveal_color)
    reveal_ans_button.grid(row = 17, column = 1, columnspan = 8, pady = 5)

    
            
            

# creating the Tkinter window    
window = Tk()
window.resizable(0,0)
window.configure(background = "light blue")
window.geometry("300x490")
window.geometry("+550+150")
window.title("Mastermind")

# adding and adjusting the background image
bg_image = ImageTk.PhotoImage(Image.open("C:\\Users\\23rapr75\\wood.jpg"))
background_label = Label(window, image = bg_image)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# calling the function draw_game_board
draw_game_board()

# calling the function get_random_colors
chosen_list = get_random_colors()


# calling the window so that it will run
window.mainloop()

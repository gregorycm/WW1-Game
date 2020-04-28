from stats import stat
from menus import Menu
from game import Game


current_stats = stat()
men = Menu(current_stats)
gam = Game(current_stats)


print("Welcome to Bravery and Malice.")
print("Please choose a option.")
print("Also please type the number beside the option not the name.")
select_nation = False
game_ended = False
while not select_nation:
    men.print_menu()
    men.select()
    select_nation = men.check_options(gam.options)
while not game_ended:
    gam.print_situation()
    game_ended = gam.take_turn()

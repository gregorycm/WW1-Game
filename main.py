from stats import stat
from menus import menu
from game import game

current_stats = stat()
men = menu(current_stats)
gam = game(current_stats)

print("Welcome to Bravery and Malice.")
print("Please choose a option.")
print("Also please type the number beside the option not the name.")
select_nation = False
game_ended = False
while not select_nation:
  men.print_menu()
  men.select()
  select_nation = men.check_options()
while not game_ended:
  gam.print_situation()
  game_ended = gam.take_turn()

  
map_sokoban = {
    "size_x":5,
    "size_y":5
}

player = {
    "x": 4,
    "y": 0
}

boxes = [
    {"x":1, "y":1},
    {"x":2, "y":2},
    {"x":3, "y":3},
]

destinations = [
    {"x":2, "y":1},
    {"x":3, "y":2},
    {"x":4, "y":3},
]

# for y in range(map_sokoban["size_y"]):
#     for x in range(map_sokoban["size_x"]):
#         if x == player["x"] and y == player["y"]:
#             print("P", end="")
#         else:
#             print("- ",end="")
#     print()
playing = True
while playing:
    for y in range(map_sokoban["size_y"]):
        for x in range(map_sokoban["size_x"]):
            box_is_here = False
            
            for box in boxes:
                if box['x'] == x and box['y'] == y:
                    box_is_here =True
            
            dest_is_here = False
            
            for dest in destinations:
                if dest['x'] == x and dest['y'] == y:
                    dest_is_here =True

            player_is_here = False
            if x == player["x"] and y == player["y"]:
                player_is_here = True

            if player_is_here:
                print("P ", end="")
            elif box_is_here:
                print("B ", end="")
            elif dest_is_here:
                print("D ", end="")            
            else:
                print("- ", end="")

        print()


    move = input("Your move: ").upper()

    # if move == "W":
    #     print("Up")
    # elif move == "S":
    #     print("Down")
    # elif move == "A":
    #     print("left")
    # elif move == "D":
    #     print("Right")
    # else:
    #     playing = False
    dx = 0
    dy = 0
    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dy = -1
    elif move == "D":
        dy = 1
    else:
        playing = False

    if 0 <= player['x'] + dx < map_sokoban['size_x']\
     and 0 <= player['y'] + dy < map_sokoban['size_y']:
        player['x'] += dx
        player['y'] += dy
ball_scores = {
    "white": 0,
    "red": 1,
    "yellow": 2,
    "green": 3,
    "brown": 4,
    "blue": 5,
    "pink": 6,
    "black": 7}

player_score = {True:0,False:0}
#  first player is False and second player is true
turn = False
previous_ball=None
reds = 15
n = int(input())
for i in range(n):
    ball = input()
    if ball=="miss":
        turn = not turn
        previous_ball=None
    elif ball=="white":
        turn = not turn
        previous_ball=None

    elif ball =="red":
        if reds>0:
            player_score[turn]+=ball_scores[ball]
            reds-=1
            previous_ball=ball
        else:
            print("Invalid")
            break
    elif ball not in ball_scores:
        print("Invalid")
        break
    elif previous_ball is None:
        turn = not turn
        previous_ball=None
    elif previous_ball=="red":
        player_score[turn]+=ball_scores[ball]
        previous_ball=ball
        if reds==0:
            ball_scores.pop(ball)
    elif reds==0:
        player_score[turn]+=ball_scores[ball]
        previous_ball=ball
        ball_scores.pop(ball)
    else:
        turn = not turn
        previous_ball=None
else:
    if player_score[True]>player_score[False]:
        print("Second")
    elif player_score[True]<player_score[False]:
        print("First")
    else:
        print("Tie")
    





# n = int(input())
# scores = {
#     "white": 0, "red": 1,
#     "yellow": 2, "green": 3,
#     "brown": 4, "blue": 5,
#     "pink": 6, "black": 7
# }

# ball_list = [
#     "yellow", "green",
#     "brown", "blue",
#     "pink", "black",
# ]

# a = []
# for _ in range(n):
#     a.append(input())

# reds = 15

# previos_ball = None
# turn = False
# player_score = [0, 0]
# for ball in a:
#     if ball == "miss" or ball=="white":
#         turn = not turn
#         previos_ball = None
#     elif ball == "red":
#         if reds <= 0:
#             print("Invalid")
#             break
#         else:
#             previos_ball = "red"
#             player_score[int(turn)] += scores["red"]
#             reds -= 1
#     elif ball not in ball_list:
#         print("Invalid")
#         break

#     elif previos_ball == "red":
#         player_score[int(turn)] += scores[ball]
#         previos_ball = ball
#         if reds<=0:
#             ball_list.remove(ball)
#     elif reds == 0:
#         player_score[int(turn)] += scores[ball]
#         previos_ball = ball
#         ball_list.remove(ball)
#     elif reds != 0:
#         turn = not turn
#         previos_ball = None
# else:
#     if player_score[0] > player_score[1]:
#         print("First")
#     elif player_score[0] < player_score[1]:
#         print("Second")
#     else:
#         print("Tie")

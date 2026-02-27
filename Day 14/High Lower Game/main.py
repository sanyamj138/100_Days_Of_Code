def game_start(time_run):
    from dataFile import data
    import random

    account_a = random.choice(data)
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    def format_data(account):
        account_name = account['name']
        return account_name

    print(f"COMPARE A: {format_data(account_a)}.")
    print("WITH")
    print(f"COMPARE B: {format_data(account_b)}.")

    ans = input("WHO HAS MORE FOLLOWERS? TYPE 'A' OR 'B': ")

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    if ans == 'A':
        if a_follower_count > b_follower_count:
            print("YOU WIN!")
            return game_start(time_run + 1)
        elif a_follower_count < b_follower_count:
            print("YOU LOSE!")
            return time_run
        else:
            print("DRAW!")
            return game_start(time_run + 1)
    else:
        if a_follower_count > b_follower_count:
            print("YOU LOSE!")
            return time_run
        elif a_follower_count < b_follower_count:
            print("YOU WIN!")
            return game_start(time_run + 1)
        else:
            print("DRAW!")
            return game_start(time_run + 1)



start = input("WOULD YOU LIKE TO PLAY THIS GAME? TYPE 'Y FOR YES' or 'N FOR NO': ")
if start == 'Y' or start == 'y':
    sol = game_start(0)
    print("YOUR FINAL SCORE: ", sol)
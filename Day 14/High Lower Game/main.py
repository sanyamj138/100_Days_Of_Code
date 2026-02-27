from dataFile import data
import random

account_a = random.choice(data)
account_b = random.choice(data)

def format_data(account):
    account_name = account['name']
    return account_name


if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print("With")
print(f"Compare B: {format_data(account_b)}.")

ans = input("Who has more followers? Type 'A' or 'B': ")

a_follower_count = account_a['follower_count']
b_follower_count = account_b['follower_count']

if ans == 'A':
    if a_follower_count > b_follower_count:
        print("You Win!")
    elif a_follower_count < b_follower_count:
        print("You Lose!")
    else:
        print("Draw!")
else:
    if a_follower_count > b_follower_count:
        print("You Lose!")
    elif a_follower_count < b_follower_count:
        print("You Win!")
    else:
        print("Draw!")
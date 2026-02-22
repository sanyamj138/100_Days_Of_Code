from dataFile import data
import random

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)

account_name = account_a['name']
import os

def generate_coins(username, coins):
    return coins

while True:
    os.system('cls')
    os.system('color 0e')
    username = input("Enter your TikTok username: ")
    coins = int(input("Enter the desired value of coins: "))
    coins = generate_coins(username, coins)
    print("Congratulations, @" + username + "! You have generated", coins, "TikTok coins.")
    
    repeat = input("Do you want to repeat the process? (yes/no): ")
    if repeat.lower() != "yes":
        break

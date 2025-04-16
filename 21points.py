import random

cards = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def deal_card():
    return random.choice(list(cards.keys()))

def calculate_total(hand):
    total = 0
    aces = 0
    for card in hand:
        total += cards[card]
        if card == 'A':
            aces += 1

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def play_game():
    
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    print("你的手牌:", player_hand)
    print("庄家的明牌:", [dealer_hand[0]])

    while True:
        player_total = calculate_total(player_hand)
        if player_total > 21:
            print("你爆牌了，你输了！")
            return
        choice = input("你要继续要牌吗？(y/n): ")
        if choice.lower() == 'y':
            new_card = deal_card()
            player_hand.append(new_card)
            print("你拿到了:", new_card)
            print("你的手牌:", player_hand)
        else:
            break

    dealer_total = calculate_total(dealer_hand)
    while dealer_total < 17:
        new_card = deal_card()
        dealer_hand.append(new_card)
        print("庄家拿到了:", new_card)
        dealer_total = calculate_total(dealer_hand)

    print("你的手牌:", player_hand, "总点数:", calculate_total(player_hand))
    print("庄家的手牌:", dealer_hand, "总点数:", dealer_total)

    player_total = calculate_total(player_hand)
    if dealer_total > 21:
        print("庄家爆牌了，你赢了！")
    elif player_total > dealer_total:
        print("你赢了！")
    elif player_total < dealer_total:
        print("你输了,fw！")
    else:
        print("平局！")

# 开始游戏
if __name__ == "__main__":
    play_game()
    choice = input("想要再来一轮吗？(y/n):")
    if choice.lower() == 'y' :
        play_game()
    else:
        if choice.lower()=='n':
            quit

print("程序结束")    
        
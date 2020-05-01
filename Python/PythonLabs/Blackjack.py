def blackjack(hand1, hand2):
    if hand1 > 21 and hand2 > 21:
        return 0
    elif hand1 > hand2 and hand1 <=21:
        return hand1
    elif hand2 > hand1 and hand2 <=21:
        return hand2

print(blackjack(22, 22))
print(blackjack(18, 21))
print(blackjack(20, 18))
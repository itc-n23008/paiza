def calculate_rank(card_sequence, order_sequence, player_hand):
    player_rank = [0] * 52
    highest_card_num = 0
    last_player_index = 52

    while player_hand.count(0) != 52:
        for index, card_num in enumerate(player_hand):
            if last_player_index == index:
                highest_card_num = 0
            elif card_num > highest_card_num:
                highest_card_num = card_num
                last_player_index = index
                player_hand[index] = 0
                player_rank[index] = max(player_rank) + 1

    return player_rank

card_sequence = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
order_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
player_hand_list = [order_sequence[card_sequence.index(card)] for card in input("プレイヤーの手札を入力してください: ").split()]

rank = calculate_rank(card_sequence, order_sequence, player_hand_list)

for i in rank:
    print(i)


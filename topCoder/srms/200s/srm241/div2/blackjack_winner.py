class BlackjackWinner:
    def winnings(self, bet, dealer, dealerBlackjack, player, blackjack):
        if player > 21 or (player < dealer and dealer <= 21):
            return -bet
        if dealerBlackjack and blackjack:
            return 0
        if dealerBlackjack and not blackjack:
            return -bet
        if not dealerBlackjack and blackjack:
            return 1.5 * bet
        if dealer > 21 or player > dealer:
            return bet
        return 0

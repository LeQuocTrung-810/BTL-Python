class BJ_Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return f"{self.name}'s Hand: " + ", ".join(str(card) for card in self.cards)

    def add(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    @property
    def total(self):
        total = 0
        aces = 0
        for card in self.cards:
            val = card.value()
            total += val
            if card.rank == 'A':
                aces += 1
        # Đổi A từ 1 thành 11 nếu không bị bust
        while aces > 0 and total + 10 <= 21:
            total += 10
            aces -= 1
        return total

class BJ_Game:
    def __init__(self, deck, dealer, player):
        self.deck = deck
        self.dealer = dealer
        self.player = player

    def start(self):
        self.player.clear()
        self.dealer.clear()
        self.player.add(self.deck.deal())
        self.player.add(self.deck.deal())
        self.dealer.add(self.deck.deal())
        self.dealer.add(self.deck.deal())

    def hit_player(self):
        card = self.deck.deal()
        self.player.add(card)
        return card

    def stand(self):
        # Dealer rút bài đến khi tổng điểm >= 17
        while self.dealer.total < 17:
            self.dealer.add(self.deck.deal())

import tkinter as tk
from tkinter import messagebox
from cards import BJ_Deck
from games import BJ_Hand, BJ_Game

class BlackjackGUI:
    def __init__(self, master):
        self.master = master
        master.title("Blackjack Game")

        self.deck = BJ_Deck()
        self.deck.shuffle()

        self.dealer_hand = BJ_Hand("Dealer")
        self.player_hand = BJ_Hand("Player")

        self.game = BJ_Game(self.deck, self.dealer_hand, self.player_hand)

        self.player_frame = tk.LabelFrame(master, text="Player")
        self.player_frame.pack(padx=10, pady=5)

        self.dealer_frame = tk.LabelFrame(master, text="Dealer")
        self.dealer_frame.pack(padx=10, pady=5)

        self.status_label = tk.Label(master, text="Welcome to Blackjack!")
        self.status_label.pack()

        self.hit_button = tk.Button(master, text="Hit", command=self.hit)
        self.hit_button.pack(side=tk.LEFT, padx=10)

        self.stand_button = tk.Button(master, text="Stand", command=self.stand)
        self.stand_button.pack(side=tk.LEFT, padx=10)

        self.restart_button = tk.Button(master, text="Restart", command=self.restart_game)
        self.restart_button.pack(side=tk.LEFT, padx=10)

        self.restart_game()

    def update_hand_display(self):
        for widget in self.player_frame.winfo_children():
            widget.destroy()
        for widget in self.dealer_frame.winfo_children():
            widget.destroy()

        for card in self.player_hand.cards:
            tk.Label(self.player_frame, text=f"{str(card)}").pack(side=tk.LEFT)

        for card in self.dealer_hand.cards:
            tk.Label(self.dealer_frame, text=f"{str(card)}").pack(side=tk.LEFT)

        self.status_label.config(
            text=f"Player: {self.player_hand.total} | Dealer: {self.dealer_hand.total if not self.hit_button['state'] == tk.NORMAL else '??'}"
        )

    def hit(self):
        self.game.hit_player()
        self.update_hand_display()
        if self.player_hand.total > 21:
            self.status_label.config(text=f"Player: {self.player_hand.total} - Bust! Dealer wins.")
            messagebox.showinfo("Game Over", "You busted! 😢")
            self.disable_buttons()

    def stand(self):
        self.game.stand()
        self.update_hand_display()

        player_total = self.player_hand.total
        dealer_total = self.dealer_hand.total

        if dealer_total > 21:
            result = "Dealer busts! You win! 🎉"
        elif player_total > dealer_total:
            result = "You win! 🎉"
        elif player_total < dealer_total:
            result = "Dealer wins. 😢"
        else:
            result = "It's a tie."

        self.status_label.config(text=result)
        messagebox.showinfo("Result", result)
        self.disable_buttons()

    def disable_buttons(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)

    def restart_game(self):
        self.deck = BJ_Deck()
        self.deck.shuffle()

        self.player_hand.clear()
        self.dealer_hand.clear()

        self.game = BJ_Game(self.deck, self.dealer_hand, self.player_hand)
        self.game.start()

        self.update_hand_display()

        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)

        if self.player_hand.total == 21:
            self.status_label.config(text="Blackjack!")
            messagebox.showinfo("Result", "Blackjack! 🎉")
            self.disable_buttons()
        else:
            self.status_label.config(text="New game started. Good luck!")

# Chạy chương trình
if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()

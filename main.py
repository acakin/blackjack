from art import logo
from replit import clear
import random
choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
play = True
while play:  
  if choice == "n":
    clear()
    play = False
  if choice == "y":    
    clear()
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    name = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = {}
    deck2 = {}
    for _ in name:
      deck[_] = cards[name.index(_)]
      deck2[_] = cards2[name.index(_)]
   
    your_cards = []
    your_cards.append(random.choice(name))
    your_cards.append(random.choice(name))
    your_total = int()
    for _ in your_cards:  
      your_total += deck[_]
    print(f"Your hand is {your_cards} and your score is {your_total}.")
    
    dealer = []
    dealer.append(random.choice(name))
    dealer.append(random.choice(name))
    dealer_total = int()
    
    for _ in dealer:
      dealer_total += deck[_] 
    print(f"Dealar's first card is {dealer[0]}.")
    
    if dealer_total > 21:
      for _ in dealer:
        if "Ace" in dealer:
          dealer_total = 0
          for _ in dealer:
            dealer_total += deck2[_]          
    
    while dealer_total < 17:
      dealer_total = 0
      dealer.append(random.choice(name))
      for _ in dealer:
        dealer_total += deck[_]        
      if dealer_total >= 17:
          if dealer_total > 21:          
            if "Ace" in dealer:
              dealer_total = 0
              for _ in dealer:
                dealer_total += deck2[_]
                if dealer_total >= 17:
                  break
          else:
            break
      else:
        dealer_total = 0
        for _ in dealer:
          dealer_total += deck[_]
        
    if your_total == 21:
      print("You win with a Blackjack.")
    else:
      while your_total < 21:
        get_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if get_card == 'y':
          your_cards.append(random.choice(name))
          your_total = 0
          for _ in your_cards:
            your_total += deck[_]        
          if your_total > 21:
            for _ in your_cards:
              if "Ace" in your_cards:          
                your_total = 0        
                for _ in your_cards:
                  your_total += deck2[_]   
                  if your_total > 21:
                    print(f"Your final hand is {your_cards} and your final score is {your_total}.")
                    print(f"Dealer's final hand is {dealer} and dealer's final score is {dealer_total}.")
                    print("You went over. You lose.")
                  
                    break
                    
              else:
                print(f"Your final hand is {your_cards} and your final score is {your_total}.")
                print(f"Dealer's final hand is {dealer} and dealer's final score is {dealer_total}.")
                print("You went over. You lose.")
                break
          elif your_total == 21:
            if your_total > dealer_total:
              print(f"Your final hand is {your_cards} and your final score is {your_total}.")
              print(f"Dealer's final hand is {dealer} and dealer's final score is {dealer_total}.")
              print("You win.")
            elif your_total == dealer_total:
              print(f"Your final hand is {your_cards} and your final score is {your_total}.")
              print(f"Dealer's final hand is {dealer} and dealer's final score is {dealer_total}.")
              print("It is a draw.")
            
            
          
          else:
            print(f"Your hand is {your_cards} and your score is {your_total}.") 
                  
        elif get_card == 'n':      
          if your_total > dealer_total:
            print(f"Your final hand is {your_cards} and your final score is {your_total}.")
            print(f"Dealer's final hand is {dealer} and dealer's final score is {dealer_total}.")
            print("You win.")
            break
          elif your_total < dealer_total and dealer_total <= 21:
            print(f"Your final hand is {your_cards} and your final score is {your_total}.")
            print(f"Dealer's final hand is {dealer} and dealer's final score is {dealer_total}.")
            print("You lose.")
            break
          elif your_total == dealer_total:
            print(f"Your final hand is {your_cards} and your final score is {your_total}.")
            print(f"Dealer's final hand is {dealer} and dealer's final score is {dealer_total}.")
            print("It is a draw.")
            break
          elif your_total < dealer_total and dealer_total > 21:
            print(f"Your final hand is {your_cards} and your final score is {your_total}.")
            print(f"Dealer's final hand is {dealer} and dealer's final score is {dealer_total}.")
            print("Dealer went over. You win.")
            break
  choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
          
          
            
    
    

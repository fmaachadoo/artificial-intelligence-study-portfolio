import random
import logging

from pprint import pprint

logging.basicConfig(level=logging.DEBUG)


class Action:
    def play(self, player, target=None):
        pass


class Income(Action):
    name = "Income"
    require_target = False
    
    @staticmethod
    def play(player, target=None):
        player.coins += 1

    def __str__(self):
        return "Income"


class ForeignAid(Action):
    name = "Foreign Aid"
    require_target = False
    
    @staticmethod
    def play(player, target):
        reacting_player = target
        
        status = reacting_player.react_to_action(player, ForeignAid, reacting_player)
        if status == "Blocked":
            return status
        
        player.coins += 2
        
        return status

    def __str__(self):
        return "Foreign Aid"


class Coup(Action):
    name = "Coup"
    require_target = True
    
    @staticmethod
    def play(player, target):
        player.coins -= 7
        target.cards.pop()
        return 'Successful'

    def __str__(self):
        return "Coup"


class Tax(Action):
    name = "Tax"
    require_target = False
    
    @staticmethod
    def play(player, target=None):
        player.coins += 3

    def __str__(self):
        return "Tax"


class Assassinate(Action):
    name = "Assassinate"
    require_target = True
    
    @staticmethod
    def play(player, target):
        status = target.react_to_action(player, Assassinate, target)
        if status == "Blocked":
            return status
        
        player.coins -= 3
        target.cards.pop()
        
        return status

    def __str__(self):
        return "Assassinate"


class Steal(Action):
    name = "Steal"
    require_target = True
    
    @staticmethod
    def play(player, target):
        status = target.react_to_action(player, Steal, target)
        if status == "Blocked":
            return status
        
        remained_coins = target.coins - 2
        
        # If the target has less than 2 coins, the player can only steal the
        # amount of coins the target has
        if remained_coins < 0:
            player.coins += target.coins
            remained_coins = 0
        
        target.coins = remained_coins
        
        return status

    def __str__(self):
        return "Steal"


class BlockForeignAid(Action):
    name = "Block Foreign Aid"
    require_target = False
    
    @staticmethod
    def play(player, target):
        pass

    def __str__(self):
        return "Block Foreign Aid"


class BlockAssassination(Action):
    name = "Block Assassination"
    require_target = False
    
    @staticmethod
    def play(player, target):
        pass

    def __str__(self):
        return "Block Assassination"


class BlockStealing(Action):
    name = "Block Stealing"
    require_target = False
    
    @staticmethod
    def play(player, target):
        pass

    def __str__(self):
        return "Block Stealing"


class Card:
    def __init__(self):
        self.name = self.__class__.__name__


class Duke(Card):
    has_action = True
    action = Tax

    def play_action(self, target=None):
        return self.action()

    def block(self):
        return BlockForeignAid()

    def __str__(self):
        return "Duke"


class Assassin(Card):
    has_action = True
    action = Assassinate

    def play_action(self, player, target):
        return self.action(player, target)

    def __str__(self):
        return "Assassin"


class Captain(Card):
    has_action = True
    action = Steal
    
    def play_action(self, player, target):
        return self.action(player, target)

    def block(self):
        return BlockStealing()

    def __str__(self):
        return "Captain"


class Contessa(Card):
    has_action = False
    
    def block(self):
        return BlockAssassination()

    def __str__(self):
        return "Contessa"


class Player:
    is_artificial_intelligence = False

    COMMON_ACTIONS = [Income, ForeignAid]

    def __init__(self, name, players=[]):
        self.name = name
        self.cards = []
        self.coins = 2
        self.players = players
        
    def print_status(self):
        print(f"{self.name} has {self.coins} coins and [{', '.join(str(card) for card in self.cards)}] cards")

    def is_alive(self):
        return len(self.cards) > 0
    
    def choose_target(self, players):
        while True:
            chosen = random.choice(players)
            if chosen != self and chosen.is_alive():
                return chosen

    def play_action(self, action, target=None):
        if target:
            action(target)
        else:
            action()

    def decide_action(self):
        if self.coins >= 10:
            return Coup

        for i in range(random.randint(0, len(self.cards)-1)):
            card_index = i
            try:
                card = self.cards[card_index]
            except IndexError:
                card_index = 0

            if card.has_action:
                if card.action == Assassinate and self.coins < 3:
                    continue

                return card.action

        if self.coins >= 7:
            return Coup

        return random.choice(self.COMMON_ACTIONS)

    def perceive_action(self, player, action, influence=None, target=None):
        pass

    def react_to_action(self, player, action, target=None):
        for influence in self.cards:
            if influence == "Captain" and action == "Steal" and target == self:
                influence.block()
                return "Blocked"

            if (
                influence == "Contessa"
                and action == "Assassinate"
                and target == self
            ):
                influence.block()
                return "Blocked"

            if influence == "Duke" and action == "Foreign Aid":
                influence.block()
                return "Blocked"

        if target == self:
            return "Successful"

    def __str__(self):
        return self.name


class AIPlayer(Player):
    is_artificial_intelligence = True

    def __init__(self, name):
        super().__init__(name)
        self.logger = logging.getLogger(name)
    
    def initialize_players(self, players):
        self.knowledge = {
            player: {"cards": [], "actions": [], "coins": player.coins}
            for player in players
        }

    def perceive_action(self, player, action, influence=None, target=None):
        self.acknowledge_player_action(action, player, target)

    def react_to_action(self, player, action, influence=None, target=None):
        for influence in self.cards:
            if influence == "Captain" and action == "Steal" and target == self:
                return influence.block()
            if (
                influence == "Contessa"
                and action == "Assassinate"
                and target == self
            ):
                return influence.block()

            if influence == "Duke" and action == "Foreign Aid":
                return influence.block()

    def acknowledge_player_action(
        self, player, action, influence=None, target=None
    ):
        self.knowledge[player]["actions"].append(action)
        if target:
            print(
                f"AI acknowledged: {player.name} {action.name} {target.name}"
            )
        else:
            print(f"AI acknowledged: {player.name} {action.name}")
        
    def acknowledge_game_status(self, players):
        for player in players:
            self.knowledge[player]["coins"] = player.coins
            self.knowledge[player]["card_amount"] = len(player.cards)

    def predict_player_cards(self, player):
        # Initialize a dictionary to hold the inferred cards for the player
        inferred_cards = {
            "Duke": 0,
            "Assassin": 0,
            "Captain": 0,
            "Contessa": 0,
        }

        # Logical propositions based on actions
        for action in self.knowledge[player]["actions"]:
            if action == "Tax":
                inferred_cards["Duke"] += 1
            elif action == "Assassinate":
                inferred_cards["Assassin"] += 1
            elif action == "Steal":
                inferred_cards["Captain"] += 1
            elif action == "Block Foreign Aid":
                inferred_cards["Duke"] += 1
            elif action == "Block Assassination":
                inferred_cards["Contessa"] += 1
            elif action in ["Foreign Aid", "Income"]:
                inferred_cards["Duke"] = max(inferred_cards["Duke"] - 1, 0)
            elif action == "Assassinated":
                inferred_cards["Contessa"] = -1
            elif action == "Stolen":
                inferred_cards["Captain"] = -1

        # If a player never blocks Foreign Aid, they likely do not have a Duke
        if "Block Foreign Aid" not in self.knowledge[player]["actions"]:
            inferred_cards["Duke"] = (
                0 if "Duke" not in self.knowledge[player]["cards"] else 1
            )

        # TODO revise this logic
        # Repeated Income Actions
        if (
            self.knowledge[player]["actions"].count("Income") > 2
        ):  # Arbitrary threshold
            # Frequent use of Income might suggest a lack of powerful cards
            inferred_cards["Duke"] = max(inferred_cards["Duke"] - 1, 0)
            inferred_cards["Captain"] = max(inferred_cards["Captain"] - 1, 0)
            inferred_cards["Assassin"] = max(inferred_cards["Assassin"] - 1, 0)

        # Normalize the counts to reflect that each player has only two cards
        for card in inferred_cards:
            inferred_cards[card] = min(inferred_cards[card], 2)

        # Find the two most likely cards
        sorted_cards = sorted(
            inferred_cards.values(), key=lambda x: x[1], reverse=True
        )
        most_likely_cards = (
            [card for card in sorted_cards[:2]]
            if len(sorted_cards) > 1
            else sorted_cards
        )

        return most_likely_cards


class CoupGame:
    def __init__(self, players):
        self.players = players
        self.deck = [
            Duke(),
            Assassin(),
            Captain(),
            Contessa(),
        ] * 3
        self.dead_cards = []
        self.current_player = 0
        self.shuffle_deck()
        
        self.ai_players = [p for p in players if p.is_artificial_intelligence]
        
        for ai_player in self.ai_players:
            ai_player.initialize_players(self.players)
            ai_player.acknowledge_game_status(self.players)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_cards(self):
        print("Dealing cards...")
        # Deal two cards to each player
        for player in self.players:
            player.cards.append(self.deck.pop())
            player.cards.append(self.deck.pop())

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def play(self):
        self.deal_cards()
        
        while not self.is_game_over():
            player = self.players[self.current_player]
            print(f"{player}'s turn")
            if player.is_alive():
                self.take_turn(player)
                
            else:
                print(f"{player}'s dead!")
                self.players.remove(player)
            
            print('\n------------------')
            for player in self.players:
                player.print_status()
            print('------------------\n')
                
            self.next_turn()
        else:
            print(f"{self.players[0]} won!")

    def take_turn(self, player):
        target = None
        
        # Player takes an action
        action = player.decide_action()
        if action.require_target:
            target = player.choose_target(self.players)
            print(f"{player.name} decides to {action.name} against {target}")
            status = action.play(player, target)
            print(f"{action.name} was {status} by {target}")
        else:
            print(f"{player.name} decides to {action.name}")
            for reacting_player in self.players:
                if reacting_player == player:
                    continue
                    
            status = action.play(player=player, target=reacting_player)
            print(f"The action was {status} by {reacting_player}")
                
        for ai_player in self.ai_players:
            ai_player.acknowledge_player_action(
                player, action, status, target if target else None
            )
            
            ai_player.acknowledge_game_status(self.players)

    def acknoledge_ai_players(self, player, action, status, target=None):
        for ai_player in self.ai_players:
            ai_player.perceive_action(player, action, target, status)

    def is_game_over(self):
        # Check if the game is over
        alive_players = [p for p in self.players if p.is_alive()]
        return len(alive_players) <= 1


if __name__ == '__main__':
    # Initialize the players
    players = [
        Player("Bob"),
        Player("Shirley"),
        AIPlayer("Guilherme"),
        AIPlayer("Kung Lao"),
    ]

    # Initialize the game
    game = CoupGame(players)

    # Play the game
    game.play()
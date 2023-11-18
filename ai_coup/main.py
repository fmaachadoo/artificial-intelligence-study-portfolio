import random
import logging
import time

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

        return "Successful", None

    def __str__(self):
        return "Income"


class ForeignAid(Action):
    name = "Foreign Aid"
    require_target = False

    @staticmethod
    def play(player, target):
        status = "Successful"

        reacting_player = target

        if target:
            status = reacting_player.react_to_action(
                player=player, action=ForeignAid, target=reacting_player
            )
            if status == "Blocked":
                return status

        player.coins += 2

        return status, None

    def __str__(self):
        return "Foreign Aid"


class Coup(Action):
    name = "Coup"
    require_target = True

    @staticmethod
    def play(player, target):
        player.coins -= 7
        dead_card = target.cards.pop()
        print(f"{target.name} lost {dead_card} card")
        return "Successful", dead_card

    def __str__(self):
        return "Coup"


class Tax(Action):
    name = "Tax"
    require_target = False

    @staticmethod
    def play(player, target=None):
        player.coins += 3

        return "Successful", None

    def __str__(self):
        return "Tax"


class Assassinate(Action):
    name = "Assassinate"
    require_target = True

    @staticmethod
    def play(player, target):
        status = "Successful"

        if target:
            status = target.react_to_action(player=player, action=Assassinate, target=target)
            if status == "Blocked":
                return status, None

        player.coins -= 3
        dead_card = target.cards.pop()

        return status, dead_card

    def __str__(self):
        return "Assassinate"


class Steal(Action):
    name = "Steal"
    require_target = True

    @staticmethod
    def play(player, target):
        status = "Successful"

        if target:
            status = target.react_to_action(player=player, action=Steal, target=target)
            if status == "Blocked":
                return status, None

        remained_coins = target.coins - 2

        # If the target has less than 2 coins, the player can only steal the
        # amount of coins the target has
        if remained_coins < 0:
            player.coins += target.coins
            remained_coins = 0

        target.coins = remained_coins

        return status, None

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

    POSSIBLE_ACTIONS = {
        "Duke": ['Tax', 'Block Foreign Aid'],
        "Assassin": ['Assassinate'],
        "Captain": ['Steal', 'Block Stealing'],
        "Contessa": ['Block Assassination']
    }

    def __init__(self, name, players=[]):
        self.name = name
        self.cards = []
        self.coins = 2
        self.players = players

    def print_status(self):
        print(
            f"{self.name} has {self.coins} coins and [{', '.join(str(card) for card in self.cards)}] cards"
        )

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
        previous_card = None
        if self.coins >= 10:
            return Coup, None

        for retry in range(3):
            card = random.choice(self.cards)

            if card == previous_card:
                continue
            
            previous_card = card

            if card.has_action:
                if card.action == Assassinate and self.coins < 3:
                    print(
                        f"{self.name} doesn't have enough coins to assassinate"
                    )
                    continue

                return card.action, None

        if self.coins >= 7:
            return Coup, None

        return random.choice(self.COMMON_ACTIONS), None

    def perceive_action(self, player, action, influence=None, target=None):
        pass

    def react_to_action(self, player, action, influence=None, target=None):
        if action.name == "Income" or action.name == "Tax":
            return "Successful"

        for influence in self.cards:
            if (
                influence.name == "Captain"
                and action.name == "Steal"
                and target.name == self.name
            ):
                influence.block()
                return "Blocked"

            if (
                influence.name == "Contessa"
                and action.name == "Assassinate"
                and target.name == self.name
            ):
                influence.block()
                return "Blocked"

            if influence == "Duke" and action == "Foreign Aid":
                influence.block()
                return "Blocked"

        if target.name == self.name:
            return "Successful"

    def __str__(self):
        return self.name


class AIPlayer(Player):
    is_artificial_intelligence = True

    def __init__(self, name, players=[]):
        super().__init__(name)
        self.name = f"\033[32mAI {self.name}\033[37m"
        self.logger = logging.getLogger(name)
        self.players = players

    def initialize_players(self, players):
        self.players = players
        self.knowledge = {
            player: {"cards": [], "actions": [], "coins": player.coins}
            for player in players
        }

    def perceive_action(self, player, action, influence=None, target=None):
        self.acknowledge_player_action(action, player, target)

    def get_target_priority(self):
        def sort_key(target):
            return (
                self.knowledge[target]["card_amount"], 
                self.knowledge[target]["coins"]
            )

        return sorted(
            self.players,
            key=sort_key,
            reverse=True,
        )

    def decide_action(self):
        target_list = self.get_target_priority()
        for target in target_list:
            if target.name == self.name:
                continue

            print(
                f"{self.name} is targeting {target.name} because it has "
                f"{target.coins} coins"
            )

            if not target.is_alive():
                print("The target is dead... choosing other target")
                continue

            if self.coins >= 10:
                print(
                    f"{self.name} has 10+ coins and is obligated to coup"
                )
                return Coup, target

            random.shuffle(self.cards)

            for card in self.cards:
                if card.has_action:
                    if (
                        card.action.name == 'Assassinate' and 
                        (
                            self.coins < 3 or 
                            self.target_has(target, "Contessa")
                        )
                    ):
                        print(
                            f"{self.name} knows that can't assassinate "
                            f"{target.name}"
                        )
                        continue
                    
                    if self.coins >= 7:
                        return Coup, target

                    if (
                        card.action.name == 'Steal' and 
                        self.target_has(target, "Captain")
                    ):
                        print(
                            f"{self.name} knows that can't steal "
                            f"from {target.name}"
                        )
                        continue

                    target = (target if card.action.require_target else None)

                    return card.action, target
            
            if self.game_hasnt("Duke"):
                return ForeignAid, None
            
            return Income, None

    def target_has(self, target, card_name):
        return card_name in self.knowledge[target]["cards"]

    def game_hasnt(self, card_name):
        for player in self.players:
            if self.target_has(player, card_name):
                return False
        
        return True

    def react_to_action(self, player, action, influence=None, target=None):
        for influence in self.cards:
            if (
                influence.name == "Captain" and 
                action.name == "Steal" and 
                target and target.name == self.name
            ):  
                influence.block()
                return 'Blocked'
            
            if (
                influence.name == "Contessa"
                and action.name == "Assassinate" and
                target and target.name == self.name
            ):
                influence.block()
                return 'Blocked'

            if influence.name == "Duke" and action.name == "Foreign Aid":
                influence.block()
                return 'Blocked'

        return "Successful"

    def acknowledge_player_action(
        self, player, action, status, target=None, dead_card=None
    ):
        if target and dead_card:
            for action in self.POSSIBLE_ACTIONS[dead_card.__class__.__name__]:
                print(
                    f'{self.name} is removing {action} '
                    f'knowledge from {target.name}'
                )
                try:
                    self.knowledge[target]["actions"].remove(action)
                except ValueError:
                    print(
                        f"{self.name} never saw {target.name} {action}"
                    )
                    pass

            self.knowledge[target]["card_amount"] -= 1

        self.knowledge[player]["actions"].append(action)
        if target:
            print(
                f"{self.name} acknowledged: {player.name} {action} "
                f"{target.name} was {status}"
            )

            if action == "Tax":
                return

            if action == "Income":
                return

            if action == "Assassination":
                if status == "Successful":
                    self.knowledge[target]["actions"].append("Assassinated")
                    print(
                        f"{self.name} acknowledged: {target.name} was assassinated"
                    )
                elif status == "Blocked":
                    self.knowledge[target]["actions"].append(
                        "Block Assassination"
                    )
                    print(
                        f"{self.name} acknowledged: {target.name} blocked {action}"
                    )

            elif action == "Steal":
                if status == "Successful":
                    self.knowledge[target]["actions"].append("Stolen")
                    print(
                        f"{self.name} acknowledged: {target.name} was stolen"
                    )
                elif status == "Blocked":
                    self.knowledge[target]["actions"].append("Block Stealing")
                    print(
                        f"{self.name} acknowledged: {target.name} blocked {action}"
                    )

            elif action == "Foreign Aid":
                if status == "Successful":
                    for player in self.players:
                        self.knowledge[target]["actions"].append(
                            "No block Foreign Aid"
                        )
                    print(
                        f"{self.name} acknowledged: No one blocked Foreign Aid"
                    )
                elif status == "Blocked":
                    self.knowledge[target]["actions"].append(
                        "Block Foreign Aid"
                    )
                    print(
                        f"{self.name} acknowledged: {target.name} blocked {action}"
                    )

        else:
            print(
                f"{self.name} acknowledged: {player.name} {action} was {status}"
            )

        self.clear_duplicated_actions()

    def clear_duplicated_actions(self):
        for player in self.players:
            self.knowledge[player]["actions"] = list(
                set(self.knowledge[player]["actions"])
            )

    def acknowledge_game_status(self, players):
        for player in players:
            self.knowledge[player]["coins"] = player.coins
            self.knowledge[player]["card_amount"] = len(player.cards)

    def predict_game(self):
        print(f'{self.name} is predicting the game')
        for player in self.players:
            if player.name == self.name:
                continue

            self.knowledge[player]['cards'] = self.predict_player_cards(player)

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
                print(
                    f"Since {player.name} played Tax,"
                    f"{self.name} inferred {player.name} has a Duke"
                )
                inferred_cards["Duke"] = 1
            elif action == "Assassinate":
                print(
                    f"Since {player.name} played Assassinate,"
                    f"{self.name} inferred {player.name} has an Assassin"
                )
                inferred_cards["Assassin"] = 1
            elif action == "Steal":
                print(
                    f"Since {player.name} played Steal,"
                    f"{self.name} inferred {player.name} has a Captain"
                )
                inferred_cards["Captain"] = 1
            elif action == "Block Foreign Aid":
                print(
                    f"Since {player.name} blocked Foreign Aid,"
                    f"{self.name} inferred {player.name} has a Duke"
                )
                inferred_cards["Duke"] = 1
            elif action == "Block Assassination":
                print(
                    f"Since {player.name} blocked Assassination,"
                    f"{self.name} inferred {player.name} has a Contessa"
                )
                inferred_cards["Contessa"] = 1
            elif action in ["Foreign Aid", "Income"]:
                print(
                    f"Since {player.name} played {action},"
                    f"{self.name} inferred {player.name} doesnt have a Duke"
                )
                inferred_cards["Duke"] = 0
            elif action == "Assassinated":
                print(
                    f"Since {player.name} was assassinated,"
                    f"{self.name} inferred {player.name} doesnt have a "
                    f"Contessa"
                )
                inferred_cards["Contessa"] = 0
            elif action == "Stolen":
                print(
                    f"Since {player.name} was stolen,"
                    f"{self.name} inferred {player.name} doesnt have a "
                    f"Captain"
                )
                inferred_cards["Captain"] = 0
            elif action == 'No block Foreign Aid':
                print(
                    f"Since no one blocked Foreign Aid,"
                    f"{self.name} inferred {player.name} doesnt have a "
                    f"Duke"
                )
                inferred_cards["Duke"] = 0
            elif action == 'Block Stealing':
                print(
                    f"Since {player.name} blocked Stealing,"
                    f"{self.name} inferred {player.name} has a Captain"
                )
                inferred_cards["Captain"] = 1

        cards = filter(lambda x: x[1] > 0, inferred_cards.items())

        # Find the two most likely cards
        sorted_cards = sorted(cards, key=lambda x: x[1], reverse=True)
        
        most_likely_cards = [card[0] for card in sorted_cards[:2]]

        print(
            f"{self.name} inferred, as a final guess, "
            f"that {player.name} has {most_likely_cards}"
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

            print("\n--------- PLAYERS ----------")
            for player in self.players:
                player.print_status()
            print("----------------------------\n")

            # time.sleep(5)

            self.next_turn()
        else:
            for player in self.players:
                if player.is_alive():
                    print(f"{player} won!")

    def take_turn(self, player):
        target = None
        dead_card = None

        # Player takes an action
        action, target = player.decide_action()
        if action.require_target:
            if not target:
                target = player.choose_target(self.players)
            print(f"{player.name} decides to {action.name} against {target}")
            status, dead_card = action.play(player, target)
            print(f"{action.name} was {status} by {target}")
        else:
            print(f"{player.name} decides to {action.name}")
            for reacting_player in self.players:
                if reacting_player == player:
                    continue

                status = reacting_player.react_to_action(
                    player=player, action=action, target=reacting_player
                )

                if status == "Blocked":
                    print(f"The action was {status} by {reacting_player}")
                    break

            else:
                print("No one blocked the action")
                status, dead_card = action.play(player=player, target=None)

            print(f"The action was {status} by {reacting_player}")

        for ai_player in self.ai_players:
            if not ai_player.is_alive():
                continue
            print("\033[02m")
            ai_player.acknowledge_player_action(
                player, action.name, status, target if target else None, dead_card
            )

            ai_player.acknowledge_game_status(self.players)

            ai_player.predict_game()
            print("\033[0m")

    def acknoledge_ai_players(self, player, action, status, target=None):
        for ai_player in self.ai_players:
            ai_player.perceive_action(player, action, target, status)

    def is_game_over(self):
        # Check if the game is over
        alive_players = [p for p in self.players if p.is_alive()]
        return len(alive_players) <= 1


if __name__ == "__main__":
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

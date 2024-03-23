@startuml
class GameState {
 - players: Player[]
 - spectators: Spectator
 - sheriff_deck: Card[]
 - bandit_deck: Card[]
 - used_deck: Card[]
 - common_deck: Card[]
 - sheriff_characters: Character[]
 - bandit_characters: Character[]
}

class Spectator {
 # name: String
}

class Player extends Spectator {
 - cards_hold: Card[]
 - characters: Character[]
}

class Card {
 - name: String
 - id: Integer
}

class Character extends Card {
 - hit_points: Integer
}

Player "1" -- "*" Card
Player "1" -- "*" Character
@enduml
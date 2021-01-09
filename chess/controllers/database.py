from chess.models.actors import Actor
from chess.models.game import Tournament
from chess.utils.conversion import str_to_date
from tinydb import TinyDB


def deserialiaze_actor(serialiazed_actor):
    actor = Actor(serialiazed_actor['last_name'],
                  serialiazed_actor['first_name'],
                  str_to_date(serialiazed_actor['birthdate']),
                  serialiazed_actor['gender'],
                  serialiazed_actor['rank'])
    actor.dict_to_actor(serialiazed_actor)
    return actor


def deserialize_player(serialiazed_player):
    actor = deserialiaze_actor(serialiazed_player['actor'])
    player = Player(actor, serialiazed_player['tournament_id'], serialiazed_player['player_id'])
    player.dict_to_player(serialiazed_player)
    return player


def deserialize_match():
    pass


def deserialize_round():
    pass


def deserialize_tournament():
    pass


class DataBaseHandler:
    def __init__(self, database):
        self.database = database

    def export_actor(self, actor):
        actors_table = self.database.table('actors')
        dictio = actor.actor_to_dict()
        actors_table.insert(dictio)

    def export_tournament(self, tournament, step):
        pass

    def import_actors(self):
        db = TinyDB('db.json')
        actors_table = db.table('actors')
        serialized_actors = actors_table.all()
        actors = []
        for value in serialized_actors:
            actor = deserialiaze_actor(value)
            actors.append(actor)
        return len(serialized_actors), actors

    def import_tournament(self):
        pass


if __name__ == '__main__':
    import datetime
    from chess.models.actors import Actor, Player

    handler = DataBaseHandler(TinyDB('db.json'))
    handler.database.table('actors').truncate()

    print("\n ### Test acteur ### \n")
    """ Test Acteur """

    acteur1 = Actor("Skywalker", "Anakin", datetime.date(41, 5, 6), "M", 8)       # 2
    acteur2 = Actor("Skywalker", "Luke", datetime.date(19, 12, 7), "M", 21)       # 3
    acteur3 = Actor("Organa", "Leia", datetime.date(19, 12, 7), "F", 143)         # 8
    acteur4 = Actor("Tano", "Ahsoka", datetime.date(36, 11, 22), "F", 35)         # 5
    acteur5 = Actor("Yoda", "Maître", datetime.date(896, 10, 15), "M", 3)         # 1
    acteur6 = Actor("Palpatine", "Sheev", datetime.date(84, 2, 25), "M", 27)      # 4
    acteur7 = Actor("Kashyyyk", "Chewbacca", datetime.date(200, 8, 31), "M", 112) # 7
    acteur8 = Actor("Solo", "Han", datetime.date(34, 7, 16), "M", 107)            # 6
    acteurs = [acteur1, acteur2, acteur3, acteur4, acteur5, acteur6, acteur7, acteur8]

    acteur1.tournaments = ["00002200", "00002201"]
    for k in acteurs:
        handler.export_actor(k)
    # print(vars(acteur1))
    acters = handler.import_actors()
    print(acters)

    """Verification"""
    print(vars(acteur1))
    print(vars(acters[1][0]))

    """ Test Joueur """
    print("\n ### Test joueur ### \n")
    joueur1 = Player(acteur1, "00000001", 1)
    joueur2 = Player(acteur2, "00000001", 2)
    joueur3 = Player(acteur3, "00000001", 3)
    joueur4 = Player(acteur4, "00000001", 4)
    joueur5 = Player(acteur5, "00000001", 5)
    joueur6 = Player(acteur6, "00000001", 6)
    joueur7 = Player(acteur7, "00000001", 7)
    joueur8 = Player(acteur8, "00000001", 8)
    joueurs = [joueur1, joueur2, joueur3, joueur4, joueur5, joueur6, joueur7, joueur8]

    """ serialize """
    j3 = joueur3.player_to_dict()
    #print("\n dico2:", dico2)

    """ deserialize """
    # acteur03 = deserialiaze_actor(dico2['actor'])
    # joueur03 = Player(acteur03, dico2['tournament_id'], dico2['player_id'])
    # joueur03.dict_to_player(dico2)
    joueur03 = deserialize_player(j3)
    print(vars(joueur3))
    print(vars(joueur03))

    print(vars(joueur3.actor))
    print(vars(joueur03.actor))

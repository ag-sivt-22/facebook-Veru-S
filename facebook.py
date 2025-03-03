from __future__ import annotations
from dataclasses import dataclass
from collections import deque

@dataclass
class User:
    name: str
    friends: list[User]

    def __init__(self, name: str) -> None:
        self.name = name
        self.friends = []

class Facebook:
    def __init__(self) -> None:
        self._users: dict[str, User] = {}

    def pridej_uzivatel(self, name: str) -> None:
        if name not in self._users:
            self._users[name] = User(name)

    def pridej_znamost(self, name1: str, name2: str) -> None:
        if name1 not in self._users or name2 not in self._users:
            return
        user1, user2 = self._users[name1], self._users[name2]
        if user2 not in user1.friends:
            user1.friends.append(user2)
            user2.friends.append(user1)

#dál domácí úkol:
    def jak_daleko(self, name1: str, name2: str) -> int | None:
        if name1 not in self._users or name2 not in self._users:
            return None
        if name1 == name2:
            return 0
        rada = deque([(self._users[name1], 0)])
        visited = set()  #The set() function creates a set object. The items in a set list are unordered, so it will appear in random order.
        while rada:
            current, distance = rada.popleft()
            if current.name == name2:
                return distance
            visited.add(current.name)
            for friend in current.friends:
                if friend.name not in visited:
                    rada.append((friend, distance + 1))
        return None

    def zobraz_pratele(self, name: str):
        if name in self._users:
            pratele = [friend.name for friend in self._users[name].friends]
            print(f"Přátelé {name}: {', '.join(pratele) if pratele else 'žádní'}")

#tvoření facebooku:
fb = Facebook()
jmena = ["Adam", "Beata", "Cyril", "Dana", "Emil", "František", "Gabriela", "Hana", "Ivan", "Jana",
         "Karel", "Lenka", "Marek", "Nina", "Ondřej", "Petra", "Quentin", "Radka", "Stanislav", "Tereza",
         "Urbán", "Veronika", "Walter", "Xenie", "Yvona", "Zdeněk", "Alex", "Blanka", "Cecilie", "David"]

for jmeno in jmena:
    fb.pridej_uzivatel(jmeno)

znamosti = [("Adam", "Beata"), ("Adam", "Cyril"), ("Beata", "Dana"), ("Cyril", "Emil"), ("Cyril", "František"),
            ("Dana", "Gabriela"), ("Emil", "Hana"), ("František", "Ivan"), ("Gabriela", "Jana"), ("Hana", "Karel"),
            ("Ivan", "Lenka"), ("Jana", "Marek"), ("Karel", "Nina"), ("Lenka", "Ondřej"), ("Marek", "Petra"),
            ("Nina", "Quentin"), ("Ondřej", "Radka"), ("Petra", "Stanislav"), ("Quentin", "Tereza"),
            ("Radka", "Urbán"), ("Stanislav", "Veronika"), ("Tereza", "Walter"), ("Urbán", "Xenie"),
            ("Veronika", "Yvona"), ("Walter", "Zdeněk"), ("Xenie", "Alex"), ("Yvona", "Blanka"),
            ("Zdeněk", "Cecilie"), ("Alex", "David"), ("Blanka", "Adam")]

for clovek1, clovek2 in znamosti:
    fb.pridej_znamost(clovek1, clovek2)

print(fb.jak_daleko("Adam", "David"))
print(fb.jak_daleko("Adam", "Tereza"))
print(fb.jak_daleko("Adam", "Xenie"))
print(fb.jak_daleko("Adam", "Adam"))
print(fb.jak_daleko("Adam", "Neexistuje"))

fb.zobraz_pratele("Adam")
fb.zobraz_pratele("David")

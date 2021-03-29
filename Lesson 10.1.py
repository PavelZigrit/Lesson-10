import requests
import time

heroes_list = []


class SuperHero:
    def __init__(self, name):
        self.token = "2619421814940190"
        self.url = "https://superheroapi.com/api/"
        self.name = name
        self.intelligence = self.get_intel_of_hero()
        heroes_list.append(self)

    def get_intel_of_hero(self):
        response = requests.get(self.url + self.token + "/search/" + self.name, timeout=5)
        time.sleep(0.3)
        if len(response.json()) > 2:
            hero_stats = [stats for stats in response.json()["results"] if stats["name"] == self.name]
            return int(hero_stats[0]["powerstats"]["intelligence"])
        else:
            return 0


def high_intel_of_heroes(hero_list):
    hero_intel_dict = {}
    for hero in hero_list:
        hero_intel_dict[hero.name] = hero.intelligence
    return f"Самый умный супергерой - {[key for key, value in hero_intel_dict.items() if value == max(hero_intel_dict.values())][0]}," \
           f" его интеллект равен {[value for key, value in hero_intel_dict.items() if value == max(hero_intel_dict.values())][0]}"


Hulk = SuperHero("Hulk")
Captain_America = SuperHero("Captain America")
Thanos = SuperHero("Thanos")
asd = SuperHero("asd")

print(high_intel_of_heroes(heroes_list))

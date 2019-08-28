
print("|-----------------------------------------------------------------|")
_desc = '''|\tEverything has its wonders, even silence and darkness.        |'''
_author = '''\n|\t\t\t\t\t\t\t\t - Helen Keller                   |'''
print(_desc, _author)
print("|-----------------------------------------------------------------|")


class GalaxyMap(object):

    def __init__(self, info_about_planets, info_about_stars):
        self.planets = info_about_planets
        self.stars = info_about_stars

    @classmethod
    def instance(cls):
        p1 = {"Mercury": {"Tell": 1,
                          "Distance": "\nThe nearest distance from Earth is 82 million kilometres.",
                          "Mass": 2}, "Venus": [], "Earth": [], "Mars": [],
              "Jupiter": [], "Saturn": [], "Uranus": [], "Neptune": [], "Pluto": []}
        s1 = {"Sun": [], "Proxima Centaurus": [],
              "Alpha Centaurus": [], "Luman 16": [],
              "Barnard Star": [], "Arcturus": {"Tell":
              "\nThe Arcturus is one of the fourth-brightest star in the night sky!",
                                               "Distance": "\nThe distance from Earth is 36,7 light years!",
                                               "Mass": f"\nThe mass of the Arcturus is 1,5 Sun masses.",
                                               "Temperature": f"\nThe temperature of the Arcturus is {4300} K. ",
                                               "Age": "\nThe age of Arcturus is 8-10 billion years"},
              "Betelgeuse": ["Betelgeuse - a big star!"], "Antares": [],
              "Vega": []}
        return cls(p1, s1)

    def request(self):
        __commands__ = ["Tell", "Mass", "Distance", "Age", "Temperature"]
        __stop__ = ["Break", "E", "Exit"]

        user_input = str(input("\nAsk me about a planet or a star --> "))
        analyze = user_input.split()

        if any(i.capitalize() in __stop__ for i in analyze):
            return "[Program Finished]"

        checking = ''.join([i.capitalize() for i in analyze if i.capitalize() in __commands__])

        for space_object in analyze:
            space_object = space_object.capitalize()

            if space_object in self.stars:

                if checking:
                    print("\n_________________________________________________________")
                    print(self.stars[space_object][checking])
                    print("__________________________________________________________")

                else:
                    print(self.stars[space_object]["Desc"])

            if space_object in self.planets:
                print(self.planets[space_object])

        return self.request()


obj = GalaxyMap.instance()
obj.request()

























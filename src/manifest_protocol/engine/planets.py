from manifest_protocol.engine.dice import dice


def to_hex(value: int) -> str:
    if value < 0:
        value = 0
    elif value > 16:
        value = 16

    if value < 10:
        return str(value)
    return chr(ord("A") + value - 10)


class Planet:
    def __init__(self):
        self.starport = "X"
        self.size = 0
        self.atmosphere = 0
        self.hydrographics = 0
        self.population = 0
        self.government = 0
        self.law_level = 0
        self.tech_level = 0

    def generate(self):
        # Size
        self.size = dice(2) - 2

        # Atmosphere
        if self.size == 0:
            self.atmosphere = 0
        else:
            self.atmosphere = dice(2) - 7 + self.size
        if self.atmosphere > 15:
            self.atmosphere = 15

        # Hydrographics
        if self.atmosphere in [0, 1, 10, 11, 12]:
            hydrographics_dm = -4
        elif self.atmosphere == 14:
            hydrographics_dm = -2
        else:
            hydrographics_dm = 0

        if self.size in [0, 1]:
            self.hydrographics = 0
        else:
            self.hydrographics = dice(2) - 7 + self.size + hydrographics_dm

        # Population
        if self.atmosphere >= 10:
            population_dm = -2
        elif self.atmosphere == 6:
            population_dm = 3
        elif self.atmosphere in [5, 8]:
            population_dm = 1
        elif self.hydrographics == 0 and self.atmosphere < 3:
            population_dm = -1
        else:
            population_dm = 0
        self.population = dice(2) - 2 + population_dm

        # Government
        self.government = dice(2) - 7 + self.population

        # Law Level
        if self.government == 0:
            self.law_level = 0
        else:
            self.law_level = dice(2) - 7

        if self.law_level < 0:
            self.law_level = 0
        if self.law_level > 10:
            self.law_level = 10

        # Starport
        starport_roll = dice(2) - 7 + self.population
        if starport_roll <= 2:
            self.starport = "X"
        elif starport_roll <= 4:
            self.starport = "E"
        elif starport_roll <= 6:
            self.starport = "D"
        elif starport_roll <= 8:
            self.starport = "C"
        elif starport_roll <= 10:
            self.starport = "B"
        else:
            self.starport = "A"

        # Tech Level ... hold on to your butts
        if self.starport == "A":
            starport_tech_dm = 6
        elif self.starport == "B":
            starport_tech_dm = 4
        elif self.starport == "C":
            starport_tech_dm = 2
        elif self.starport == "X":
            starport_tech_dm = -4
        else:
            starport_tech_dm = 0

        if self.size <= 1:
            size_tech_dm = 2
        elif self.size <= 4:
            size_tech_dm = 1
        else:
            size_tech_dm = 0

        if self.atmosphere <= 3 or self.atmosphere >= 10:
            atmosphere_tech_dm = 1
        else:
            atmosphere_tech_dm = 0

        if self.hydrographics in [0, 9]:
            hydrographics_tech_dm = 1
        elif self.hydrographics == 10:
            hydrographics_tech_dm = 2
        else:
            hydrographics_tech_dm = 0

        if self.population in [1, 2, 3, 4, 5, 9]:
            population_tech_dm = 1
        elif self.population == 10:
            population_tech_dm = 2
        elif self.population == 11:
            population_tech_dm = 3
        elif self.population == 12:
            population_tech_dm = 4
        else:
            population_tech_dm = 0

        if self.government in [0, 5]:
            government_tech_dm = 1
        elif self.government == 7:
            government_tech_dm = 2
        elif self.government in [13, 14]:
            government_tech_dm = -2
        else:
            government_tech_dm = 0

        self.tech_level = (
            dice(1)
            + starport_tech_dm
            + size_tech_dm
            + atmosphere_tech_dm
            + hydrographics_tech_dm
            + population_tech_dm
            + government_tech_dm
        )

        if (
            self.hydrographics in [0, 10]
            and self.population >= 6
            and self.tech_level < 4
        ):
            self.tech_level = 4
        if self.atmosphere in [4, 7, 9] and self.tech_level < 5:
            self.tech_level = 5
        if self.atmosphere in [0, 1, 2, 3, 10, 11, 12] and self.tech_level < 7:
            self.tech_level = 7
        if (
            self.atmosphere in [13, 14]
            and self.hydrographics == 10
            and self.tech_level < 7
        ):
            self.tech_level = 7

    @classmethod
    def random(cls):
        planet = cls()
        planet.generate()
        return planet

    def to_uwp_string(self):
        fields = [
            self.starport,
            to_hex(self.size),
            to_hex(self.atmosphere),
            to_hex(self.hydrographics),
            to_hex(self.population),
            to_hex(self.government),
            to_hex(self.law_level),
            "-",
            to_hex(self.tech_level),
        ]
        return "".join(fields)


planet = Planet.random()
print(planet.to_uwp_string())

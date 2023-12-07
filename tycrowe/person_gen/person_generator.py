import random
import uuid

names = []
good_traits = {
    "Analytical": 3,
    "Collaborative": 2,
    "Communicative": 2,
    "Creative Thinker": 2,
    "Detail-Oriented": 3,
    "Diplomatic": 2,
    "Empathetic": 3,
    "Flexible": 2,
    "Innovative": 2,
    "Leadership": 4,
    "Logical": 3,
    "Mediator": 2,
    "Organized": 2,
    "Problem-Solver": 3,
    "Reliable": 3,
    "Resourceful": 2,
    "Strategic": 3,
    "Supportive": 2,
    "Tech-Savvy": 2,
    "Time-Manager": 3,
}
bad_traits = {
    "Resistant to Change": -2,
    "Procrastinator": -3,
    "Indecisive": -2,
    "Impulsive": -1,
    "Rigid": -2,
    "Overly Critical": -2,
    "Passive": -1,
    "Conflict-Averse": -2,
    "Easily Distracted": -1,
    "Perfectionist (to a fault)": -1,
    "Dismissive": -2,
    "Non-communicative": -2,
    "Overly Competitive": -1,
    "Unreliable": -3,
    "Defensive": -1,
    "Micromanaging": -2,
    "Pessimistic": -1,
    "Unempathetic": -2,
    "Stubborn": -1,
    "Aloof": -1,
    "Impatient": -1,
    "Intolerant": -2,
    "Narrow-Minded": -2,
    "Uncooperative": -2,
    "Overbearing": -1,
    "Moody": -1,
    "Skeptical": -1
}
traits = {**good_traits, **bad_traits}
NUM_GOOD_TRAITS_PER_PERSON = 3
NUM_BAD_TRAITS_PER_PERSON = 2

class Trait:
    name: str
    rating: int
    good: bool

    def __init__(self, name: str, rating: int, good: bool):
        self.name = name
        self.rating = rating
        self.good = good

class_good_traits = []
class_bad_traits = []
for trait, rating in traits.items():
    class_good_traits.append(Trait(trait, rating, True)) if rating > 0 else class_bad_traits.append(Trait(trait, rating, False))

class Person:
    name: str
    traits: list[Trait]
    free_hours_a_week: int

    def __init__(self, name: str, traits: list[Trait] = [], free_hours_a_week: int = random.randint(0, 168)):
        self.name = name
        self.free_hours_a_week = free_hours_a_week
        self.traits = traits

    def calculate_score(self):
        score = 0
        for trait in self.traits:
            score += trait.rating
        return score

    def to_csv_row(self):
        return f"""{self.name},{';'.join([f"{trait.name}[{trait.rating}]" for trait in self.traits])},{self.free_hours_a_week}\n"""


with open("tycrowe/person_gen/first_names.txt", "r") as f:
    for line in f:
        names.append(line.strip())

with open("tycrowe/person_gen/people.csv", "w") as f:
    f.write("Name,Traits,Free Hours\n")
    chosen_names = []
    for i in range(0, 2000):
        name = names[random.randint(0, len(names) - 1)]
        while name in chosen_names:
            name = names[random.randint(0, len(names) - 1)]

        # Choose NUM_GOOD_TRAITS_PER_PERSON good traits and NUM_BAD_TRAITS_PER_PERSON bad traits using sample
        traits = random.sample(class_good_traits, NUM_GOOD_TRAITS_PER_PERSON) + random.sample(class_bad_traits, NUM_BAD_TRAITS_PER_PERSON)
        free_hours = random.randint(0, 40)
        person = Person(name, traits, free_hours)
        f.write(person.to_csv_row())
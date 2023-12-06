import random
import uuid

names = []
traits = {
    "Analytical": "Able to analyze complex problems and data.",
    "Collaborative": "Works well with others, promotes teamwork.",
    "Communicative": "Strong in verbal and written communication.",
    "Creative Thinker": "Comes up with innovative solutions and ideas.",
    "Detail-Oriented": "Pays attention to the small but important details.",
    "Diplomatic": "Skilled in handling sensitive situations or negotiations.",
    "Empathetic": "Understands and shares the feelings of others.",
    "Flexible": "Adapts to changing situations and ideas.",
    "Innovative": "Brings new and original ideas to the table.",
    "Leadership": "Able to guide and inspire a team.",
    "Logical": "Thinks clearly and reasons well.",
    "Mediator": "Resolves conflicts and builds consensus.",
    "Organized": "Keeps tasks and projects in order.",
    "Problem-Solver": "Identifies and resolves issues effectively.",
    "Reliable": "Dependable and consistent in work and attendance.",
    "Resourceful": "Finds ways to overcome challenges.",
    "Strategic": "Plans effectively for the long term.",
    "Supportive": "Provides help and encouragement to teammates.",
    "Tech-Savvy": "Proficient with technology and technical skills.",
    "Time-Manager": "Manages time efficiently and meets deadlines."
}
trait_count_per_person = 3


class Person:
    unique_id: str
    name: str
    traits: list[str]
    free_hours_a_week: int

    def __init__(self, name: str, traits: list[str], free_hours_a_week: int):
        self.unique_id = uuid.uuid4()
        self.name = name
        self.traits = traits
        self.free_hours_a_week = free_hours_a_week

    def to_csv_row(self):
        return f"{self.unique_id},{self.name},{';'.join(self.traits)},{self.free_hours_a_week}\n"


with open("tycrowe/first_names.txt", "r") as f:
    for line in f:
        names.append(line.strip())

with open("tycrowe/people.csv", "w") as f:
    f.write("Name,Traits,Free Hours\n")
    chosen_names = []
    keys = traits.keys()
    for i in range(0, 2000):
        name = names[random.randint(0, len(names) - 1)]
        while name in chosen_names:
            name = names[random.randint(0, len(names) - 1)]
        traits = random.sample(list(keys), trait_count_per_person)
        free_hours = random.randint(0, 168)
        person = Person(name, traits, free_hours)
        f.write(person.to_csv_row())
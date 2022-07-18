import logging
import pandas as pd
from random import randint


# TODO: CHANGE DIFFICULTY PARAMETER TO A RANGE OF INTEGERS
# TODO: ADJUST question_statistics.csv FILEPATH
class Interactions:
    def __init__(self, parent_dir: str = "../Registry"):
        self.statistics_filepath = parent_dir + r"/question_statistics.csv"

    def get_random_question_from_parameters(self, discipline: str, area: str = None, subject: str = None,
                                            difficulty_level: int = None):
        with open(self.statistics_filepath, "r") as file:
            questions_df = pd.read_csv(file, sep=";")

        if type(discipline) is not str:
            logging.exception(f"Discipline passed as {type(discipline)} type")
            raise TypeError("Discipline must be passed as a string")

        filtered_df = questions_df.loc[questions_df.discipline == discipline]
        if area is not None:
            filtered_df = filtered_df.loc[filtered_df.area == area]
        if subject is not None:
            filtered_df = filtered_df.loc[filtered_df.subject == subject]
        if difficulty_level is not None:
            filtered_df = filtered_df.loc[filtered_df.difficulty_level == difficulty_level]

        available_indexes = filtered_df.shape[0] - 1

        if available_indexes < 0:
            logging.exception(f"No questions available for {discipline}/{area}/{subject}")
            raise LookupError("There are no questions that satisfy the search criteria")

        random_question = filtered_df.iloc[randint(0, available_indexes)].question_id

        return random_question


if __name__ == "__main__":
    interactions = Interactions(parent_dir="../Registry")
    random_question = interactions.get_random_question_from_parameters(discipline="FÍSICA")
    print(random_question)
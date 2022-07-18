import logging
import pandas as pd
from random import randint
from typing import Tuple


class Interactions:
    def __init__(self, parent_dir: str = "../Registry"):
        self.statistics_filepath = parent_dir + r"/question_statistics.csv"

    def get_random_question_from_parameters(self, discipline: str, area: str = None, subject: str = None,
                                            difficulty_level: Tuple[int,int] = (1, 5)) -> str:
        """
        Generate a random question from the passed parameters.
        The only parameter required is discipline, the others are optional.
        If there isn't a question that fits the filters, a LookupError will be raised.
        :param discipline:
        :param area:
        :param subject:
        :param difficulty_level: tuple of integers representing the min level and the max level : (min, max)
        :return: string representation of the question_id
        """
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
            if type(difficulty_level) is not tuple:
                logging.exception(f"difficulty_level passed as type {type(difficulty_level)}")
                raise TypeError("difficulty_level must be a tuple of integers")

            if difficulty_level[0] is not None:
                filtered_df = filtered_df.loc[filtered_df.difficulty_level >= difficulty_level[0]]
            if difficulty_level[1] is not None:
                filtered_df = filtered_df.loc[filtered_df.difficulty_level <= difficulty_level[1]]

        available_indexes = filtered_df.shape[0] - 1

        if available_indexes < 0:
            logging.exception(f"No questions available for {discipline}/{area}/{subject}")
            raise LookupError("There are no questions that satisfy the search criteria")

        random_question_id = filtered_df.iloc[randint(0, available_indexes)].question_id

        return random_question_id


if __name__ == "__main__":
    interactions = Interactions(parent_dir="../Registry")
    random_question = interactions.get_random_question_from_parameters(discipline="TESTING")
    print(type(random_question))
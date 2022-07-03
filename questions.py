import typing
from dataclasses import dataclass
from typing import Optional, TypedDict
import logging
import random
import string
import json
import os


class QuestionID:
    """
    1) Generate a new ID for a question upon entry.
    2) Check if the new ID already exists.
    3) Write the new ID on the master file for later conference.
    """

    def __init__(self):
        self.master_filename = "ids_master.txt"

        _loop_counter = 0
        while True:
            _loop_counter += 1
            if _loop_counter >= 100:
                raise TimeoutError("Too many checks for the generated ID")
            self.generated_id = self.generate_random_id()
            if self.check_if_id_exists(self.generated_id):
                continue
            else:
                break
        self.add_new_id_to_master_file(self.generated_id)

    def __str__(self):
        return self.generated_id

    def __repr__(self):
        return self.generated_id

    @staticmethod
    def generate_random_id(id_length: int = 6) -> str:
        """
        Generate a random lowercase ASCII string with {id_length} cases.
        :param id_length: number of cases of the new ID to be generated.
        :return: String of the New ID
        """
        letters = string.ascii_lowercase
        new_id = ''.join(random.choice(letters) for i in range(id_length))

        return new_id

    def check_if_id_exists(self, new_id: str) -> bool:
        """
        Open the master txt file (that contains all the generated IDs) and
        verify if the newly generated ID already exists.
        :param new_id: generated ID to verify
        :return: Boolean value (True if the ID already exists)
        """
        with open(self.master_filename, 'r') as ids:
            lines = ids.readlines()
            if new_id in lines or f'{new_id}\n' in lines:
                ids.close()
                return True
            else:
                ids.close()
                return False

    def add_new_id_to_master_file(self, new_id: str) -> None:
        """
        After the ID has been checked, add it to the master txt file.
        :return: None
        """
        with open(self.master_filename, "a") as ids:
            ids.write(f'{new_id}\n')
            ids.close()

        logging.info(f"{new_id} added to the master file")
        return None


class HTMLString(str):
    """
    Baseclass for HMTL Strings (both on the question text and alternatives).
    """
    pass


class AlternativeModel(TypedDict):
    """
    Baseclass for each alternative dict.
    Each and every question must consist of 4 different alternatives.
    The right answer will be based on the adequate key (A-D).
    """
    A: HTMLString
    B: HTMLString
    C: HTMLString
    D: HTMLString


class OldExamModel(TypedDict):
    """
    Baseclass for each Exam description.
    It's not a required parameter, but if chosen to be added, must follow this specific standard.
    """
    exam_name: str
    exam_year: int


@dataclass
class BaseQuestionModel:
    """
    Class for formatting new questions and later turning each entry into its own JSON file.
    """

    question_text: HTMLString
    alternatives: AlternativeModel
    exam_description: Optional[OldExamModel] = None
    difficulty_level: int = 3
    question_id = QuestionID()
    has_auxiliary_image: bool = False

    def __post_init__(self):
        """
        Run all applicable validations on data upon entry.
        :return: None
        """
        self.question_id = str(self.question_id)
        if self.difficulty_level not in range(1, 6):
            logging.exception(f"Difficulty level entered ({self.difficulty_level}) outside of the desired range.")
            raise ValueError("Difficulty level must be an integer between 1 and 5.")

        logging.info(f"QUESTION of ID {self.question_id} generated")


def export_into_json(generated_question: BaseQuestionModel, parent_dir: str = "Questions") -> None:
    """
    Create a JSON file with the new question ID as the filename.
    :return: None
    """
    root_folder = parent_dir
    question_id = generated_question.question_id
    json_file = json.dumps(generated_question.__dict__)

    with open(f"{root_folder}/{question_id}.json", "w") as file:
        file.write(json_file)

    logging.info(f"{question_id}.json file created")

    return None


def create_questions_folder() -> None:
    os.makedirs("Questions", exist_ok=True)
    return None


if __name__ == "__main__":
    new_question = BaseQuestionModel(
        difficulty_level=1,
        question_text='Quinto é 2 + 2?',
        alternatives={"A": "23",
                      "B": "4",
                      "C": "6",
                      "D": "5"}
    )
    # export_into_json(new_question)

    # print(id(new_question))
    create_questions_folder()
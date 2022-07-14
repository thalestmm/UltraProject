from dataclasses import dataclass
from typing import Optional
import pandas as pd
import logging
import random
import string
import json
import os

# LOCAL MODULES
import disciplines


# TODO: CHANGE REGISTRY FILE TO CSV FORMAT AND USE PANDAS TO HANDLE EXISTING IDs
class QuestionID:
    """
    1) Generate a new ID for a question upon entry.
    2) Check if the new ID already exists.
    3) Write the new ID on the master file for later conference.
    """

    def __init__(self):
        self.master_filepath = "Registry/ids_master.txt"

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
        with open(self.master_filepath, 'r') as ids:
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
        with open(self.master_filepath, "a") as ids:
            ids.write(f'{new_id}\n')
            ids.close()

        logging.info(f"{new_id} added to the master file")
        return None


# TODO: EVALUATE CHANGING THE PARAGRAPH TAGS TO SOME INLINE VALUES (MAYBE SPAN)
@dataclass
class HTMLString:
    """
    Baseclass for HMTL Strings (both on the question text and alternatives).
    """
    content: str

    def __repr__(self):
        return self.add_paragraph_tags(self.content)

    @staticmethod
    def add_paragraph_tags(text: str) -> str:
        return f"<p>{text}</p>"


@dataclass
class AlternativeModel:
    """
    Baseclass for each alternative dict.
    Each and every question must consist of 4 different alternatives.
    The right answer will be based on the adequate key (A-D).
    """
    A: HTMLString
    B: HTMLString
    C: HTMLString
    D: HTMLString
    answer: str

    def __post_init__(self):
        available_answers = ["A", "B", "C", "D"]

        self.answer = self.answer.upper()

        if self.answer not in available_answers:
            logging.exception("Answer provided is not available")
            raise ValueError("Answer must be either A, B, C or D")


@dataclass
class OldExamModel:
    """
    Baseclass for each Exam description.
    It's not a required parameter, but if chosen to be added, must follow this specific standard.
    """
    exam_name: str
    exam_year: int

    def __post_init__(self):
        if type(self.exam_year) is not int:
            logging.exception(f"'{self.exam_year}' value entered is not an integer ")
            raise ValueError("Exam Year must be an integer")

    def __repr__(self):
        if self.exam_name is None and self.exam_year is None:
            # This means there wasn't an Old Exam entry
            return None


@dataclass
class BaseQuestionModel:
    """
    Class for formatting new questions and later turning each entry into its own JSON file.
    """

    question_text: HTMLString
    alternatives: AlternativeModel
    discipline: str
    area: str
    subject: Optional[str] = None
    exam_description: Optional[OldExamModel] = None
    difficulty_level: int = 3
    question_id = QuestionID()
    has_auxiliary_image: bool = False
    has_solution_image: bool = False

    def __post_init__(self):
        """
        Run all applicable validations on data upon entry.
        :return: None
        """
        self.question_id = str(self.question_id)

        if int(self.difficulty_level) not in range(1, 6):
            logging.exception(f"Difficulty level entered ({self.difficulty_level}) outside of the desired range.")
            raise ValueError("Difficulty level must be an integer between 1 and 5.")

        self.discipline = self.discipline.upper()
        available_disciplines = disciplines.get_all_discipline_names()

        if self.discipline not in available_disciplines:
            logging.exception(f"'{self.discipline}' discipline not registered")
            raise ValueError("Entered discipline not registered in the Dependencies Folder")

        self.area = self.area.upper()
        discipline_areas = disciplines.get_all_areas_from_discipline(self.discipline)

        if self.area not in discipline_areas:
            logging.exception(f"'{self.area}' area not registered in {self.discipline}")
            raise ValueError("Entered area not registered in the respective Discipline Folder")

        area_subjects = disciplines.get_all_subjects_from_area(self.discipline, self.area)

        if self.subject not in area_subjects and self.subject is not None:
            logging.exception(f"'{self.subject}' subject not registered in {self.discipline}/{self.area}")
            raise ValueError("Entered subject not registered in the respective Discipline Folder")

        logging.info(f"QUESTION of ID {self.question_id} generated")

    def get_statistic_params(self):
        return {
            "question_id": self.question_id,
            "discipline": self.discipline,
            "area": self.area,
            "subject": self.subject,
            "difficulty_level": self.difficulty_level
        }


def insert_new_question_into_master_file(generated_question: BaseQuestionModel, parent_dir: str = "Registry") -> None:
    data = generated_question.get_statistic_params()

    filepath = parent_dir + "/question_statistics.csv"

    questions_df = pd.read_csv(filepath, sep=";")

    questions_df = questions_df.append(data, ignore_index=True)

    questions_df.to_csv(filepath, sep=";")


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


if __name__ == "__main__":
    pass

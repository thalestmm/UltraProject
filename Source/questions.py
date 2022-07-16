import typing
from dataclasses import dataclass
from typing import Optional
import pandas as pd
import logging
import random
import string
import json
import os

# LOCAL MODULES
from Source import disciplines


class QuestionID:
    """
    1) Generate a new ID for a question upon entry.
    2) Check if the new ID already exists.
    3) Write the new ID on the master file for later conference.
    """

    def __init__(self):
        self.master_filepath = r"Registry/question_statistics.csv"

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
        questions_df = pd.read_csv(self.master_filepath, sep=";")

        if new_id in questions_df["question_id"].to_list():
            return True
        else:
            return False


# TODO: EVALUATE CHANGING THE PARAGRAPH TAGS TO SOME INLINE VALUES (MAYBE <span>)
@dataclass
class HTMLString:
    """
    Baseclass for HMTL Strings (both on the question text and alternatives).
    """
    content: str

    def __post_init__(self):
        self.content = self.add_paragraph_tags(self.content)

    def __repr__(self):
        return str(self.content)

    def __str__(self):
        return str(self.content)

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
    A: HTMLString.__str__
    B: HTMLString.__str__
    C: HTMLString.__str__
    D: HTMLString.__str__
    answer: str

    def __post_init__(self):
        self.A = str(self.A.__str__())
        self.B = str(self.B.__str__())
        self.C = str(self.C.__str__())
        self.D = str(self.D.__str__())

        available_answers = ["A", "B", "C", "D"]

        self.answer = self.answer.upper()

        if self.answer not in available_answers:
            logging.exception(f"Alternative '{self.answer}' provided is not available")
            raise ValueError("Answer must be either A, B, C or D")

        if self.A == self.B or self.A == self.C or self.A == self.D or \
           self.B == self.C or self.B == self.D or self.C == self.D:
            raise ValueError("There cannot be any 2 alternatives with the same value")

    def __repr__(self):
        return {
            "A": str(self.A),
            "B": str(self.B),
            "C": str(self.C),
            "D": str(self.D),
            "answer": str(self.answer)
        }


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
        else:
            return {
                "exam_name": str(self.exam_name),
                "exam_year": int(self.exam_year)
            }


@dataclass
class BaseQuestionModel:
    """
    Class for formatting new questions and later turning each entry into its own JSON file.
    """

    question_text: HTMLString.__str__
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

    def dict_representation(self) -> dict:
        return {
            "question_id": str(self.question_id),
            "discipline": str(self.discipline),
            "area": str(self.area),
            "subject": str(self.subject),
            "difficulty_level": int(self.difficulty_level),
            "question_text": str(self.question_text),
            "alternatives": self.alternatives.__repr__(),
            "exam_description": self.exam_description.__repr__(),
            "has_auxiliary_image": bool(self.has_auxiliary_image),
            "has_solution_image": bool(self.has_solution_image)
        }


# TODO: CHANGE THE APPEND() METHOD TO SOME OTHER, MAYBE CONCAT(), BECAUSE APPEND WILL BE REMOVED
def insert_new_question_into_master_file(generated_question: BaseQuestionModel, parent_dir: str = "Registry") -> None:
    data = pd.Series(generated_question.get_statistic_params())

    filepath = parent_dir + "/question_statistics.csv"

    questions_df = pd.read_csv(filepath, sep=";")

    questions_df = questions_df.append(data, ignore_index=True)

    questions_df.to_csv(filepath, sep=";", index=False)


def export_into_json(generated_question: BaseQuestionModel, parent_dir: str = "Questions") -> None:
    """
    Create a JSON file with the new question ID as the filename.
    :return: None
    """
    if type(generated_question) is not BaseQuestionModel:
        raise ValueError("Must pass question as BaseQuestionModel")

    question_id = generated_question.question_id
    question_data = generated_question.dict_representation()
    json_file = json.dumps(question_data)

    with open(f"{parent_dir}/{question_id}.json", "w") as file:
        file.write(json_file)

    logging.info(f"{question_id}.json file created")

    return None


def create_questions_folder() -> None:
    os.makedirs("../Questions", exist_ok=True)


if __name__ == "__main__":
    new_question = BaseQuestionModel(
        question_text=HTMLString(content="ABCDSDSF"),
        alternatives=AlternativeModel(
            A=HTMLString(content="1"),
            B=HTMLString(content="2"),
            C=HTMLString(content="3"),
            D=HTMLString(content="4"),
            answer="A"
        ),
        discipline="MATEMÁTICA",
        area="FUNÇÕES"
    )
    insert_new_question_into_master_file(new_question)
    export_into_json(new_question)
    print(type(HTMLString("lalala").__str__()))
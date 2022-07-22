import json


class Rendering:
    def __init__(self, parent_dir: str = "Questions"):
        self.questions_path_dir = parent_dir + "/"

    def get_question_parameters_from_id(self, question_id: str) :
        question_filepath = self.questions_path_dir + question_id + ".json"
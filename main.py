from questions import BaseQuestionModel


def register_new_question(*args, **kwargs):
    new_question = BaseQuestionModel(
        kwargs
    )

from django.db import models
from django.core.exceptions import ValidationError
import uuid

# VALIDATION FUNCTIONS


def validate_alternative_answer(value):
    value = value.upper()
    available_range = ["A", "B", "C", "D"]
    if value not in available_range:
        raise ValidationError(f"{value} is not an available answer alternative")


def validate_difficulty_range(value):
    if value not in range(1, 6):
        raise ValidationError(f"Difficulty level must be an integer between 1 and 5, {value} isn't")


# MODELS
class Discipline(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Area(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subject(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text = models.TextField(max_length=400)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

    alt_a = models.CharField(max_length=100)
    alt_b = models.CharField(max_length=100)
    alt_c = models.CharField(max_length=100)
    alt_d = models.CharField(max_length=100)
    answer_alt = models.CharField(max_length=1, validators=[validate_alternative_answer])

    difficulty_level = models.IntegerField(validators=[validate_difficulty_range], default=3)

    auxiliary_image = models.ImageField()
    solution_image = models.ImageField()

    def __str__(self):
        return self.id

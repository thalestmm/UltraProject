import logging
import os
from typing import List
import pandas as pd


def get_all_discipline_names() -> List[str]:
    """
    List all the disciplines on the Disciplines Dependencies folder.
    This will be used to select the adequate discipline on both the questions API and the Exam Reports.
    :return: List of strings containing all the registered disciplines.
    """
    folder_path = r"../Dependencies/Disciplines"
    full_filename = os.listdir(folder_path)
    output = []

    for file in full_filename:
        file = file.rstrip(".csv")
        output.append(file)

    return output


def get_all_areas_from_discipline(discipline_name: str) -> List[str]:
    """
    List all the registered areas from the selected discipline.
    :param discipline_name: discipline name, as registered in the Disciplines Dependencies folder.
    :return: List containing all the Areas (without repetition)
    """
    discipline_name = discipline_name.upper()

    filepath = f"../Dependencies/Disciplines/{discipline_name}.csv"
    try:
        discipline_df = pd.read_csv(filepath, index_col="id")
        return list(discipline_df["area"].unique())

    except FileNotFoundError:
        logging.exception(f"'{discipline_name}' discipline not registered")
        raise KeyError("discipline_name not available in Disciplines folder")


def get_all_subjects_from_area(discipline_name: str, area_name: str) -> List[str]:
    """
    List all the registered Subjects from the discipline's areas.
    :param discipline_name: discipline name, as registered in the Disciplines Dependencies folder.
    :param area_name: area name, as registered in the Disciplines Dependencies folder.
    :return: List containing all the Subjects
    """
    discipline_name = discipline_name.upper()
    area_name = area_name.upper()

    filepath = f"../Dependencies/Disciplines/{discipline_name}.csv"

    try:
        discipline_df = pd.read_csv(filepath, index_col="id")
        subjects_from_area = list(discipline_df.loc[discipline_df.area == area_name]["subject"].unique())

        if len(subjects_from_area) == 0:
            logging.exception(f"{area_name} passed is not available inside the {discipline_name} file")
            raise KeyError(f"area_name passed is not available inside the {discipline_name} file")

        return subjects_from_area

    except FileNotFoundError:
        logging.exception(f"{discipline_name} discipline not registered")
        raise KeyError("discipline_name not available in Disciplines folder")


if __name__ == "__main__":
    print(get_all_discipline_names())
    print(get_all_areas_from_discipline("MATEMÁTICA"))
    print(get_all_subjects_from_area("MATEMÁTICA", "NÚMEROS COMPLEXOS"))
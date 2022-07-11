import os
from typing import List


def get_all_discipline_names() -> List[str]:
    """
    List all the disciplines on the Disciplines Dependencies folder.
    This will be used to select the adequate discipline on both the questions API and the Exam Reports.
    :return: List of strings containing all the registered disciplines.
    """
    folder_path = r"Dependencies/Disciplines"
    full_filename = os.listdir(folder_path)
    output = []

    for file in full_filename:
        file = file.rstrip(".csv")
        output.append(file)

    return output


def list_all_areas_from_discipline(discipline_name: str) -> List[str]:
    """
    List all the registered areas from the selected discipline.
    :param discipline_name: discipline name, as registered in the Disciplines Dependencies folder.
    :return: List containing all the Areas (without repetition)
    """
    pass


if __name__ == "__main__":
    print(get_all_discipline_names())
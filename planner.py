import datetime
from datetime import date
from math import ceil
import logging
import pandas as pd


class PlannerMaker:
    def __init__(self, date_begin, date_exam, available_weekdays: list, hours_per_day: list, revision_days: int = 7,
                 difficulty_per_area = None):

        self.date_begin     = date_begin
        self.date_exam      = date_exam

        self.revision_days  = int(revision_days)

        self.date_end       = self.date_exam - datetime.timedelta(self.revision_days,0,0)

        weekdays            = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        self.days           = {day: (available, hours) for day, available, hours in zip(weekdays,
                                                                              available_weekdays,
                                                                              hours_per_day)}

        self.hours_per_week = sum([available * hours for available, hours in self.days.values()])

        self.total_days     = (self.date_end - self.date_begin)
        self.total_weeks    = (self.total_days / 7).days
        self.total_hours    = ceil(self.total_weeks * self.hours_per_week)

        self.n_simulations  = self.get_total_simulations_n(self.total_weeks)

        self.difficulty_per_discipline = {'port': 0.111,
                                          'fis':  0.347,
                                          'mat':  0.401,
                                          'ing':  0.141}

        logging.info("Planner Class Instantiated")

    @staticmethod
    def get_total_simulations_n(total_weeks):
        """Calculates the optimal number of test simulations to take
            in regard to the total available study weeks.

            If the total number of weeks is less than 25 (about half a year),
            take simulation tests every week.

            If it's larger than 25 weeks, take 'em every 2 weeks."""

        return total_weeks if total_weeks < 25 else ceil(total_weeks / 2)


class Topics:
    def __init__(self, filepath = None):
        self.filepath = r'Dependencies/BANCO AFA - TOPICS.csv'

        topics_df = pd.read_csv(self.filepath, index_col="id")

        areas = topics_df['area'].unique()

        # FOR TEST PURPOSES ONLY
        from random import randint

        time_needed_per_subject = pd.Series([randint(15,50) / 10 for x in range(topics_df.__len__())])

        trial_df = pd.concat((topics_df,time_needed_per_subject),axis=1)

        trial_df = trial_df.rename(columns={0: 'time_needed'})

        output = trial_df

        return output


if __name__ == "__main__":
    import random

    difficulties   = [random.randint(1,5) for x in range(32)]
    available_days = [random.randint(0,1) for x in range(7)]
    hours_per_day  = [random.randint(2,8) for x in range(7)]

    # print(difficulties)

    planner = PlannerMaker(date.today(), date(2022,10,25), available_days, hours_per_day, difficulty_per_area= difficulties)

    topics = Topics()


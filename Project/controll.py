
"""
The controller module. It connects the view with the model.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""

import logging

import tkinter as tk

# from gui import GUI
from persons import PersonList
from person import Student, Faculty

# set up logger
for handler in logging.root.handlers[:]:  # make sure all handlers are removed
    logging.root.removeHandler(handler)

logging_level = logging.DEBUG
logging_format = logging.Formatter('%(asctime)s: %(levelname)s [%(name)s:%(funcName)s:%(lineno)d] - %(message)s')
logging.root.setLevel(logging_level)
h = logging.StreamHandler()
h.setFormatter(logging_format)
logging.root.addHandler(h)


class Controller:

    def __init__(self):
        """
        Initialize the controller and bind all the button from the view.
        """
        self._persons = PersonList()
        self.main_tk = tk.Tk()
        self._view = GUI(self.main_tk)

        # add the commands to the view callback dict
        self._view.add_callback(1, self.add_student)
        self._view.add_callback(2, self.add_faculty)
        self._view.add_callback(3, self.remove_person)
        self._view.bind_command()

        self.logger = logging.getLogger(__name__)

    def run(self):
        """
        Run the GUI interface.
        """
        self.main_tk.mainloop()

    def add_student(self):
        """
        Add a student to the persons list based on info from the view.
        """

        # TODO: Clear the error message in the view.
        # TODO: get the data for student from the view (calling self._view.add_student())
        #  and split the data as we did before.
        try:
            # TODO: create a Student instant using the data you got from the view
            # TODO: add the student instance you just created to the persons instance. This uses append from before.
            pass
        except Exception as e:
            # TODO: notify the view of the error if any error happens!
            pass

        # TODO: update the view list (using self._view.list_people) with the new list of people.

    def add_faculty(self):
        # TODO: Do exactly the same as you did with the add_student
        pass

    def remove_person(self):
        # TODO: Also do exactly as you did with the add_student, but consider the remove of a person.
        pass

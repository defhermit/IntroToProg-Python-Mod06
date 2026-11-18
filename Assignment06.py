# -------------------------------------------------------------------------- #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   James Connolly,11/18/2026,Updated Script from starter doc per assignment
# -------------------------------------------------------------------------- #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.
# Data Storage ------------------------------------------------------------- #
class FileProcessor:
    """
    A collection of processing Layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    James Connolly,11/18/2026,Modified class for use in Assignment 6
        added descriptive document strings to some functions
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads stored data from a file
                Changelog: (Who, When, What)
                RRoot,1.3.2030,Created function
                James Connolly,11/18/2026,Added document string to function
                :return: list of student data
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file is not None and file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes student_data list to a file
                Changelog: (Who, When, What)
                RRoot,1.3.2030,Created function
                James Connolly,11/18/2026,Added document string to function
                :return: None
        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=2)
            print("Successfully saved data to file!")
            print()
            print(json.dumps(student_data, indent=2))
            print()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file is not None and file.closed == False:
                file.close()


# Presentation ------------------------------------------------------------- #
class IO:
    """
    A collection of presentation Layer functions that manage user input and
    output

    Changelog (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    James Connolly,11.18.2026,Modified class per Assignment 6 description
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error message to the user
        Changelog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        Changelog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """
        print() # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        Changelog: (Who, When, What)
        RRoot,1.3.2030,Created function
        James Connolly,11/18/2026,Modified documentation string

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__()) # Not passing e

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays each student course enrollment entry

        Changelog: (Who, When, What)
        James Connolly,11/18/2026,Created function based on existing
            code in starter document

        :return: None
        """
        print("-" * 50)
        for student in student_data:
            print(f'{student["FirstName"]},{student["LastName"]},'
                  f'{student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function receives user input for first and last name and
            course name in which to enroll them, appends the new entry to
            the list and returns the list

        Changelog: (Who, When, What)
        RRoot,1.3.2030,Created function
        James Connolly,11.18.2026,Modified description to reflect function

        :return: list
        """
        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("What course is the student enrolling in? ")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
        except ValueError as e:
            IO.output_error_messages(
                "That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

# beginning of main program
# When the program starts, read the file data into a list of lists (table)

students = FileProcessor.read_data_from_file(
    file_name=FILE_NAME, student_data=students)

while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    # Allow the user to input their choice from the options
    menu_choice = IO.input_menu_choice()

    # Handle each option the user may choose
    if menu_choice == "1":  # This will not work if it is an integer!
        # Accept new student enrollment data
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":

        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        FileProcessor.write_data_to_file(
            file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":

        break  # out of the loop
    # If the user chooses a non-valid option, inform them and continue
    else:
        print("Please only choose option 1, 2, 3, or 4")
        continue

print("Program Ended")

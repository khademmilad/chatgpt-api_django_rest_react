from enum import Enum


class OptionValue:
    def __init__(self, title, text):
        self.title = title
        self.text = text


class TextOptions(Enum):
    OPTION_1 = OptionValue('Option 1 Title', 'Option 1 Text')
    OPTION_2 = OptionValue('Option 2 Title', 'Option 2 Text')
    OPTION_3 = OptionValue('Option 3 Title', 'Option 3 Text')


# Function to process the selected option
def process_option(title, text):
    modified_title = 'Write a short post about ' + title
    modified_text = text  # You can make any changes you need
    print("Hoora")

    return f"Modified title: {modified_title}\nModified text: {modified_text}"
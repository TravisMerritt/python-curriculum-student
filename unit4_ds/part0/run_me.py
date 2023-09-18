from common import tutorial

# Launch the program
if __name__ == "__main__":
    git_lesson = tutorial.Lesson(
        "What is Data Science?",
        "This lesson will cover the basics of Data Science."
    )
    git_lesson.launch_as_ui("data_science_lesson.json")
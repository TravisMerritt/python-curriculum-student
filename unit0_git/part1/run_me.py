from common import tutorial

# Launch the program
if __name__ == "__main__":
    git_lesson = tutorial.Lesson(
        "Git lesson on basics",
        "This lesson will cover the basics of Git."
    )
    git_lesson.launch_as_ui("git_lesson.json")
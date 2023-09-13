import json
import tkinter as tk
from PIL import Image, ImageTk
import logging

logger = logging.getLogger('sysm_logger')
logger.setLevel(logging.DEBUG)


class Tutorial:
    title: str
    description: str
    next_tutorial: str
    widgets: list[tk.Widget]
    frame_parent: tk.Frame
    custom_build: [callable] = []

    @staticmethod
    def add_label(tutorial: 'Tutorial', text: str, font: tuple[str, int] = ("Arial", 11), anchor=tk.W):
        """
        Adds a new callable to the tutorial that will add a label to the tutorial.
        :param tutorial:    The tutorial to add the label to.
        :param text:        The text to display in the label.
        :param font:        The font to use for the label.
        :param anchor:      The anchor to use for the label.
        :return:            None
        """
        tutorial.custom_build.append(lambda t=tutorial: t.add_widget(
            tk.Label(t.frame_parent, text=text, font=font, anchor=anchor, wraplength=400, justify=tk.LEFT)
        ))

    @staticmethod
    def add_whitespace(tutorial: 'Tutorial', height: int = 11):
        """
        Adds a blank label to the tutorial. Acts as a spacer.
        :param height:      The height of the whitespace.
        :param tutorial:    The tutorial to add the whitespace to.
        :return:            None
        """
        tutorial.custom_build.append(lambda t=tutorial: t.add_widget(
            tk.Label(t.frame_parent, text="", font=("Arial", height), anchor=tk.W)
        ))

    @staticmethod
    def add_image(tutorial: 'Tutorial', img_path: str, img_description: str, width: int = None, height: int = None, scale: float = None):
        """
        Adds an image to the tutorial.
        :param tutorial:            The tutorial to add the image to.
        :param img_path:            The path to the image to add.
        :param img_description:     The description of the image.
        :param width:               The width of the image.
        :param height:              The height of the image.
        :param scale:               The scale of the image.
        :return:                    None
        """
        def add_image_widget(inner_tutorial: 'Tutorial'):
            img = Image.open(img_path)
            label = tk.Label(inner_tutorial.frame_parent, anchor=tk.W)
            if width and height:
                img = img.resize((width, height))
            elif scale:
                img = img.resize((int(img.width * scale), int(img.height * scale)))
            photo = ImageTk.PhotoImage(img)
            label.image = photo
            label.configure(image=photo)
            return label

        tutorial.add_label(tutorial, img_description)
        tutorial.custom_build.append(lambda t=tutorial: t.add_widget(
            add_image_widget(t)
        ))

    @staticmethod
    def add_next_button(tutorial: 'Tutorial', the_next_tutorial: str):
        """
        Adds a button to the tutorial that will move to the next tutorial.
        :param tutorial:                The tutorial to add the image to.
        :param the_next_tutorial:       The title of the next tutorial to move to.
        :return:                        None
        """
        tutorial.next_tutorial = the_next_tutorial
        tutorial.custom_build.append(lambda t=tutorial: t.add_widget(
            tk.Button(tutorial.frame_parent, text="Next Tutorial", command=lambda: \
                ui.use_tutorial_by_name(t.next_tutorial))
        ))

    @staticmethod
    def add_code(tutorial: 'Tutorial', description: str, code: str):
        """
        Adds a code block to the tutorial.
        :param description:             The description of the code block.
        :param tutorial:                The tutorial to add the code block to.
        :param code:                    The code to add.
        :return:
        """
        def add_code_block(inner_tutorial: 'Tutorial'):
            text = tk.Text(
                inner_tutorial.frame_parent,
                font=("Courier", 12, "bold"),
                height=1,
                width=1,
                wrap=tk.WORD,
                padx=5,
                pady=5,
                bg="black",
                fg="white"
            )
            text.insert(tk.END, code)
            text.configure(state=tk.DISABLED)
            return text

        Tutorial.add_label(tutorial, description)
        Tutorial.add_whitespace(tutorial, height=5)
        tutorial.custom_build.append(lambda t=tutorial: t.add_widget(
            add_code_block(t)
        ))

    def __init__(self, title: str, description: str, custom_build=None):
        if custom_build is None:
            custom_build = []
        self.title = title
        self.description = description
        self.widgets = []
        self.custom_build = custom_build

    def build_tutorial(self, frame_parent: tk.Frame):
        self.frame_parent = frame_parent
        tutorial_title = tk.Label(self.frame_parent, text=self.title, font=("Arial", 24), anchor=tk.NW)
        tutorial_description = tk.Label(self.frame_parent, text=self.description, font=("Arial", 14),
                                        anchor=tk.NW)
        self.add_widget(tutorial_title)
        self.add_widget(tutorial_description)
        if self.custom_build:
            for build in self.custom_build:
                build()

    def add_widget(self, widget: tk.Widget):
        self.widgets.append(widget)

    def pack_widgets(self):
        for widget in self.widgets:
            widget.pack(fill=tk.BOTH)

    def delete_widgets(self):
        for widget in self.widgets:
            # Hide the widget.
            widget.pack_forget()


class TutorialWindow(tk.Tk):
    tutorials: dict[str, Tutorial]
    current_tutorial: Tutorial

    def on_canvas_resize(self, event, canvas, max_height=None):
        self.is_maximized = self.winfo_width() >= self.winfo_screenwidth()
        if self.is_maximized:
            canvas.configure(
                scrollregion=canvas.bbox("all"),
                width=event.width,
                height=event.height
            )
        else:
            canvas.configure(
                scrollregion=canvas.bbox("all"),
                width=event.width,
                height=event.height if not max_height else max_height
            )

    def on_list_canvas_scroll(self, event, canvas):
        # Check if the mouse is over the canvas.
        if self.on_list_canvas_hover:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_content_canvas_scroll(self, event, canvas):
        # Check if the mouse is over the canvas.
        if self.on_content_canvas_hover:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def __init__(self, loaded_tutorials: list[Tutorial] = None):
        super(TutorialWindow, self).__init__()
        self.current_tutorial = None
        self.on_list_canvas_hover = None
        self.on_content_canvas_hover = None
        self.is_maximized = False
        self.tutorials = {tutorial.title: tutorial for tutorial in loaded_tutorials}
        self.title("Python Tutorial")
        self.minsize(800, 0)

        # Create a window called `tutorial_window` that will contain the tutorial.
        self.tutorial_window = tk.Frame(self)
        self.tutorial_window.pack(fill=tk.BOTH, expand=True)
        self.tutorial_window.rowconfigure(0, weight=1)
        self.tutorial_window.columnconfigure(0, weight=0)
        self.tutorial_window.columnconfigure(1, weight=0)
        self.tutorial_window.columnconfigure(2, weight=0)
        self.tutorial_window.columnconfigure(3, weight=1)

        # Create a window called `tutorial_list` that will contain the list of tutorials. It will be on the left side of
        #   the `tutorial_window`.
        self.tutorial_list_canvas = tk.Canvas(self.tutorial_window)
        self.tutorial_list = tk.Frame(self.tutorial_list_canvas)
        self.tutorial_list_scrollbar = tk.Scrollbar(self.tutorial_window, orient="vertical",
                                                    command=self.tutorial_list_canvas.yview)
        self.tutorial_list_scrollbar.grid(row=0, column=0, sticky=tk.NS)
        self.tutorial_list_canvas.grid(row=0, column=1, sticky=tk.NW)
        self.tutorial_list_canvas.configure(yscrollcommand=self.tutorial_list_scrollbar.set)
        # Scroll the canvas when the mouse wheel is used but only when the mouse is over the canvas.
        self.tutorial_list_canvas.bind("<Enter>", lambda event: setattr(self, "on_list_canvas_hover", True))
        self.tutorial_list_canvas.bind("<Leave>", lambda event: setattr(self, "on_list_canvas_hover", False))
        self.tutorial_list_canvas.bind_all("<MouseWheel>",
                                           lambda event: self.on_list_canvas_scroll(event, self.tutorial_list_canvas))
        self.tutorial_list.bind(
            "<Configure>",
            lambda event, canvas=self.tutorial_list_canvas: self.on_canvas_resize(event, canvas)
        )
        self.tutorial_list_canvas.create_window((0, 1), window=self.tutorial_list, anchor=tk.NW)

        # Create a window called `tutorial_content` that will contain the content of the tutorial.
        # Create a scrollable canvas for the tutorial content.
        self.tutorial_content_canvas = tk.Canvas(self.tutorial_window)
        self.tutorial_content = tk.Frame(self.tutorial_content_canvas)
        self.tutorial_content_scrollbar = tk.Scrollbar(self.tutorial_window, orient="vertical",
                                                       command=self.tutorial_content_canvas.yview)
        self.tutorial_content_scrollbar.grid(row=0, column=2, sticky="nsw")
        self.tutorial_content_canvas.grid(row=0, column=3, sticky="nsew")
        self.tutorial_content_canvas.configure(yscrollcommand=self.tutorial_content_scrollbar.set)
        self.tutorial_content_canvas.create_window((0, 1), window=self.tutorial_content, anchor=tk.W)
        self.tutorial_content_canvas.bind("<Enter>", lambda event: setattr(self, "on_content_canvas_hover", True))
        self.tutorial_content_canvas.bind("<Leave>", lambda event: setattr(self, "on_content_canvas_hover", False))
        self.tutorial_content_canvas.bind_all(
            "<MouseWheel>",
            lambda event: self.on_content_canvas_scroll(event, self.tutorial_content_canvas)
        )
        self.tutorial_content.bind(
            "<Configure>",
            lambda event, canvas=self.tutorial_content_canvas: self.on_canvas_resize(event, canvas, max_height=600)
        )
        self.build_tutorial_list()

    def build_tutorial_list(self):
        """
        Builds the tutorial list.
        :return:
        """
        # Iterate through the list of tutorials and create a button for each tutorial.

        for i, tutorial in self.tutorials.items():
            tutorial.build_tutorial(self.tutorial_content)
            # Create a button for the tutorial.
            tutorial_button = tk.Button(
                self.tutorial_list,
                text=tutorial.title,
                width=20,
                height=2,
                command=lambda t=tutorial: self.use_tutorial_by_object(t)
            )
            tutorial_button.pack(fill=tk.X, expand=True)

    def use_tutorial_by_name(self, tutorial: str):
        tutorial = self.tutorials[tutorial]
        if tutorial:
            self.use_tutorial_by_object(tutorial)

    def use_tutorial_by_object(self, tutorial: Tutorial):
        """
        Replaces the contents of the tutorial window with the given tutorial.
        :param tutorial:
        :return:
        """
        if self.current_tutorial is not tutorial:
            # Set scrollbar to top.
            self.tutorial_content_canvas.yview_moveto(0)
            if self.current_tutorial is not None:
                self.current_tutorial.delete_widgets()
            self.current_tutorial = tutorial
            self.current_tutorial.pack_widgets()
            # Set the scroll bar to the top.
            self.tutorial_content_canvas.update_idletasks()
            self.tutorial_content_canvas.yview_moveto(0)


def process_lessons(file_path: str):
    """
    Reads a json file containing the lessons and returns a list of Tutorial objects.
    :param file_path:  The path to the json file containing the lessons.
    :return:           A list of Tutorial objects.
    """
    with open(file_path) as lesson_file:
        lesson_data = json.load(lesson_file)
        tutorials_from_json = lesson_data['tutorials']
        process_tutorials = []
        for tutorial in tutorials_from_json:
            title = tutorial['title']
            description = tutorial['description']
            temp_tutorial = Tutorial(title, description)
            # Read the components of the lesson, parsing them into Tutorial objects.
            components = tutorial['components']
            for component in components:
                component_type = component['type']
                if component_type == 'label':
                    component_text = component['text']
                    Tutorial.add_label(
                        temp_tutorial,
                        component_text
                    )
                if component_type == 'image':
                    component_path = f"./res/img/{component['image_file_name']}"
                    component_description = component['description']
                    component_width = component['width'] if 'width' in component else None
                    component_height = component['height'] if 'height' in component else None
                    component_scale = component['scale'] if 'scale' in component else None
                    Tutorial.add_image(temp_tutorial, component_path, component_description,
                                       width=component_width, height=component_height, scale=component_scale)
                if component_type == 'whitespace':
                    Tutorial.add_whitespace(temp_tutorial)
                if component_type == 'next_btn':
                    component_next = component['next_tutorial_title']
                    Tutorial.add_next_button(temp_tutorial, component_next)
                if component_type == 'code':
                    component_description = component['description']
                    component_code = component['code']
                    Tutorial.add_code(temp_tutorial, component_description, component_code)
            process_tutorials.append(temp_tutorial)
        return process_tutorials


if __name__ == '__main__':
    tutorials = process_lessons('./res/tutorials.json')
    ui = TutorialWindow(loaded_tutorials=tutorials)

    try:
        ui.update_idletasks()
        screen_width = ui.winfo_screenwidth()
        screen_height = ui.winfo_screenheight()

        size = tuple(int(_) for _ in ui.geometry().split('+')[0].split('x'))
        x = screen_width / 2 - size[0] / 2
        y = (screen_height / 2 - (size[1] + 400) / 2) - 50

        ui.geometry("+%d+%d" % (x, y))
        ui.mainloop()
    except Exception as ex:
        logger.error('Exception:', ex)

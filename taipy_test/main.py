from taipy import Gui
from data import data_md
from home import home_md
from user_input import user_input_md

# pages = {"/":"<|navbar|>", "home":home_md, "data":data_md}
pages = {"home":home_md, "data":data_md, "user-input":user_input_md}

Gui(pages=pages, css_file="main.css").run(use_reloader=True, port=5001)

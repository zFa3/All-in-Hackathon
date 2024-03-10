from taipy import Gui
from carbon_footprint_survey import form_mb
from game import game_mb
from daily_noti import noti_mb

pages = {"survey_form":form_mb, "game":game_mb, "notification":noti_mb}

Gui(pages=pages, css_file="main.css").run(use_reloader=True, port=5001, stylekit=False)

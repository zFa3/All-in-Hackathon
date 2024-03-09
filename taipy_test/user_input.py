from taipy.gui import Markdown

def read_value(state):
    print(state.just_myself)

just_myself = True

user_input_md = Markdown("""

<|container text-styling|
#TaiPy Project Baby!!!
|>

<|navbar|>

<br/>

<|Just Myself|button|on_action=read_value|>

""")
from taipy.gui import Markdown

value1 = 25
value2 = 24
value3 = 23

home_md = Markdown("""

<|container text-styling|
#TaiPy Project Baby!!!
|>

<|navbar|>

<br/>

<|layout|columns=1 1 1|

<|first column
<|container container-styling|
###Slider 1 <br/>
Slider value: <|{value1}|> <br/>
<|{value1}|slider|min=22|max=30|>
|>
|>

<|second column
<|container container-styling|
###Slider 2 <br/>
Slider value: <|{value2}|> <br/>
<|{value2}|slider|min=22|max=30|>
|>
|>

<|third column
<|container container-styling|
###Slider 3 <br/>
Slider value: <|{value3}|> <br/>
<|{value3}|slider|min=22|max=30|>
|>
|>
|>
""")
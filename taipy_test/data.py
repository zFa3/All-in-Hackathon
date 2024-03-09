from taipy.gui import Markdown
import pandas as pd

content = "average_data.csv"

def get_data(path):
    return pd.read_csv(path)

data = get_data("average_data.csv")

data_md = Markdown("""

<|container text-styling|
#TaiPy Project Baby!!!
|>

<|navbar|>

<br/>

<|layout|columns=1 5|

<|container container-styling|
<|{content}|file_download|label=install|>
|>

<|{data}|chart|type=bar|x=Country|y=Average Age|orientation=v|>

|>
""")

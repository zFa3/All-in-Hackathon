from taipy.gui import Markdown, navigate
from CO2_calculator import Carbon_Footprint

def read_Q1(state, id, properties):
    if id == "button1":
        Carbon_Footprint.set_household_members(Carbon_Footprint, 1)
    elif id == "button2":
        Carbon_Footprint.set_household_members(Carbon_Footprint, 2)
    elif id == "button3":
        Carbon_Footprint.set_household_members(Carbon_Footprint, 3)
    elif id == "button4":
        Carbon_Footprint.set_household_members(Carbon_Footprint, 4)

def read_Q2(state, id):
    if id == "button5":
        Carbon_Footprint.set_type_of_food(Carbon_Footprint, 8)
    elif id == "button6":
        Carbon_Footprint.set_type_of_food(Carbon_Footprint, 4)
    elif id == "button7":
        Carbon_Footprint.set_type_of_food(Carbon_Footprint, 2)
    elif id == "button8":
        Carbon_Footprint.set_type_of_food(Carbon_Footprint, 12)

def read_Q3(state):
    Carbon_Footprint.set_kWh(Carbon_Footprint, state.KWH)

def read_Q4(state, id):
    if id == "button10":
        Carbon_Footprint.set_transportation_type(Carbon_Footprint, 15)
    elif id == "button11":
        Carbon_Footprint.set_transportation_type(Carbon_Footprint, 12)
    elif id == "button12":
        Carbon_Footprint.set_transportation_type(Carbon_Footprint, 1)

def read_Q5(state):
    Carbon_Footprint.set_house_size(Carbon_Footprint, state.sqft)

def read_Q6(state):
    Carbon_Footprint.set_house_temp(Carbon_Footprint, state.temp)

def read_Q7(state, id):
    if id == "button15":
        Carbon_Footprint.set_dishwasher(Carbon_Footprint, 3)
    elif id == "button16":
        Carbon_Footprint.set_dishwasher(Carbon_Footprint, 2)
    elif id == "button17":
        Carbon_Footprint.set_dishwasher(Carbon_Footprint, 1)
    elif id == "button18":
        Carbon_Footprint.set_dishwasher(Carbon_Footprint, 0)

def read_Q8(state, id):
    if id == "button19":
        Carbon_Footprint.set_washing_machine(Carbon_Footprint, 3)
    elif id == "button20":
        Carbon_Footprint.set_washing_machine(Carbon_Footprint, 2)
    elif id == "button21":
        Carbon_Footprint.set_washing_machine(Carbon_Footprint, 1)
    elif id == "button22":
        Carbon_Footprint.set_washing_machine(Carbon_Footprint, 0)

def read_Q9(state, id):
    if id == "button23":
        Carbon_Footprint.set_appliances(Carbon_Footprint, 10)
    elif id == "button24":
        Carbon_Footprint.set_appliances(Carbon_Footprint, 8)
    elif id == "button25":
        Carbon_Footprint.set_appliances(Carbon_Footprint, 6)
    elif id == "button26":
        Carbon_Footprint.set_appliances(Carbon_Footprint, 3)

def calculate_footprint(state):
    navigate(state=state, to="/game", tab="_blank")

KWH = 20
sqft = 800
temp = 10

form_mb = Markdown("""
<|container body|
<|container title-styling|
Mind Your Carbon
|>

<|navbar|>

<br/>

<|container header-styling|
Take this quick quiz see your carbon footprint
|>

<|container form-box|
You yawn as you wake up to start a new day. After all, you live with...
<br/>
<|Just Myself|button|on_action=read_Q1|id=button1|>
<|1 other person|button|on_action=read_Q1|id=button2|>
<|2 other people|button|on_action=read_Q1|id=button3|>
<|3+ people|button|on_action=read_Q1|id=button4|>


<br/>
You need to get to work soon, but you need to remember to include 
protein in your meal! What type of contents are generally in your meals?
<br/>
<|you eat domestic meat frequently|button|on_action=read_Q2|id=button5|>
<|you are a vegetarian|button|on_action=read_Q2|id=button6|>
<|you are a vegan|button|on_action=read_Q2|id=button7|>
<|you prefer prepackaged meals|button|on_action=read_Q2|id=button8|>

<br/>
You find a notice informing of your electrical bill, informing that your 
kilowatt hour value for this month was
<br/>
<|container slider-styling|
Slider value: <|{KWH}|> <br/>
<|{KWH}|slider|min=10|max=50|>
<br/>
<|Enter|button|on_action=read_Q3|id=button9|>
|>

<br/>
You have a decent job as a construction worker for a large corporation, 
you get decent pay and some benefits. The problem? It's located downtown, 
some 40 minutes from your home. What is your choice of transportation?
<br/>
<|Obtain the keys and drive there|button|on_action=read_Q4|id=button10|>
<|take the bus|button|on_action=read_Q4|id=button11|>
<|Use your bike|button|on_action=read_Q4|id=button12|>

<br/>
You manage to get to work on time and it is smooth sailing from there. 
After your shift, you head home after a satisfying day of work. You earned 
this residence with hard-earned money, but it was challenging. You ponder 
the idea of how lucky you were to get a house with
<br/>
<|container slider-styling|
Slider value: <|{sqft}|> square feet<br/>
<|{sqft}|slider|min=800|max=4000|>
<br/>
<|Enter|button|on_action=read_Q5|id=button13|>
|>

<br/>
You are drenched in sweat from the heat, it is 32 degrees Celsius after all.
You decide to set your house temperature to
<br/>
<|container slider-styling|
Slider value: <|{temp}|> <br/>
<|{temp}|slider|min=10|max=25|>
<br/>
<|Enter|button|on_action=read_Q6|id=button14|>
|>

<br/>
You decided to put some dishes in the dishwasher before warming up some 
food. As you turn on the dishwasher, you remember you have used the 
dishwasher
<br/>
<|9+ this week|button|on_action=read_Q7|id=button15|>
<|4 - 9 times this week|button|on_action=read_Q7|id=button16|>
<|1 - 3 times this week|button|on_action=read_Q7|id=button17|>
<|0 times this week|button|on_action=read_Q7|id=button18|>

<br/>
You quickly throw some clothes into the washing machine before you head 
to the kitchen. You ponder how fast your clothes get dirty, but then 
again, you have used the washing machine
<br/>
<br/>
<|9+ this week|button|on_action=read_Q8|id=button19|>
<|4 - 9 times this week|button|on_action=read_Q8|id=button20|>
<|1 - 3 times this week|button|on_action=read_Q8|id=button21|>
<|0 times this week|button|on_action=read_Q8|id=button22|>

<br/>
Afterward, you head to the kitchen to warm up a few beef patties in your 
new microwave. You sigh as you see a flyer for a new fridge, but it does 
not mean much to you as you already bought
<br/>
<br/>
<|7+ new appliances this year|button|on_action=read_Q9|id=button23|>
<|5 - 7 new appliances this year|button|on_action=read_Q9|id=button24|>
<|3 - 5 new appliances this year|button|on_action=read_Q9|id=button25|>
<|less than 3 new appliances this year|button|on_action=read_Q9|id=button26|>

<br/>
You venture to your bedroom, ignoring a newspaper 
you picked up that mentions the negative effects of 
carbon footprints. After all, you're just one person, 
so you can't possibly contribute to the environment, **right**{: .italics }? 

<br/>
<|Submit|button|on_action=calculate_footprint|id=submit-button27|>

|>
|>
""")

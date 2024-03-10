from taipy import Gui
from taipy.gui import Markdown
from CO2_calculator import Carbon_Footprint
import taipy

co2 = Carbon_Footprint()

def read_Q1(state, id, properties):
    if id == "button1":
        co2.set_household_members(1)
    elif id == "button2":
        co2.set_household_members(2)
    elif id == "button3":
        co2.set_household_members(3)
    elif id == "button4":
        co2.set_household_members(4)

def read_Q2(state, id):
    if id == "button5":
        co2.set_type_of_food( 8)
    elif id == "button6":
        co2.set_type_of_food( 4)
    elif id == "button7":
        co2.set_type_of_food( 2)
    elif id == "button8":
        co2.set_type_of_food( 12)

def read_Q3(state):
    co2.set_kWh(state.KWH)

def read_Q4(state, id):
    if id == "button10":
        co2.set_transportation_type(15)
    elif id == "button11":
        co2.set_transportation_type(12)
    elif id == "button12":
        co2.set_transportation_type(1)

def read_Q5(state):
    co2.set_house_size(state.sqft)

def read_Q6(state):
    co2.set_house_temp(state.temp)

def read_Q7(state, id):
    if id == "button15":
        co2.set_dishwasher(3)
    elif id == "button16":
        co2.set_dishwasher(2)
    elif id == "button17":
        co2.set_dishwasher(1)
    elif id == "button18":
        co2.set_dishwasher(0)

def read_Q8(state, id):
    if id == "button19":
        co2.set_washing_machine(3)
    elif id == "button20":
        co2.set_washing_machine(2)
    elif id == "button21":
        co2.set_washing_machine(1)
    elif id == "button22":
        co2.set_washing_machine(0)

def read_Q9(state, id):
    if id == "button23":
        co2.set_appliances(10)
    elif id == "button24":
        co2.set_appliances(8)
    elif id == "button25":
        co2.set_appliances(6)
    elif id == "button26":
        co2.set_appliances(3)

def calculate_footprint(state):
    state.carbon_foot = co2.calculate_footprint()
    state.all_points = sorted(co2.max_carbon_contribution, key=lambda x: x[1], reverse=True)
    # print(state.all_points)
    if state.all_points[0][0] == "kwh": solution1 = "Always remember to turn objects that use electricity off"
    elif state.all_points[0][0] == "summer_temp": solution1 = "lower the thermostat in your house"
    elif state.all_points[0][0] == "dishwasher": solution1 = "use less dishes in your daily lives to use the dishwasher less"
    elif state.all_points[0][0] == "transport": solution1 = "consider taking the bus or biking more"
    elif state.all_points[0][0] == "food": solution1 = "eat more vegetables!!!"
    elif state.all_points[0][0] == "wash": solution1 = "only use washing machine when there are big loads of clothes"
    else: solution1 = "buy less new appliances"

    if state.all_points[1][0] == "kwh": solution2 = "Always remember to turn objects that use electricity off"
    elif state.all_points[1][0] == "summer_temp": solution2 = "lower the thermostat in your house"
    elif state.all_points[1][0] == "dishwasher": solution2 = "use less dishes in your daily lives to use the dishwasher less"
    elif state.all_points[1][0] == "transport": solution2 = "consider taking the bus or biking more"
    elif state.all_points[1][0] == "food": solution2 = "eat more vegetables!!!"
    elif state.all_points[1][0] == "wash": solution2 = "only use washing machine when there are big loads of clothes"
    else: solution2 = "buy less new appliances"

    if state.all_points[2][0] == "kwh": solution3 = "Always remember to turn objects that use electricity off"
    elif state.all_points[2][0] == "summer_temp": solution3 = "lower the thermostat in your house"
    elif state.all_points[2][0] == "dishwasher": solution3 = "use less dishes in your daily lives to use the dishwasher less"
    elif state.all_points[2][0] == "transport": solution3 = "consider taking the bus or biking more"
    elif state.all_points[2][0] == "food": solution3 = "eat more vegetables!!!"
    elif state.all_points[2][0] == "wash": solution3 = "only use washing machine when there are big loads of clothes"
    else: solution3 = "buy less new appliances"

    new_content = (f"You venture to your bedroom, ignoring a newspaper you picked up that mentions the negative"
                   f"effects of carbon footprints. After all, you are just one person, so you can not possibly"
                   f" contribute to the environment, right? "
                   f"<br/><br/>"
                   f"you carbon footprint is approximately: {state.carbon_foot}"
                   f"<br/><br/>"
                   f"Your top improvements you can make"
                   f"<ol>"
                   f"<li>{solution1}</li>"
                   f"<li>{solution2}</li>"
                   f"<li>{solution3}</li>"
                   f"</ol>")
    state.partial_a.update_content(state, new_content)
    taipy.gui.navigate(state=state, to="/your-tailored-solutions")

KWH = 20
sqft = 800
temp = 10

carbon_foot = 0
all_points = []

form_mb = Markdown("""
<|container body|
<|container title-styling|
Mind Your Carbon
|>

<center><|navbar|></center>

<br/>

<|container header-styling|
Take this quick (creative) survey see your carbon footprint
|>

<|container form-box1|
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
kilowatt hour value for this day was
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
<|9+ this week|button|on_action=read_Q8|id=button19|>
<|4 - 9 times this week|button|on_action=read_Q8|id=button20|>
<|1 - 3 times this week|button|on_action=read_Q8|id=button21|>
<|0 times this week|button|on_action=read_Q8|id=button22|>

<br/>
Afterward, you head to the kitchen to warm up a few beef patties in your 
new microwave. You sigh as you see a flyer for a new fridge, but it does 
not mean much to you as you already bought
<br/>
<|7+ new appliances this year|button|on_action=read_Q9|id=button23|>
<|5 - 7 new appliances this year|button|on_action=read_Q9|id=button24|>
<|3 - 5 new appliances this year|button|on_action=read_Q9|id=button25|>
<|less than 3 new appliances this year|button|on_action=read_Q9|id=button26|>

<br/>
<|Submit|button|on_action=calculate_footprint|id=submit-button27|>
<br/>
|>
|>
""")

noti_mb = Markdown("""
<|container body|
<|container title-styling|
Mind Your Carbon
|>

<center><|navbar|></center>
<br/>

<|container form-box2|
##Daily Notification:
|>
|>
""")

solution_mb = Markdown("""
<|container body|
<|container title-styling|
Mind Your Carbon
|>

<center><|navbar|></center>

<br/>

<|container form-box3|
<|Your tailored improvements|expandable|expanded=False|partial={partial_a}|>
|>

|>
""")

pages = {"survey-form":form_mb, "your-tailored-solutions":solution_mb, "notification":noti_mb}

gui = Gui(pages=pages, css_file="main.css")
partial_a = gui.add_partial("""
Nothing here yet!
<br/>
Complete the survey first!
""")
gui.run(use_reloader=True, port=5001, stylekit=False)

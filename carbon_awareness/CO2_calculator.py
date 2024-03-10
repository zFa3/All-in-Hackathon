class Carbon_Footprint:
    def __init__(self):
        # Outside temperature used to calculate
        # the amount of points you get for AC
        self.summer_temperature = 32
        self.carbon_points = 0
        self.max_carbon_contribution = []

        # The Average Canadian creates 31808 lbs of CO2 per year

        # Variables that you change
        # based on your lifestyle
        self.household_members = 0
        self.house_size = 0
        self.house_temp = 0
        self.kWh = 0

        self.type_of_food = 0
        self.transportation_type = 0
        self.dishwasher = 0
        self.washing_machine = 0
        self.appliances = 0
        # These are the weights it shows
        # us how much impact each factor has
        # on the amount of CO2 emitted

        # lbs of CO2 per:
        self.kWh_weight = 0.8
        self.members_weight = 1.7
        self.housesize_weight = 0.15
        self.HVAC_weight = 0.85

    ########################################
    # Setter Functions
    def set_household_members(self, n):
        self.household_members = n
        # print(self.household_members)

    def set_house_size(self, n):
        self.house_size = n
        # print(self.house_size)

    def set_house_temp(self, summer_temp):
        self.house_temp = summer_temp
        # print(self.house_temp)

    def set_kWh(self, n):
        self.kWh = n
        # print(self.kWh)

    def set_type_of_food(self, n):
        self.type_of_food = n
        # print(self.type_of_food)

    def set_transportation_type(self, n):
        self.transportation_type = n
        # print(self.transportation_type)

    def set_dishwasher(self, n):
        self.dishwasher = n
        # print(self.dishwasher)

    def set_washing_machine(self, n):
        self.washing_machine = n
        # print(self.washing_machine)

    def set_appliances(self, n):
        self.appliances = n
        # print(self.appliances)

    ########################################

    def return_all_vals(self):
        return self.carbon_points

    def calculate_footprint(self) -> int:
        self.carbon_points = 0

        max_carbon_contribution = []
        # calculating the amount of CO2
        # emitted through energy consumption
        self.carbon_points += min(30, int(self.kWh * self.kWh_weight))
        max_carbon_contribution.append(("kwh", min(30, int(self.kWh * self.kWh_weight))))

        # this takes the number of people in your house
        # and deducts more points based on if you live alone
        # or with others
        self.carbon_points += min(30, int(self.household_members * self.members_weight))

        # take the amount of heating and cooling you prefer
        # and calculate how much CO2 you create
        self.carbon_points += min(30, int(((self.summer_temperature - self.house_temp) * (
                    self.house_size // 1000)) * self.HVAC_weight))
        max_carbon_contribution.append(("summer_temp", min(30, int(((self.summer_temperature - self.house_temp) * (
                    self.house_size // 1000)) * self.HVAC_weight))))

        # Add the points for house size (in sqft)
        self.carbon_points += self.house_size // 400
        # adding the rest of the non-input/non-slider questions
        self.carbon_points += self.dishwasher + self.transportation_type + self.type_of_food + self.washing_machine + self.appliances
        max_carbon_contribution.append(("dishwasher", self.dishwasher))
        max_carbon_contribution.append(("transport", self.transportation_type))
        max_carbon_contribution.append(("food", self.type_of_food))
        max_carbon_contribution.append(("wash", self.washing_machine))
        max_carbon_contribution.append(("appliance", self.appliances))

        self.max_carbon_contribution = max_carbon_contribution[:]

        return self.carbon_points
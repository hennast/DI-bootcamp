from unicodedata import name


[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]

class Family:
    def __init__(self, last_name, members): 
        self.last_name = last_name
        self.members = members
    def born(self, child):
        self.members.append(child)
        print("congrats")
    def is_18(self, name):
        for member in self.members:
            if name == member['first_name']:
                if member['age'] >= 18:
                    return True
                else:
                    return False
    def family_presentation(self):
        members_print = ''
        for member in self.members:
            members_print += f'name: {member[name]}, age: {member[age]}'
        output = f"""the {self.last_name} family
        ______
        {members_print}
        """

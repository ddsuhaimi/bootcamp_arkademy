import json


def get_info(name, age, address, hobbies, is_married, list_school, skills, interest_in_coding):
    info_dict = {}
    info_dict['name'] = name
    info_dict['age'] = age
    info_dict['address'] = address
    info_dict['hobbies'] = hobbies
    info_dict['is_married'] = is_married
    info_dict['list_school'] = list_school
    info_dict['skills'] = skills
    info_dict['interest_in_coding'] = interest_in_coding

    return info_dict


name = 'Dedi Suhaimi'
age = 22
address = 'Banda Aceh'
hobbies = ['programming', 'running']
is_married = False
list_school = [{'year_in': 2015, 'year_out': 2019, 'major': 'Mathematics'}]
skills = [{'skill_name': 'Data Analysis', 'level': 'beginner'},
          {'skill_name': 'Python', 'level': 'advanced'}]
interest_in_coding = True

info_dict = get_info(name, age, address, hobbies, is_married,
                     list_school, skills, interest_in_coding)

with open('person.json', 'w') as json_file:
    json.dump(info_dict, json_file)

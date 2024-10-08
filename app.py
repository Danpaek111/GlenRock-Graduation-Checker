from flask import Flask, render_template, request, make_response
import csv
import pandas as pd
from io import StringIO

app = Flask(__name__)


world_lang = pd.read_csv('processed_data/filled_world_lang.csv')
social_studies = pd.read_csv('processed_data/filled_social_studies.csv')
science_courses = pd.read_csv('processed_data/filled_science_courses.csv')
phys_ed = pd.read_csv('processed_data/filled_phys_ed.csv')
performing_arts = pd.read_csv('processed_data/filled_performing_arts.csv')
math_courses = pd.read_csv('processed_data/filled_math_courses.csv')
fin_lit = pd.read_csv('processed_data/filled_fin_lit.csv')
english_courses = pd.read_csv('processed_data/filled_english_courses.csv')
century_courses = pd.read_csv('processed_data/filled_21st_century.csv')

categories = [
    (world_lang, "world_lang"), 
    (social_studies, "social_studies"),
    (science_courses, "science_courses"),
    (phys_ed, "phys_ed"), 
    (performing_arts, "performing_arts"),
    (math_courses, "math_courses"), 
    (fin_lit, "fin_lit"), 
    (english_courses, "english_courses"), 
    (century_courses, "century_courses")
]
def required_num_of_credits_per_category(category):
    if (category == 'world_lang'):
        return 10
    elif (category == 'social_studies'):
        return 15
    elif (category == 'science_courses'):
        return 18
    elif (category == 'phys_ed'):
        return 20
    elif (category == 'performing_arts'):
        return 10
    elif (category == 'math_courses'):
        return 15
    elif (category == 'fin_lit'):
        return 2.5
    elif (category == 'english_courses'):
        return 20
    elif (category == 'century_courses'):
        return 5
    
def find_category_for_course(course):
    for i in range(len(categories)):
        if course in list(categories[i][0]['Name']):
            return categories[i]
        
def find_num_of_credits_for_course(course, category_csv):
    for i in range(len(category_csv)):
        row = category_csv.iloc[i]
        if row['Name'] == course:
            return row['Credits']

def change_string_to_credits(credits_str):
    credits_str = credits_str.strip()
    for i in range(len(credits_str)):
        if(credits_str[i] == " "):
            return float(credits_str[:i])

def count_graduation_requirement(list_of_courses_taken):
        # Need to know the required credits for each category --> required_num_of_credits_per_category(category)
        # For a course taken, --> for course in list_of_courses_taken:
            # Find the category the course belongs to --> find_category_for_course(course)
            # Find the number of credits of the course --> find_num_of_credits_for_course(course)
            
            # Keep track of the number of credits taken for that category
    set_of_courses_taken = set(list_of_courses_taken)
    list_of_courses_taken_nodup = list(set_of_courses_taken)
    creds_dict = {}
    # for loop for each category
    for category in categories:
        required_credits = required_num_of_credits_per_category(category[1])
        creds_dict[category[1]] = required_credits

    for course in list_of_courses_taken_nodup:
        category = find_category_for_course(course)
        string_credits = find_num_of_credits_for_course(course, category[0])
        credits = change_string_to_credits(string_credits)
        creds_dict[category[1]] = creds_dict[category[1]] - credits
        if category[1] == "fin_lit": 
            creds_dict["century_courses"] = creds_dict["century_courses"] - credits
    return creds_dict

# default page
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    # create a list of classes that the user took
    list_classes = []
    for key in request.form:
        if "class" in key:
            list_classes.append(request.form[key])
    creds_dict = count_graduation_requirement(list_classes)
    for category in creds_dict.keys():
        if creds_dict[category] < 0:
            creds_dict[category] = 0
    total_credits = 0
    for idx in creds_dict:
        total_credits += required_num_of_credits_per_category(idx) - creds_dict[idx]
    if total_credits == 130:
        last_comment = "Congratulations! You are ready to graduate!"
    else:
        last_comment = "You can read the program of studies to find more classes to take!"
        
    return render_template("result.html", 
                           wl_credits=creds_dict['world_lang'], wl_required_credits = required_num_of_credits_per_category("world_lang"),
                           ss_credits=creds_dict['social_studies'], ss_required_credits = required_num_of_credits_per_category('social_studies'),
                           sc_credits=creds_dict['science_courses'], sc_required_credits = required_num_of_credits_per_category("science_courses"),
                           pe_credits=creds_dict['phys_ed'], pe_required_credits = required_num_of_credits_per_category("phys_ed"),
                           pa_credits=creds_dict['performing_arts'], pa_required_credits = required_num_of_credits_per_category("performing_arts"),
                           mc_credits=creds_dict['math_courses'], mc_required_credits = required_num_of_credits_per_category("math_courses"),
                           fl_credits=creds_dict['fin_lit'], fl_required_credits = required_num_of_credits_per_category("fin_lit"),
                           ec_credits=creds_dict['english_courses'], ec_required_credits = required_num_of_credits_per_category("english_courses"),
                           stc_credits=creds_dict['century_courses'], stc_required_credits = required_num_of_credits_per_category("century_courses"),
                           total_credits=total_credits,
                           last_comment=last_comment
                           )

# For Testing purpuses
def main():
    print(count_graduation_requirement(['Advanced Placement (AP) Psychology','The Graphic Novel']))
if __name__=="__main__":
    main()
# Glen Rock Graduation Requirement

## Brief description of the program

The program is a Graduation Checker that will take in courses from Glen Rock High School's Program of Studies as inputs. After entering courses into each text box and pressing submit, the user will be brought to a result page in which 
## Motivation

I was having trouble finding courses to take for my senior year. I was struggling to find which credits I still needed to fulfill for the required categories to graduate. I wanted a way to track my remaining graduation requirements so that finding courses to take would be easier. My school does not have a graduation requirement checker, so I noticed many other students share the same problem as I do. I saw the need for a tool that can automatically check a student’s graduation requirement, and that was the start of this web app!

## UX Research Procedure

This is a screenshot of my application version 1.

![homepage of ver 1](images/homepage_ver1.png)

Once the app opens, the user will be presented with a UI that shows textboxes with a “submit” button above as well as an “add class” button underneath. When the user clicks on a textbox they will be presented with a list of courses offered at Glen Rock High School. (The list was aggravated from Glen Rock High School official website). The user can either select a course from the list or type out the course, which will dynamically shorten the list of courses shown based on what is typed. Once they fill in all the necessary information, the “Submit” button will take them to a result page. The result page after pressing the submit button shows the amount of credits left to be fulfilled out of the required amount of credits for the labeled category. This page shows the user which categories they still need to fulfill based on the courses entered and its purpose is to ensure that the user will take other courses that fulfill such categories.


A survey took place to receive user’s feedback and comments, which will be used for improvements and design modification of the app. The survey contains different questions that ask the user how useful, accurate, and intuitive the app was. The link to the survey is provided below.

[Survey Link](https://forms.gle/TikVRLhfF4VKGJrz9)

## Video Instruction
[Link to the Instruction](TOBEFILLED)

## Tools Used
Flask, Python, html, CSS, Jupyter Notbook, pandas

## Development Process

### Collecting Data 
The first step was getting a list of courses offered at Glen Rock High School. The information can be found in the school's official website under "Program of Studies." I imported the pdf into the workspace and observed which information was neccesary for my graduation checker. The pdf provided the name, number of credits, description, and class state code.

### Data Cleaning / Pre-processing
I decided to keep not only the name of the course and its number of credit, but also its description and state code for possibly using them for future improvement of the app. (e.g. Using the description to recommend courses to the students) I uses the python package called PyPDF2 to load the pdf into python. I iterated through the pdf pages and extracted the information based on the structure / format of the pdf. We went through multiple rounds of testing by manually checking if the extraction based on string manipulation was done correctly.

I created a csv file for each category of courses, which included the information I mentioned above. I noticed that some courses were missing, due to inconsistency in the pdf structure. I updated the csv files that were created using a Jupyter Notebook by manually typing in the missing data points.

### Design / Make model
I have decided to use Flask to run my app, as the Harvard online class I took CS50: Introduction to Computer Science based its appy development on it. We kept the simplicity of the code by naming each category with a string and maintaing a tuple that held its name and the csv file, which was loaded with pandas. We took the total number of credits required for each category for graduation. The model was able to get the list of courses that a student took and output a dictionary that held the remaining number of credit per category.

The model is populated in app.py.

### Working on the front-end 
As there are multiple courses, too many to show to the user the entire list, the intuitive decision was to use a text box to receive the input from the user. A shortcoming of the text box is that the model requires the user to input the exact name, found in the Program of Studies, to locate the course. Otherwise, the model will not recognize the course and crash. To over come this problem, we also added a dropdown menu into the text box to ensure that the user is not only provided with the exact name but can also click and auto-complete the name before writing out the entire course name.

Because the number of courses the user took is different per user, I decided to provide three text box initially. I implemented an add class button, which the user can click to add more boxes below.

### Deployment 
Up to this point, the app was being run locally via flask testing. In order to share the app and deploy it publicly, I researched into hosting the flask app on the internet. I used Koyeb, which offers free website hosting via GitHub. 

### User Experience Research
In order to receive feedback from users and update the app accordingly, I conducted a UX research via survey. I made a google form which asked the user on the app's accuracy, functionality, and design. The survey included scoring component, giving me scores to base the result, and comment section, where the user can freely provide their feedback.

I recieved 18 responses from my classmates, who are currently attending Glen Rock High School, and a teacher. 

#### Results from the survey

##### Problems
* Text color / font and background image was distracting
* Missing courses
* Missing (unclear) instructions
* The need for a delete class button
* Result page's design is unclear

##### Suggestions
* Adding a graph/chart
* Make adding classes more easy and fast

### Updating the app (Version 2)
All the problems mentioned above were fixed in version 2. I entertained using transcripts to input the classes but the idea was infeasible, as the name of the courses found on the transcript was different from the one found in the Program of Studies. 

## Past Bugs summary

1. Internal Server Error with specific courses
There was a problem that many of the users encountered when pressing the submit button to get the results of the graduation checker. It resulted from only specific courses and after being selected in the course boxes, the app would give back an internal server error which would prevent the user from seeing the result page with the remaining credits for each category.

I noticed it was because of the whitespaces that were inconsistent in front and end of a course name. The problem was solved utilizing the .strip() function.

2. Financial Literacy Courses not being double counted
This was a problem that, although users did not mention it, had to do with all courses in the financial literacy category. All of the financial literacy courses, according to the GRHS program of studies, are double counted for both the financial literacy AND 21st Century categories. My app was unable to do that so I added a piece of code that would check for when a financial literacy course would be entered and make it count for both financial literacy and 21st Century credits.

### What was exciting (Personal Reflection)

I think the most exciting part was designing the app because I was able to use my creativity to come up with cool designs and features to make it look nice. Changing the font and background images was a great way for me to stay focused on the program and not lose interest. I think just in general, making the app look better made it more appealing to other people who tried it. Improving the appearance of the app came to me after many of the responses in my UX research form reflected needs for better design/appearance. But of course, creating the app itself was also exciting because I knew it would be the first of its kind in my school and that it would pique interest in others.

## Resources

1. [Glen Rock High School program of Studies 2023-2024](https://cdnsm5-ss14.sharpschool.com/UserFiles/Servers/Server_611619/File/2023-2024%20HS%20Program%20of%20Studies%20FINAL.pdf)
2. Used ChatGPT to aid me in coding for html and CSS

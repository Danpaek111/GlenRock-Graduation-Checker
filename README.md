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
[Link to the Intrusction](TOBEFILLED)

## Tools Used
Flask, Python, html, CSS, Jupyter Notbook, pandas

## Development Process

The first step I took in creating the app was loading all of Glen Rock High School's course information into VS Code(The app I used to make the graduation checker). I used the pdf file that held the course information and parsed the data from the pdf using PyPDF2. After obtaining all the course data, I moved on to the main bulk of the app, app.py. I began by separating the courses into separate categories that would need to be fulfilled in order for the user to graduate. Using pandas, I was able to make variable for each category and set it to its own csv(ex. phys_ed = pd.read_csv('processed_data/filled_phys_ed.csv')). Following that I created a list of tuples called categories which would allow me to refer to a category and its name. Then, I created a function that would give each category its required amount of credits. 

### Past Bugs summary

1. Internal Server Error with specific courses
There was a problem that many of the users encountered when pressing the submit button to get the results of the graduation checker. It resulted from only specific courses and after being selected in the course boxes, the app would give back an internal server error which would prevent the user from seeing the result page with the remaining credits for each category.

2. Financial Literacy Courses not being double counted
This was a problem that, although users did not mention it, had to do with all courses in the financial literacy category. All of the financial literacy courses, according to the GRHS program of studies, are double counted for both the financial literacy AND 21st Century categories. My app was unable to do that so I added a piece of code that would check for when a financial literacy course would be entered and make it count for both financial literacy and 21st Century credits.
### What was exciting (Personal Reflection)

I think the most exciting part was designing the app because I was able to use my creativity to come up with cool designs and features to make it look nice. Changing the font and background images was a great way for me to stay focused on the program and not lose interest. I think just in general, making the app look better made it more appealing to other people who tried it. Improving the appearance of the app came to me after many of the responses in my UX research form reflected needs for better design/appearance. But of course, creating the app itself was also exciting because I knew it would be the first of its kind in my school and that it would pique interest in others.

## Resources

1. [Glen Rock High School program of Studies 2023-2024](https://cdnsm5-ss14.sharpschool.com/UserFiles/Servers/Server_611619/File/2023-2024%20HS%20Program%20of%20Studies%20FINAL.pdf)
2. Used ChatGPT to aid me in coding for html and CSS
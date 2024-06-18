# Glen Rock Graduation Requirement

## Brief description of the program

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

### Past Bugs summary

1. Internal Server Error with specific courses
There was a problem that many of the users encountered when pressing the submit button to get the results of the graduation checker. It resulted from only specific courses and after being selected in the course boxes, the app would give back an internal server error which would prevent the user from seeing the result page with the remaining credits for each category.

2. Financial Literacy Courses not being double counted
This was a problem that, although users did not mention it, had to do with all courses in the financial literacy category. All of the financial literacy courses, according to the GRHS program of studies, are double counted for both the financial literacy AND 21st Century categories. My app was unable to do that so I added a piece of code that would check for when a financial literacy course would be entered and make it count for both financial literacy and 21st Century credits.
### What was exciting (Personal Reflection)

To be filled

## Resources

1. [Glen Rock High School program of Studies 2023-2024](https://cdnsm5-ss14.sharpschool.com/UserFiles/Servers/Server_611619/File/2023-2024%20HS%20Program%20of%20Studies%20FINAL.pdf)
2. Used ChatGPT to aid me in coding for html and CSS
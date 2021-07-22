<link rel="stylesheet" href="main.css">
<title>Roger Johnson</title>

# <u>Who am I?</u>

My name is Roger Johnson, a student at [Southern New Hampshire University](https://www.snhu.edu/about-us/accreditations), studying Computer Science with a concentration in Software Engineering. I started at SNHU in the beginning of 2018 but before my journey, I attended Butte Community College. At Butte I found my calling in Computer Programming and made it my main priority to take every course offered on the subject. In 2016 I was given the opportunity to participate in the [California Space Grant Consortium](https://casgc.ucsd.edu/?page_id=7301) which focused on microcomputers and robotics. Participants were given an [Award of Excellence](https://drive.google.com/file/d/17GqlkbeGKNBTO9U17OXAIPlvY7EDNAcj/view?usp=sharing) along with a [Congressional recognition](https://drive.google.com/file/d/1zKCqRKnIZH5B6TEayqCbJTXCVukYfYPQ/view?usp=sharing) from their local Congress person. This opportunity introduced me to Arduinos and the world of IOT devices. My background in Computer Science is extremely broad and I have not had the opportunity to figure out my career focus.

# <u>Professional Self-Assessment</u>

A. Discuss how completing your coursework throughout the program and developing the ePortfolio has helped showcased your strengths and
shape your professional goals and values and prepared you to either enter or become more employable in the computer science field. Use
specific examples from your program and include examples outside of the artifacts included in your ePortfolio. Please address following topics:
collaborating in a team environment, communicating to stakeholders, data structures and algorithms, software engineering and database,
and security. Note: This should function as an overall introduction to your skills and you will become more specific relative to the included
artifacts in the next section.

B. Summarize/introduce how your artifacts fit together and inform the portfolio as a whole; this will help demonstrate the full range of your
computer science talents and abilities? This section should introduce your audience to the technical artifacts that will follow the professional
self-assessment. 

# <u>Code Review</u>

The video below shows a code review performed on the [original artifact](https://github.com/TheRogerDodger/Portfolio/blob/gh-pages/C%20to%20Python/ProjectCode.c). The review covers the origins of the artifact, existing functionality, code analysis, and the early thought process of potential enhancements. 

{% include youtubePlayer.html id="Co-PABozkaU" %}

# <u>Artifact 1:</u> [C to Python](https://github.com/TheRogerDodger/Portfolio/tree/gh-pages/C%20to%20Python)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Category: Software Design and Engineering

The [original artifact](https://github.com/TheRogerDodger/Portfolio/blob/gh-pages/C%20to%20Python/ProjectCode.c) comes from CS-410: Software Reverse Engineering where we were tasked on extracting [assembly code](https://github.com/TheRogerDodger/Portfolio/blob/gh-pages/C%20to%20Python/Assembly.txt) from an object file and converting it into C. To complete that assignment, I used the terminal command “objdump” to extract the assembly code from the object file and then proceeded to convert it into C. The program was designed to keep track of 5 student’s grades. During the conversion from assembly, I kept the functionality of the program exact, including all flaws.

I chose this artifact for the software design and engineering category because it demonstrates my ability to utilize reverse engineering tools and practices, knowledge of assembly language, and the skill to convert between multiple languages. To accomplish that I converted the C code into Python and show the code below, split up into respective sections.

<details>
  <summary>Click to view code</summary>
  
  <hr>

  {% highlight c %}
  const char * STUDENTS[5] = { "Jim", "Tom", "Ben", "Alice", "Ruby" };
  char GRADES[6] =  {'A','C','C','D','F','\0'};
  {% endhighlight %}

  {% highlight python %}
  STUDENTS = ["Jim", "Tom", "Ben", "Alice", "Ruby"]
  GRADES =  ['A','C','C','D','F','\0']
  {% endhighlight %}

  <hr>

  {% highlight c %}
  int ReadUserInfo(){
    int password = 0;
    char str1[15];
    puts("Enter name:");
    scanf("%s", str1);
    puts("Enter password:");
    scanf(" %d", &password);
    return password;
  }
  {% endhighlight %}

  {% highlight python %}
  def ReadUserInfo():
      name = input("Enter name:")
      password = input("Enter password:")
      return password
  {% endhighlight %}

  <hr>

  {% highlight c %}
  bool CheckUserPermissionAccess(int password){
    bool check = 0;
    if(password == 123){
      check = 1;
    }
    else{
      check = 0;
    }
    return check;
  }
  {% endhighlight %}

  {% highlight python %}
  def CheckUserPermissionAccess(password):
      if int(password) == 123:
          check = True
      else:
          check = False
      return check
  {% endhighlight %}

  <hr>

  {% highlight c %}
  void DisplayStudentInformation(){
    int i;
    for(i = 0; i <= 4; ++i){
      printf("%s %c\n", STUDENTS[i], GRADES[i]);
    }
  }
  {% endhighlight %}

  {% highlight python %}
  def DisplayStudentInformation():
      for index, name in enumerate(STUDENTS):
          print(name + ": " + GRADES[index])
  {% endhighlight %}

  <hr>

  {% highlight c %}
  int main()
  {
    int password;
    int i;
    char choice;
    password = ReadUserInfo();
    if(CheckUserPermissionAccess(password) == 1){
      puts("Welcome professor. Below are all student grades");
      DisplayStudentInformation();
      puts("Adjust grades for students?");
      scanf(" %c", &choice);
      if(choice == 'Y'){
        printf("Enter the GPA for students one at a time\n");
          for(i=0; i <= 4; ++i){
            printf("%s", STUDENTS[i]);
            scanf(" %c", &GRADES[i]);
          }
        puts("You have successfully updated class grades. The grades are now as follows:");
        DisplayStudentInformation();
      }
    }
    return 0;
  }
  {% endhighlight %}

  {% highlight python %}
  password = ReadUserInfo()
  if CheckUserPermissionAccess(password) == True:
      print("Welcome professor. Below are all student grades")
      DisplayStudentInformation()
      if input("Adjust grades for students? Y/N:") == "Y":
          print("Enter the GPA for students one at a time")
          for index, name in enumerate(STUDENTS):
              GRADES[index] = input(name + ":")
          print("You have successfully updated class grades. The grades are now as follows:")
          DisplayStudentInformation()
  {% endhighlight %}

  <hr>
  
</details>

Converting the C code into Python isn't extremely complicated as long as you have a background in programming and understand the syntax. Because this was one of my first experiences with Python, I had to learn the proper way to take an input from the user and how indices are gathered from a for-loop. Since the original code had no form of documentation, after converting to Python I went through and added the needed comments and code documentaion that can be seen [here](https://github.com/TheRogerDodger/Portfolio/blob/gh-pages/C%20to%20Python/CS-499-MilestoneTwo.py).

# <u>Artifact 2:</u> [Sign-in and Input Handling](https://github.com/TheRogerDodger/Portfolio/tree/gh-pages/Sign-in%20and%20Input%20Handling)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Category: Algorithms and Data Structure
This artifact is the above finished [Python code](https://github.com/TheRogerDodger/Portfolio/blob/gh-pages/C%20to%20Python/CS-499-MilestoneTwo.py). While the program is running, it allows anyone that knows the password to view and change the grades of five students.

I chose to build off from my first artifact for the algorithms and data structure category because of how much room there was for improvement in the code. Before my enhancements, the program didn’t have a secure sign-on, it didn’t use the entered username for any checks and also used ‘123’ as a password for everyone. The program also didn’t care what was entered and would exit on certain inputs. Below I go into the main enhancements that were made.

<hr>

For the sign-in feature, I used the existing function ReadUserInfo to gather both username and password. To accomadate a more secure system, when the user is entering their password, the text will not be shown. Since I am using lists to store the creditials of the teachers and their passwords, the indices of the username and password together act as a key-value pair. So to check if the entered values match, I used a for-loop with enumerate to track the index and compare both lists.

<details>
  <summary>View code</summary>
  
  {% highlight python %}  
  def SignInFeature():
      (password, name) = ReadUserInfo() 
      for index, teacher in enumerate(TEACHERS): 
          if name == teacher and CheckUserPermissionAccess(index, password) == True: 
              signin = True
              break 
          else:
              signin = False
      return signin
  {% endhighlight %}
  
</details>

For the input handling I made a function to ensure that the program only continues or exits on the specific value. To do this the function has 2 parameters: output, restriction. The output is the string that prompts the user for input. The restriction is what the user is allowed to enter, usually a list. The function starts with an infinite loop that exits on return. It prompts the user for their input and goes into a try-except clause. This ensures that the user is entering the desired variable type. Next it goes into an if statement that will only be true if the value entered matches any value within the restriction parameter. 

<details>
  <summary>View code</summary>
  {% highlight python %} 
  def HandleInput(output, restriction):
      while True:
          value = input(output)
          try: 
              if type(restriction[0])(value) in restriction:
                  return value
              else:
                  print("INVALID INPUT. TRY AGAIN")
          except:
              print("INVALID INPUT. TRY AGAIN")
  {% endhighlight %}

</details>

Code documentation can be found [here](https://github.com/TheRogerDodger/Portfolio/blob/gh-pages/Sign-in%20and%20Input%20Handling/CS-499-MilestoneThree.py).

<hr>

As stated in the last category, I don’t have much experience in Python but I am starting to learn that it’s a very intuitive language and is easy to pick up with the knowledge I already have. I learned how to type cast using a variables type we already know. One challenge I had was when I started the type casting I was getting an error if the restriction I was looking for didn't match the entered type. I fixed this with a try-except clause which catches the error and notifies the user that the input was incorrect.

# <u>Artifact 3:</u> [Firebase Integration](https://github.com/TheRogerDodger/Portfolio/tree/gh-pages/Firebase%20Integration)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Category: Databases
The [final artifact](https://github.com/TheRogerDodger/Portfolio/blob/gh-pages/Sign-in%20and%20Input%20Handling/CS-499-MilestoneThree.py) will be a continuation of the last two categories where I took [C code](https://github.com/TheRogerDodger/Portfolio/blob/gh-pages/C%20to%20Python/ProjectCode.c), converted it into [Python](https://github.com/TheRogerDodger/Portfolio/blob/gh-pages/C%20to%20Python/CS-499-MilestoneTwo.py) and then added more functionality.

I chose this artifact for the database category to demonstrate my ability to utilize APIs and implement a real-time database. Before the enhancements, the code was using lists that would revert on program close. It also relied on indexing those lists and hoping the needed matches were present. The code itself had plain text passwords within a list which was a security risk. Below I go through the process in implementing Firebase within Python.

<hr>



<hr>

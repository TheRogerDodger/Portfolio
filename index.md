<title>Roger Johnson</title>

# <u>Who am I?</u>

# <u>Professional Self-Assessment</u>

# <u>Code Review</u>
{% include youtubePlayer.html id="Co-PABozkaU" %}

# <u>Artifact 1:</u> [C to Python](https://github.com/TheRogerDodger/Portfolio/tree/gh-pages/C%20to%20Python)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Category: Software Design and Engineering

The [original artifact](https://github.com/TheRogerDodger/Portfolio/blob/gh-pages/C%20to%20Python/ProjectCode.c) comes from CS-410: Software Reverse Engineering where we were tasked on extracting [assembly code](https://github.com/TheRogerDodger/Portfolio/blob/gh-pages/C%20to%20Python/Assembly.txt) from an object file and converting it into C. To complete that assignment, I used the terminal command “objdump” to extract the assembly code from the object file and then proceeded to convert it into C. The program was designed to keep track of 5 student’s grades. During the conversion from assembly, I kept the functionality of the program exact, including all flaws.

I chose this artifact for the software design and engineering category because it demonstrates my ability to utilize reverse engineering tools and practices, knowledge of assembly language, and the skill to convert between multiple languages. 

---

{% highlight python %}
STUDENTS = ["Jim", "Tom", "Ben", "Alice", "Ruby"]
GRADES =  ['A','C','C','D','F','\0']
{% endhighlight %}
{% highlight c %}
const char * STUDENTS[5] = { "Jim", "Tom", "Ben", "Alice", "Ruby" };
char GRADES[6] =  {'A','C','C','D','F','\0'};
{% endhighlight %}

---

{% highlight python %}
def ReadUserInfo():
    name = input("Enter name:")
    password = input("Enter password:")
    return password
{% endhighlight %}
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

---

{% highlight python %}
def CheckUserPermissionAccess(password):
    if int(password) == 123:
        check = True
    else:
        check = False
    return check
{% endhighlight %}
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

---

{% highlight python %}
def DisplayStudentInformation():
    for index, name in enumerate(STUDENTS):
        print(name + ": " + GRADES[index])
{% endhighlight %}
{% highlight c %}
void DisplayStudentInformation(){
  int i;
  for(i = 0; i <= 4; ++i){
    printf("%s %c\n", STUDENTS[i], GRADES[i]);
  }
}
{% endhighlight %}

---

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

---

The outcome I outlined in module one was to convert the artifact into Python and that was successful. I also added comments into the Python code to explain how it runs. Since Python isn’t my best language I learned the proper ways to define a function and how to take input from a user. The for loop in python is a lot different than other languages since it doesn’t use indexes so I learned how to use enumerate to index the list.

# <u>Artifact 2:</u> [Sign-in and Input Handling](https://github.com/TheRogerDodger/Portfolio/tree/gh-pages/Sign-in%20and%20Input%20Handling)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Category: Algorithms and Data Structure
This artifact is a direct continuation from milestone 2 in CS-499 where I translated a program from C to Python. I chose to build off from my first artifact so I can show the steps I have taken to enhance the code. I believe doing it this way will show that I can take a program from fruition to the end. Before my enhancements, the program didn’t have a secure sign-on. It didn’t use the entered username for any checks and also used ‘123’ as a password for everyone. The program also didn’t care what was entered and would exit on certain inputs.

I have diverted from the outcomes I outlined in module one but believe I have demonstrated enough skill to justify the change. The enhancements I made were a sign-in feature, input handling and secure input for passwords. The sign-in feature is triggered right away and will loop until a successful login happens. We gather the user inputs and when the password would be entered the console doesn’t output what is being entered as a security measure. The username has the same index as its password so when both is true, a successful login happens. For the input handling I made a function to ensure that the program only continues or exits on the specific value. To do this the function has 2 parameters: output, restriction. The output is the string that prompts the user for input. The restriction is what the user is allowed to enter, usually a list. The function starts with an infinite loop that exits on return. It prompts the user for their input and goes into a try-except clause. This ensures that the user is entering the desired variable type. Next it goes into an if statement that will only be true if the value entered matches any value within the restriction parameter. 

As stated in the last narrative, I don’t have much experience in Python but I am starting to learn that it’s a very intuitive language and is easy to pick up with the knowledge I already have. I learned how to type cast using variables type we already know. One challenge I had was when I started the type casting I was getting an error if the restriction I was looking for was an int. I fixed this with a try-except clause which catches the error and notifies the user that the input was incorrect.

{% highlight python %}
TEACHERS = ['Admin','Johnson']
PASSWORDS = ['password', 'Roger']
{% endhighlight %}

{% highlight python %}
def CheckUserPermissionAccess(password):
    if int(password) == 123:
        check = True
    else:
        check = False
    return check
{% endhighlight %}

{% highlight python %}
def CheckUserPermissionAccess(index, password):
    if password == PASSWORDS[index]:
        check = True
    else:
        check = False
    return check
{% endhighlight %}

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

{% highlight python %} 
def HandleInput(output, restriction):
    while True: # loop until return
        value = input(output)
        try: 
            if type(restriction[0])(value) in restriction:
                return value
            else:
                print("INVALID INPUT. TRY AGAIN")
        except:
            print("INVALID INPUT. TRY AGAIN")
{% endhighlight %}

{% highlight python %}   
while SignInFeature() != True: 
    print("Incorrect credentials. Try again")

print("Welcome professor. Below are all student grades")
DisplayStudentInformation()
choice = HandleInput("Adjust grades for students? Y/N:", ['Y','y','N','n']) 
if choice == 'Y' or choice == 'y': 
    print("Enter new grade for students one at a time")
    for index, student in enumerate(STUDENTS): 
        GRADES[index] = HandleInput(student + ":", ['a','A','b','B','c','C','d','D','f','F']).upper() 
    print("You have successfully updated class grades. The grades are now as follows:")
    DisplayStudentInformation()

print("Goodbye")
{% endhighlight %}

# <u>Artifact 3:</u> [Firebase Integration](https://github.com/TheRogerDodger/Portfolio/tree/gh-pages/Firebase%20Integration)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Category: Databases
This artifact is a direct continuation from milestone 3 in CS-499 where I added more functionality to the code. I built off from this artifact to show that I can add new functionality to old projects. Before the enhancements this code was using lists that would revert on program close. It also relied on indexing those lists and hoping the needed matches were present. The code itself had passwords within a list which could be a security risk. I enhanced this artifact by integrating with a Real-time database, Firebase. 
Because I diverted from my initial outlined outcomes from module 1, I did not meet those objectives. But when I decided to go this route, I had a plan to fulfill the third category. Looking at the Database category though has me questioning if I really did do what was asked of me. I believe what I did would be considered full stack but firebase seems to simple since all you do is import a json file to build the database. If I didn’t fulfill what was needed, for the final I will add a local MongoDB into the program.
For the enhancements, I started by setting up Firebase. This consists of setting up an app for credentials and setting the database up. The database can be setup with injected code or you can use their web console to import a json file or manual inserts. The original artifact had this data in a list so in order to get it into firebase I created a json file for it: 
On the right is how firebase stores the data. Next the code that will access the database needs to have authority to do so. To keep the info secure I put it into a json file the project can read.
Now we need a way to call the firebase functions in Python. In the firebase documentation was a link to a module called Pyrebase. Since this is not a native Python module we need to install it. I’m on Windows so a simple pip install doesn’t exactly work. To install it we navigate to the folder that holds Python and open a command prompt. Now a modified pip install works here. Windows blocked the first attempt so I had to change executable rights in the windows power shell. Now the project is ready to access Firebase. The enhancements to the code include modifications to existing functions and 2 new functions.
The first function is FirebaseSetup(), this opens the credentials json file, creates an object for it and passes it to Pyrebase to connect to Firebase.
The second function ChangeStudentGrades(), moves code that was in the main code block to its own function and now uses Firebase instead of the original lists. In order to change every students grade one at a time, we need a for loop. In order to loop through we need a list of just student names so we access the database STUDENTS and get() the value of the first key. So now for each student we can change individual grades. To change an existing entry we use update() so an example would look like:
Database.child(“STUDENTS”).child(“Jim”).update({“grade” :  ”A”}); “A” will be the value changed.
Since we are in a for-loop then we are using variables and the value being changed is a user input so we need input handling.
The modifications made to existing code were in the DisplayStudntInformation() and SignInFeature(). For the display function we now connect to the database and loop through all students like we did in ChangeStudentGrades() but this time print both name and grade with no return. For SignInFeature() we kept the original user inputs and now use them to search the database and verify that the entered username and password combo exists.

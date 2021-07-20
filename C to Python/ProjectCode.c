//CS 499 Original artifact

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

const char * STUDENTS[5] = { "Jim", "Tom", "Ben", "Alice", "Ruby" };
char GRADES[6] =  {'A','C','C','D','F','\0'};

int ReadUserInfo();
bool CheckUserPermissionAccess(int password);
void DisplayStudentInformation();

int main()
{
    int password;
    int i;
    char choice;
    password = ReadUserInfo();
    if(CheckUserPermissionAccess(password) == 1)
    {
        puts("Welcome professor. Below are all student grades");
        DisplayStudentInformation();
        puts("Adjust grades for students?");
        scanf(" %c", &choice);
        if(choice == 'Y')
        {
            printf("Enter the GPA for students one at a time\n");
            for(i=0; i <= 4; ++i)
            {
                printf("%s", STUDENTS[i]);
                scanf(" %c", &GRADES[i]);
            }
            puts("You have successfully updated class grades. The grades are now as follows:");
            DisplayStudentInformation();
        }
    }
    return 0;
}
int ReadUserInfo()
{
    int password = 0;
    char str1[15];
    puts("Enter name:");
    scanf("%s", str1);
    puts("Enter password:");
    scanf(" %d", &password);
    return password;
}
bool CheckUserPermissionAccess(int password)
{
    bool check = 0;
    if(password == 123)
    {
        check = 1;
    }
    else
    {
        check = 0;
    }
    return check;
}
void DisplayStudentInformation()
{
    int i;
    for(i = 0; i <= 4; ++i)
    {
        printf("%s %c\n", STUDENTS[i], GRADES[i]);
    }
}

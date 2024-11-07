# 215908-Eco-Smart-City
Algorithm Design, Analysis and Evaluation

The system aims to manage different energy sources and check if the production meets the demand. The energy class stores the type and its rate. The distribution grid manages lists of sources. The user can add, remove or calculate the production from the sources that are being used. The GUI lets the user interact with the system. With the use of buttons to operate the type and rate, they can modify what is needed. The design will be a simple user interface to manage energy distribution and production to meet demand.

Some challenges to be aware of are:

Handling Invalid User Input: It's important to make sure users enter valid values, like positive numbers for production rates and demand.
Managing Energy Sources Efficiently: As more energy sources are added, it can be harder to manage them and ensure they are correctly added or removed. A clear interface would be good for this.
Constant state: App will stay up to date based on what is being added or removed. App should handle no changes without errors.
Error Handling: The app should handle unexpected problems and not crash, showing helpful error messages instead.
User Experience: The app should be easy to use and provide clear instructions for users.

Evaluation of design

The design algorithm I have made Will be done within python visual code studio. I'm using this because of the built in features it has like Debugging features being able to control how I debug, built in shortcuts, GitHub interactions an and how easy it is to operate within Visual code studio.

The algorithm in my design outlines the steps to add, remove, and calculate energy sources. My code accurately implements these steps using classes and functions to manage energy sources and calculate distribution based on current demand. I made sure the logic in the design is followed in the code.


What is Procedural programming

It is the basic way of writing code. Tasks are broken down into smaller steps, reusable steps called functions. It focuses on having easy step by step instructions. It works best for smaller programs or when problem solving. It helps beginners understand how to organise tasks. Key characteristics are is it a linear flow so it is done in clear sequence steps, reusable functions and it is simple and straightforward.
(Bhatia, 2022)

What is object-orientated programming

Object-oriented programming (OOP) is a way of writing code that organizes software around "objects" instead of just focusing on functions and actions. An object is a piece of data that has its own properties and behaviours. Useful for large complex software that will need regular updates. Key characteristics are Encapsulation which involves data and functions are together, Inheritance which allows classes to inherit properties of existing ones and polymorphism that allows objects to behave different ways based on the class that they are in. Used for mobile apps mainly.
(Gillis, 2021)


What is event- driven paradigms 

Commonly used for GUIS it is where it the program is determined by the users clicks or keystrokes. The key characteristics are: Events trigger actions. The flow of the program is determined by events, such as user inputs or system signals. Event handler functions, Functions or methods are designed to respond to specific events. Responsiveness, It is ideal for interactive applications like GUIs, where user actions drive the program's behaviour. Used in web development, apps and real time systems.
(geeksforgeeks, 2024)

The way they work together well is because how different each of them are. Procedural Programming focuses on step-by-step instructions and functions, OOP organizes code into objects with attributes and behaviours, making it more modular and reusable. Event-Driven Programming centres around responding to events, with an emphasis on user interaction or system signals. You can use all of them together in large applications which combines the strength of each for the best efficiency and flexibility.


Comparing and Evaluating procedural, OOP and event driven that could be used within source code.

Explanation:
In procedural programming, the code is written as a series of functions that perform tasks one after another.
Code is written as a sequence of functions. Functions receive and return data, usually in a linear flow.

Pros: Simple and easy to understand for small tasks.
Cons: Becomes difficult to manage and extend for larger applications

In object-oriented programming (OOP), the code is organized into objects that contain both data and the functions that operate on that data. Code is organized using classes and objects. Data is stored inside objects and accessed through methods.

Pros: Good for managing larger applications. Code can be reused.
Cons: Might be too complex for small tasks.

In event-driven programming, the flow of the program is controlled by events like user actions (e.g., clicks) or system messages. The program waits for events (like button clicks) and responds with event handlers. 

Pros: Great for interactive applications like GUIs.
Cons: Can become complicated with many events and handlers.

Conclusion:
Procedural programming is best for simple, small programs with a clear sequence of actions.
Object-oriented programming is ideal for large, complex applications where you need to organize data and functionality into manageable pieces.
Event-driven programming is perfect for applications that need to react to user input or other events, like graphical user interfaces (GUIs).


My code 

I wrote my Python code using Visual Studio Code (VS Code), which made the process easier and more efficient. I used the Python extension to help with things like auto-completion and error checking, so I could spot mistakes while writing the code. For debugging, I used VS Code's built-in debugger. This allowed me to set breakpoints and pause the program at certain points to check if the code was working correctly. I could also step through the code line by line to find and fix any issues. I used the Integrated Terminal in VS Code to run my Python code directly, making it faster to test changes without switching to another window.
(Awan, 2023)

Using an IDE is important because it has a lot of built in features like: centralised tools like editors, debuggers, and compilers into a single interface, making it easier to focus on development without setting up multiple applications. Code Editing Automation-IDEs help automate code writing by understanding programming language rules, which saves time and reduces errors. Syntax Highlighting- They use colours and formatting to make code more readable and to catch syntax errors quickly. Testing- IDEs support automated testing so developers can catch errors early, even before integrating with others' code. Being able to look at code line by line when debugging to be more effective.
(Amazon Web Services, 2023)

Not using an IDE can be good to  because you can get a better understanding of code because you need to type out each line manually and forces you to understand each line. It has less complexity as IDEs have advanced features that can be overwhelming for people starting out. A simple text editor doesn't do that. Text editors also take less resources. IDEs can be resource-heavy, which might cause a lag, especially if your computer is limited in processing power or memory. Without an IDE you learn how to build code manually as IDEs help or do things for you.
(Legrant, 2021)

Overall IDEs save time and make coding easier, while not using one teaches the basics better. I think using one or not depends on what a user wants. If they want to try learn it the challenging way they can use the text editor on the other hand if you want to use an IDE for the features so you are able to understand the code better that is also a good option to pick.

Debugging process and facilities in visual code studio

Breakpoints: These are markers you set on specific lines of code where you want the program to pause. This pause lets you examine variables, conditions, and the program’s state at those exact points, making it easier to pinpoint bugs. Step In, Step Over, Step Out: Step In allows you to enter a function call and examine each line of the function. Step Over moves to the next line without entering functions, letting you skip over them if they’re not relevant to the bug you’re tracking. Step Out exits the current function, taking you back to the function’s caller.
Watch and autos window: Watch window lets you monitor specific variables or expressions in real time so you can see how the values change as code executes. Auto window shows variables being chosen on the current line or breakpoint, giving you more information on variables without having to select them. Call Stack: This shows all active functions leading up to the current line, helping you trace the sequence of calls that brought you to this point. It’s helpful for understanding how different parts of the program interact and where issues may have started.
(cwebster-99, no date)



How the debugging process can be used to help develop more secure applications

The debugging process helps create more secure and robust applications by identifying and fixing potential vulnerabilities, errors, and unexpected behaviours early in development. Identifying Vulnerabilities: Debugging helps detect weaknesses like buffer overflows, injection flaws, or weak input validation that attackers might exploit. Preventing Crashes: By finding and addressing bugs, developers prevent crashes that could otherwise expose the application to denial-of-service attacks. Ensuring Data Integrity: Debugging tools allow careful examination of variables, helping developers verify that sensitive data remains protected, reducing risks of data leakage or corruption. Testing Boundary Cases: Debugging tools allow for the testing of edge cases and boundary conditions, revealing vulnerabilities that might only appear under extreme conditions. This ensures that the software behaves as expected even in unusual or unexpected situations​. Keeping code consistency is important throughout the process as the code behaves as intended and any inconsistencies can be dealt with.
(Mikejo5000, no date),(Anon, 2023)


Coding Standard used

My Code follows the PEP8 Guidelines. The main things I considered when structuring my code is: Indentation where I use 4 spaces per indentation level. This makes code blocks clear and consistent across my code. Maximum line length: This is where code lines are limited to 79 characters, this helps make code easier to read in smaller windows and looks nicer overall. I also used Blank lines as having good white space as it makes the code more structured. Naming the correct things in the right way for example lowercase for function names, Capitalise class names and constants should be full capitalised. Making comments is crucial as it makes the code readable so users can understand what's happening. By following the PEP8 standards my code can look clean, professional and it aligns with the standards.
(van Rossum, Warsaw and Coghlan, 2001)

Why coding standards are necessary

Coding standards are important for guidelines in programming as it sets clear expectations for code readability, and consistency. They improve both individual and team productivity by ensuring that code is structured in an organised, predictable manner, which makes it easier to understand and maintain.

For individuals, following a standard means that their code will be clear and understandable even if they come back to it later. It also helps prevent mistakes because they're following a tested set of guidelines.
In a team environment coding standards are very important. When everyone does coding the same way it makes it easier for members to read and understand each different work that they look at and spot issues and make the correct updates. Having consistency saves time as no one needs to learn each different persons coding style. Having standards make code simpler as everyone code is similar so people know patterns and practices that keeps the project organised and it avoids messy code. Coding standards are both very good for both solo and in a team environment as they do different things to make sure the main goal overall is met.

(Codewave, 2023),(A Guide to Coding Standards to Improve Code Quality, 2023)

Reference List

A Guide to Coding Standards to Improve Code Quality (2023) DEV Community. Available at: https://dev.to/documatic/a-guide-to-coding-standards-to-improve-code-quality-68n (Accessed: 7 November 2024).

Amazon Web Services (2023) What is an IDE? IDE Explained - AWS, Amazon Web Services, Inc. Available at: https://aws.amazon.com/what-is/ide/ (Accessed: 29 October 2024).

Anon (2023) Effective Debugging Techniques for Software Development, DEV Community. Available at: https://dev.to/billy_de_cartel/effective-debugging-techniques-for-software-development-17j7 (Accessed: 5 November 2024).

ArjanCodes (2023) Python Logging: How to Write Logs Like a Pro!, YouTube. Available at: https://www.youtube.com/watch?v=pxuXaaT1u3k (Accessed: 2 November 2024).

Awan, A.A. (2023) Setting Up VSCode For Python: A Complete Guide, Datacamp.com. DataCamp. Available at: https://www.datacamp.com/tutorial/setting-up-vscode-python (Accessed: 28 October 2024).

Bhatia, S. (2022) What is Procedural Programming? Key Features of Procedural Programming, Hackr.io. Available at: https://hackr.io/blog/procedural-programming (Accessed: 6 November 2024).

Codewave (2023) The Crucial Role of Coding Standards in Software Development Services - Codewave Insights, Codewave Insights. Available at: https://codewave.com/insights/the-crucial-role-of-coding-standards-in-software-development-services/ (Accessed: 7 November 2024).

cwebster-99 (no date) Debug Python code - Visual Studio (Windows), learn.microsoft.com. Available at: https://learn.microsoft.com/en-us/visualstudio/python/debugging-python-in-visual-studio?view=vs-2022 (Accessed: 5 November 2024).

geeksforgeeks (2024) What is the Event Driven Programming Paradigm?, GeeksforGeeks. Available at: https://www.geeksforgeeks.org/what-is-the-event-driven-programming-paradigm/ (Accessed: 6 November 2024).

Gillis, A. (2021) What Is Object-Oriented Programming (OOP)?, TechTarget. Edited by S. Lewis. Available at: https://www.techtarget.com/searchapparchitecture/definition/object-oriented-programming-OOP (Accessed: 6 November 2024).

Legrant, D. (2021) Why You Shouldn’t Always Use an IDE, Medium. Available at: https://betterprogramming.pub/why-you-shouldnt-always-use-an-ide-28ed8c7e6843 (Accessed: 29 October 2024).

Mikejo5000 (no date) Debugger Security - Visual Studio (Windows), learn.microsoft.com. Available at: https://learn.microsoft.com/en-us/visualstudio/debugger/debugger-security?view=vs-2022 (Accessed: 5 November 2024).

ProgrammingKnowledge (2023) Debugging Python with Visual Studio Code (VSCode), YouTube. Available at: https://www.youtube.com/watch?v=b4p-SBjHh28 (Accessed: 4 November 2024).

Schafer, C. (2015) ‘Python Tutorial: Using Try/Except Blocks for Error Handling’, YouTube. Available at: https://www.youtube.com/watch?v=NIWwJbo-9_8 (Accessed: 2 November 2024).

van Rossum, G., Warsaw, B. and Coghlan, N. (2001) PEP 8 – Style Guide for Python Code, peps.python.org. Available at: https://peps.python.org/pep-0008/ (Accessed: 6 November 2024).









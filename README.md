# pyArduino

Hi. This is a repo for my journey of learning python.

## Structure

### Python-PW

->Is the folder where I hold the files made while following the introductory tutorial made by Paul McWhorter.<br />
Link: [Learn Python for Beginners](https://www.youtube.com/watch?v=XCKWZAtKTnU&list=PLGs0VKk2DiYzguDvh5xk2XoX9V1VKP5Hv)

#### Files:

1. 1.helloWorld.py - my first ever python script
2. 2.ifStatements.py - as the name implies, with user input
3. 3.evenOdd.py - homework for 2. Check if entered integer is even or odd. Modulo use.
4. 4.comConditional\_.py - If 'and','or','!=','==' conditionals
5. 4.comConditional_hw.py - Homework 1 - Check if number is in interval between 5 and 10.
6. 4.comConditional_hw2.py - Homework 2 - Made in 2 ways: a.Costy - compound single print. b.As Intended by PaulW.
7. 5.forLoop\_.py - Going through lists and ranges() using for loops
8. 5.forLoops_hw.py - Homework 1 - Made in 2 ways: a.Costy - my version. b.As Intended by PaulW and added formatting (first, second, etc.)
9. 5.forLoops_hw2.py - Homework 2 - Calculate average grade based on grades introduced manually by user
10. 5.forLoops_hw3.py - Homework 3 - Added lines to show highest and lowest grade
11. 6.sortingList-Costy.py - forLoops_hw3.py with grades sorting - Costy version
12. 6.sortingList-PaulW.py - forLoops_hw3.py with grades sorting - PaulW version
13. 7.whileLoops.python - while tutorial and input grades as homwork
14. 8.myData.pkl - pickle file
15. 8.myPickle.py - learn of the pickle library
16. 8.pickleHW-1.py - pickle homework 1 - Write to a pickle file number of students, their name and grade.
17. 8.pickleHW-2.py - pickle homework 2 - Read from a pickle file the students name and grade.
18. 8.studentData.pkl - file used for homework 1 and 2
19. 9.pyFunctions.python - function declaration
20. 10.funcHW.py - 5.forLoops_hw3.py with functions
21. 11.classMethod-.py - Learning classes
22. 11.classMethod-HW.py - Homework - 5.forLoops_hw3.py defining studends using classes
23. 12.threadExample.py - Learning of threading

### vPython-PW

->Is the folder where I hold the files made while following the tutorial made by Paul McWhorter on Visual Python.<br />
Link: [Visual Python 3D Graphics and Animations](https://www.youtube.com/watch?v=MJiVtz4Uj7M&list=PLGs0VKk2DiYzGCOzBrMNSWEdd2CIGC0kJ)

#### Files:

1. 1.vPythonIntro.py - cube with ball bouncing from left wall to right wall
2. 2.roomSimParam.py - size parametrized with vectors instead of length, height, etc.
3. 3.roomSimParam2.py - roomSimParam.py but with 3 balls of different colors, size and speed parameters
4. 4.roomSimParam3.py - roomSimParam2.py but with n(user input) balls of different colors, size and speed parameters (user input). The size of the room is also set by user input. **No checking** of size of balls vs room size.
5. 5.myPiston.py - thermometer components
6. 6.myThermo.py - basic thermometer demo. Temperature changes from -20 to 50 deg C. Difference from PaulW version: Color changes based on temperature and values are floats instead of ints. Also a mapping function translates temperature change to cylinder height change.
7. 7.myThermometer.py - a variation of 6.myThermo.py - you can change the temperature shown by inputing a temperature in the range of -20 and 50degC. **No checks are made** to see if the input values is in the range.
8. 8.myThermo2.py - insert n(user input) thermometers - only spawn the thermometers, equally spaced - a lot of user input. Transformed the Thermometer into a class to spawn multiple instances.
9. 9.myThermo3.py - insert n(user input) thermometers - their temperature vary according to input parameters of deltaVar which represent the rate of change. **No checks are made** to see if the rate of change drives the 'mercury' beyond the logical threshold of the thermometer.
10. 10.myThermo4.py - User input of temperature. Representation check is made to show maximum or minimum value if the user input a value which is not in the range of the specified thermometer range.
11. 11.mixingColors.py - Color shuffle Costy version
12. 12.mixingColorsPW.py - Color shuffle PaulW version
13. 13.mixingColorsPW-improved.py - Color shuffle PaulW version with constant brightness
14. 14.axisOrient.py - Orientation of objects using axis parameter
15. 15.3DRotate.py - arrow with trail rotation along X, Y and Z
16. 16.3DClockBase.py - Clock background build - minor tick made with better for loop (different from PaulW)
17. 17.3DClockPWnCo.py - Wotking clock with fix hands and clippy movement of hour and minute hand
18. 18.3DClock.py - Working clock with intermediate positions of the hour and minute hand
19. 19.3DClock2.py - Clock with numbers and label
20. 20.pyThonWidGet.py - Changing parameters of 3.roomSimParam2.py on the go

### pyArd-PW

->Is the folder where I hold the files made while following the tutorial made by Paul McWhorter on linking the well known Arduino to Python.<br />
Link: [Free Tutorials: Using Python with Arduino](https://www.youtube.com/watch?v=flfuaZaKFCM&list=PLGs0VKk2DiYzWURfJCbCGPa8HI0APjBfo)

#### Files:

1. lesson3-1.py - receive data via serial
2. lesson3-2.py - split multiple data in single variables
3. lesson3-3.0.1-homework-dial-base.py - dial demo with in-place code to adjust for cases when input is higher than expected **No text on dial**
4. lesson3-3.0.2-homework-dial-base.py - dial demo with in-place code to adjust for cases when input is higher than expected. Here the arrow remains at max and the dial turns red if value is out of dial bounds.
5. lesson3-3.1-homework-dial-class.py - transformed the dial to a class and test the spawing of multiple dials with different parameters
6. lesson3-3.2-homework-dial-class.py - getting multiple data from arduino and showing it on the multiple dials - data is translated using PaulW method (utf-8)
7. lesson3-3.3.1.-hw-v4_test.py - testing to change the way data received from the arduino is interpreted
8. lesson3-3.3.2.-homework-dial-class.py - modified the way the data received is translated (using ascii)
9. config_files.py and config.ini files used to learn about setting ini files
10. lesson3-3.3.3-prereq-testing.py - used to test data read from ini file; lesson3-3.3.3-prereq-testing.ini used for the main program and future versions of it
11. lesson3-3.3.3.-homework-dial-class-w_ini.py - modified to take all the input files from the ini file and not from user input in terminal
12. lesson3-3.3.4.-homework-dial-class-w_ini-autoconnect.py - modified to autoconnect to the arduino by finding "CH340" in the com ports. lesson3-3.3.4.-serial_auto_connect.py is used to test the autoconnect part of the program. The modification is based on this [video](https://www.youtube.com/watch?v=DJD28uK5qIk)
13. lesson3-3.3.5.-homework-dial-class-w_ini-autoconnect-scene_center.py - modified to add tkinter camera control. Dropdown list according to number of dials. Selecting '0' centers the camera.

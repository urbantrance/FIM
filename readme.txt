This project was created by Enwerem Chinonso(avaliable on linkedin) 
File intergrity monitor is a program that monitors a directory using hashing functions to ensurre that the dicectory is not tampered with and preserves the INTERGRITY of the information

To run this program and keep in running in background, input in this in your terminal
nohup python your_script.py /path/to/directory &


The nohup command ignores any input and sends all output (like print statements) to nohup.out. This file is created in the directory where you ran the command. So your script is working as expected!
To run the command input this below in your terminal
cat nohup.out


To stop the program from running in the background input this command in your terminal
ps aux | grep your_script.py

This command will list all processes related to your script. Look for the line with your script's name and note the PID (a number usually in the second column).

kill <PID>
Replace <PID> with the actual PID you found. This command stops the script.

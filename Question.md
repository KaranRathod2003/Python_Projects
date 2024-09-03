1.To create the quiz game in Python:

Start with a score of 0.
For the first question, only add points if correct; no deduction for wrong answers.
From the second question onward, deduct 1 point for each wrong answer.
If the score drops below zero, end the game and display the final score.
The quiz consists of 10 questions; if all are answered correctly, display "Game Won."
If any score between 0 and 10 is maintained after 10 questions, display the final score.


2. Password manager:

i. Encryption and Decryption: Uses the Fernet encryption method from the cryptography package to securely encrypt and decrypt passwords.
ii. Master Password Protection: The encryption key is combined with a master password provided by the user, adding an additional layer of security.
iii. Password Management: The script allows the user to add new passwords and view existing ones, storing them securely in a text file.
iv. File Handling: Passwords are stored in a file named passwords.txt, and the encryption key is stored in a file named key.key.
v. User Interface: Provides a simple command-line interface where the user can choose to add a new password, view existing passwords, or quit the program.
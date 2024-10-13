This code send multiple emails at once using Python's smtplib, 
you can connect to an SMTP server, authenticate, and loop through a list of recipients,
sending the same message to each one. Use the message and subject variables to set the message and subject to compose the email.
 

Note :- Gmail blocks less secure apps by default. 
If you're using SMTP through Gmail, you can use an App password.

Steps to generate an App password:
(*) Go to your Google Account.
(*) Under the "Security" tab, scroll down to "Signing in to Google".
(*) Enable 2-Step Verification if not already enabled.
(*) Once done, you'll see an option to generate an App Password.
(*) Use this generated App password in place of your password in the code.

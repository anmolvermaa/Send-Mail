import smtplib as smt


def reset():
    print("\nDo you want to send mail again (y/n)? ")
    inn = str(input())

    if inn == 'y' or inn == 'Y':
        main()
    elif inn == 'n' or inn == 'N':
        print("Thank you for using this system")


def Receiver() ->list[str]:
    
    print("How many people do you want to send the mail to ?")
    inn = int(input())

    ToMail = []
    for i in range(inn):
        print("Enter the email ")
        em = str(input())
        ToMail.append(em)
        print()
    return ToMail


def Sender(Tomail) -> None:
    
    Mail = smt.SMTP('smtp.gmail.com',587)
    Mail.ehlo()
    Mail.starttls()

    email = 'Your_email_address'
    password = 'App_password' # sometimes google blocks less secure app by default. you need to generate the 'app password' from security options after the 2-step verification.  
    Mail.login(email, password)

    sub = str(input("Enter the subject = "))
    body = str(input("Enter your message = "))

    message = f"subject:{sub}\n\n{body}"

    Mail.sendmail(email, Tomail, message)
    print("Mail send")
    Mail.quit()
    
    
def main() -> None:
    x = Receiver()
    Sender(x)
    reset()
    
    
    
main()










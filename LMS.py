import time
import datetime
from datetime import date

# All data
admindict = {0: {'user': 'admin', 'password': 'admin'}}
borrowerdict = {}
bookdict = {}
issuedict = {}
activeissue = {}


# Return Book
def return_book():
    bid = int(input('Enter book id::'))
    mail = input('Enter borrower email::')
    flag = -1

    for i in range(len(activeissue)):
        if activeissue[i]['Book Id'] == bid and activeissue[i]['Email id'] == mail:
            flag = 1
            index = i
            break

    if flag == 1:
        today = date.today()
        dd = (today - activeissue[index]['Date of issue']).days
        if dd > 15:
            print('This issue has passed its due date. Please collect a fine of 100 rupees.')
            res = input('Is fine collected(yes/no)::')
            if res == 'no':
                print('Book return failed!!!')
                issue_return()
            elif res != 'yes':
                print('Wrong input!!! Please try again')
                return_book()

        for i in range(index, len(activeissue) - 1):
            activeissue[i] = activeissue[i + 1]
        del activeissue[len(activeissue) - 1]
        bookdict[bid]['No of copies'] += 1
        print('Book returned successfully :)')

    else:
        print('Book ID does not exist')
    issue_return()


# Issue Book
def issue_book():
    bid = int(input('Enter book id::'))
    x = bookdict.keys()
    if bid in x:
        if bookdict[bid]['No of copies'] > 0:
            mail = input('Enter borrower email::')
            flag = -1
            for i in range(len(borrowerdict)):
                if borrowerdict[i]['Email id'] == mail:
                    name = borrowerdict[i]['Full name']
                    flag = 1
                    break

            if flag == 1:
                today = date.today()
                issuedict[len(issuedict)] = {'Book Id': bid, 'Borrower name': name, 'Email id': mail,
                                             'Date of issue': today}
                activeissue[len(issuedict)] = {'Book Id': bid, 'Borrower name': name, 'Email id': mail,
                                               'Date of issue': today}
                bookdict[bid]['No of copies'] -= 1
                print('Book issued successfully')
            else:
                print('Borrower email does not exist')
    else:
        print('Book ID does not exist')
    issue_return()


# Issue or Return
def issue_return():
    res = input("issue or return or exit or go back::")
    if res == 'issue':
        issue_book()
    elif res == 'return':
        return_book()
    elif res == 'go back':
        admin_panel()
    elif res == 'exit':
        print("Now terminating the program...")
        time.sleep(3)
        quit()
    else:
        print("Invalid input!!!")
    issue_return()


# Currently Available Books
def available_book():
    x = bookdict.keys()
    print('Book ID\t\t Book Title\t Copies Available')
    for i in x:
        if bookdict[i]['No of copies'] > 0:
            print(bookdict[i]['Book Id'], '\t\t', bookdict[i]['Book Title'], '\t', bookdict[i]['No of copies'])


# Remaining time
def remaining_time(name):
    flag = -1
    today = date.today()
    for i in range(len(activeissue)):
        if activeissue[i]['Borrower name'] == name:
            dd = (today - activeissue[i]['Date of issue']).days
            if dd > 15:
                rd = 'Overdue'
            else:
                rd = 15 - dd
            print('Book Id:', activeissue[i]['Book Id'], '\t', 'Book Title:',
                  bookdict[activeissue[i]['Book Id']]['Book Title'], '\t', 'Date of issue:',
                  activeissue[i]['Date of issue'], '\t', 'Remainig days:', rd)
            flag = 1
    if flag == -1:
        print('No active issue found!!!')


def borrowed_detail(name):
    flag = -1
    for i in range(len(activeissue)):
        if activeissue[i]['Borrower name'] == name:
            print('Book Id:', activeissue[i]['Book Id'], '\t', 'Book Title:',
                  bookdict[activeissue[i]['Book Id']]['Book Title'], '\t', 'Author:',
                  bookdict[activeissue[i]['Book Id']]['Author'], '\t', 'ISBN:',
                  bookdict[activeissue[i]['Book Id']]['ISBN'], '\t', 'Published Year:',
                  bookdict[activeissue[i]['Book Id']]['Published Year'])
            flag = 1
    if flag == -1:
        print('No active issue found!!!')

    # Individual History


def individual_history(name):
    flag = -1
    for i in range(len(issuedict)):
        if issuedict[i]['Borrower name'] == name:
            print('Book Id:', issuedict[i]['Book Id'], '\t', 'Book Title:',
                  bookdict[issuedict[i]['Book Id']]['Book Title'], '\t\t', 'Date of issue:',
                  issuedict[i]['Date of issue'])
            flag = 1
    if flag == -1:
        print('No history found!!!')


# Book History
def book_history():
    bid = int(input('Enter book id to check its borrow history::'))
    flag = -1
    for i in range(len(issuedict)):
        if issuedict[i]['Book Id'] == bid:
            print('Borrower name:', issuedict[i]['Borrower name'], '\t\tDate of issue:', issuedict[i]['Date of issue'])
            flag = 1
    if flag == -1:
        print('History for this bookid does not exist!!!')
    time.sleep(3)
    book_action()


# Delete Book
def delete_book():
    temp = int(input("Enter bookid::"))
    x = bookdict.keys()
    if temp in x:
        del bookdict[temp]
        print("Book details deleted successfully :)")
    else:
        print('Bookid not found!!!')
    time.sleep(3)
    book_action()


# Edit Book Details
def edit_book():
    temp = int(input("Enter bookid::"))
    x = bookdict.keys()
    if temp in x:
        print('Enter updated details:-')
        title = input("Book title::")
        author = input("Author name::")
        pcount = int(input("No of pages::"))
        no_copy = int(input("No of copies::"))
        isbn = int(input("ISBN number::"))
        pyear = int(input("Published Year::"))
        bookdict[temp] = {'Book Id': temp, 'Book Title': title, 'Author': author, 'Page count': pcount,
                          'No of copies': no_copy, 'ISBN': isbn, 'Published Year': pyear}
        print("Book details updated successfully :)")
    else:
        print('Bookid not found!!!')
    time.sleep(3)
    book_action()


# View Book Details
def view_book():
    print("Choose Your Option")
    print("1. View all books")
    print("2. Search book based on bookid")
    print("3. Go back")
    print("4. Exit")
    choice = int(input("Enter your choice(1-4)::"))

    if choice == 1:
        x = bookdict.keys()
        print('Book Id\t Book Title\t\t Author\t\t Page count\t No of copies\t ISBN\t\t Published Year')
        for i in x:
            print(bookdict[i]['Book Id'], '\t', bookdict[i]['Book Title'], '\t', bookdict[i]['Author'], '\t',
                  bookdict[i]['Page count'], '\t\t', bookdict[i]['No of copies'], '\t\t', bookdict[i]['ISBN'], '\t',
                  bookdict[i]['Published Year'])

    elif choice == 2:
        temp = int(input("Enter bookid::"))
        x = bookdict.keys()
        if temp in x:
            print('Book Id\t Book Title\t\t Author\t\t Page count\t No of copies\t ISBN\t\t Published Year')
            print(bookdict[temp]['Book Id'], '\t', bookdict[temp]['Book Title'], '\t', bookdict[temp]['Author'], '\t',
                  bookdict[temp]['Page count'], '\t\t', bookdict[temp]['No of copies'], '\t\t', bookdict[temp]['ISBN'],
                  '\t', bookdict[temp]['Published Year'])
        else:
            print('Bookid not found!!!')
        book_action()

    elif choice == 3:
        book_action()
    elif choice == 4:
        print("Now terminating the program...")
        time.sleep(3)
        quit()
    else:
        print("Invalid input!!!")
    time.sleep(2)
    view_book()


# Add Book Details
def add_book():
    print('Enter details:-')
    title = input("Book title::")
    author = input("Author name::")
    pcount = int(input("No of pages::"))
    no_copy = int(input("No of copies::"))
    isbn = int(input("ISBN number::"))
    pyear = int(input("Published Year::"))

    if len(bookdict) == 0:
        bookdict[1000] = {'Book Id': 1000, 'Book Title': title, 'Author': author, 'Page count': pcount,
                          'No of copies': no_copy, 'ISBN': isbn, 'Published Year': pyear}
    else:
        x = list(bookdict.keys())
        newkey = x[len(x) - 1] + 1
        bookdict[newkey] = {'Book Id': newkey, 'Book Title': title, 'Author': author, 'Page count': pcount,
                            'No of copies': no_copy, 'ISBN': isbn, 'Published Year': pyear}

    print("New book added to library successfully :)")
    time.sleep(2)
    book_action()


# Book related action
def book_action():
    res = input("What action you will perform(add/view/edit/delete/history) or exit or go back::")
    if res == 'add':
        add_book()
    elif res == 'view':
        view_book()
    elif res == 'edit':
        edit_book()
    elif res == 'delete':
        delete_book()
    elif res == 'history':
        book_history()
    elif res == 'go back':
        admin_panel()
    elif res == 'exit':
        print("Now terminating the program...")
        time.sleep(3)
        quit()
    else:
        print("Invalid input!!!")
    time.sleep(3)
    book_action()


# Borrower related Action
def borrower_related_action():
    print("Choose Your Option")
    print("1. Complete account details of all borrowers")
    print("2. Complete Borrow history")
    print("3. Active Borrows")
    print("4. Go back")
    print("5. Exit")
    choice = int(input("Enter your choice(1-5)::"))

    if choice == 1:
        print('Full name\t\t DOB\t\t Contact Number\t\t Email id')
        for i in range(len(borrowerdict)):
            print(borrowerdict[i]['Full name'], '\t\t', borrowerdict[i]['DOB'], '\t', borrowerdict[i]['Contact Number'],
                  '\t\t', borrowerdict[i]['Email id'])

    elif choice == 2:
        print('Borrower name\t\t Book Id\t Book title\t\t\t Date of issue')
        for i in range(len(issuedict)):
            print(issuedict[i]['Borrower name'], '\t\t', issuedict[i]['Book Id'], '\t\t',
                  bookdict[issuedict[i]['Book Id']]['Book Title'], '\t\t', issuedict[i]['Date of issue'])

    elif choice == 3:
        print('Borrower name\t\t Book Id\t Book title\t\t\t Date of issue\t Remainig days')
        today = date.today()
        for i in range(len(issuedict)):
            dd = (today - activeissue[i]['Date of issue']).days
            if dd > 15:
                rd = 'Overdue'
            else:
                rd = 15 - dd
            print(activeissue[i]['Borrower name'], '\t\t', activeissue[i]['Book Id'], '\t\t',
                  bookdict[issuedict[i]['Book Id']]['Book Title'], '\t\t', activeissue[i]['Date of issue'], '\t', rd)

    elif choice == 4:
        admin_panel()
    elif choice == 5:
        print("Now terminating the program...")
        time.sleep(3)
        quit()

    else:
        print("Invalid input!!!")
    time.sleep(3)
    borrower_related_action()


# Borrower Registration
def borrower_registration(user):
    print('Enter details:-')
    fname = input("Full name::")
    dob = input("DOB(dd/mm/yy)::")
    mobile = int(input("Contact number::"))
    email = input("Email id::")
    pwd = input("Password::")
    borrowerdict[len(borrowerdict)] = {'Full name': fname, 'DOB': dob, 'Contact Number': mobile, 'Email id': email,
                                       'Password': pwd}
    print("New borrower account created successfully :)")
    if user == 'admin':
        admin_panel()
    elif user == 'borrower':
        borrower()


# Borrower Panel
def borrower_panel(name):
    print("Choose Your Option")
    print("1. List of books currently available in library")
    print("2. List of your currently borrowed books with remaining time")
    print("3. Borrowed books details")
    print("4. Your borrow history")
    print("5. Go back")
    print("6. Exit")
    choice = int(input("Enter your choice(1-6)::"))

    if choice == 1:
        available_book()
    elif choice == 2:
        remaining_time(name)
    elif choice == 3:
        borrowed_detail(name)
    elif choice == 4:
        individual_history(name)
    elif choice == 5:
        borrower()
    elif choice == 6:
        print("Now terminating the program...")
        time.sleep(3)
        quit()

    else:
        print("Invalid input!!!")
    time.sleep(3)
    borrower_panel(name)


# Check Id aand password validity for Borrower
def borrower_check():
    email = input("Enter your Email id::")
    pwd = input("Enter your password::")
    flag = 'error'
    for i in range(len(borrowerdict)):
        if borrowerdict[i]['Email id'] == email and borrowerdict[i]['Password'] == pwd:
            flag = borrowerdict[i]['Full name']
            break
    if flag == 'error':
        print("Wrong credentials!!!")
    return flag


# Borrower
def borrower():
    res = input("You want to login or register or exit or go back::")
    if res == 'login':
        flag = borrower_check()
        if flag != 'error':
            print("Login Successful...")
            borrower_panel(flag)
    elif res == 'register':
        borrower_registration('borrower')
    elif res == 'go back':
        main()
    elif res == 'exit':
        print("Now terminating the program...")
        time.sleep(3)
        quit()
    else:
        print("Invalid input!!!")
    time.sleep(3)
    borrower()


# Create Admin
def create_admin():
    uname = input("Enter new admin username::")
    pwd = input("Enter new admin password::")
    admindict[len(admindict)] = {'user': uname, 'password': pwd}
    print("New admin account created successfully :)")


# Create users
def create_user():
    res = input("Type of user to create(admin or borrower) or exit or go back::")
    if res == 'admin':
        create_admin()
    elif res == 'borrower':
        borrower_registration('admin')
    elif res == 'go back':
        admin_panel()
    elif res == 'exit':
        print("Now terminating the program...")
        time.sleep(3)
        quit()
    else:
        print("Invalid input!!!")
    create_user()


# Check Id aand password validity for Admin
def admin_check():
    uname = input("Enter your username::")
    pwd = input("Enter your password::")
    flag = -1
    for i in range(len(admindict)):
        if admindict[i]['user'] == uname and admindict[i]['password'] == pwd:
            flag = 1
            break
    if flag == -1:
        print("Wrong credentials!!!")
        admin_check()
    return flag


# Admin Panel
def admin_panel():
    print("Choose Your Option")
    print("1. Create user")
    print("2. Book Action (Add/View/Edit/Delete/Borrower History)")
    print("3. Issue/Return book")
    print("4. Borrower related action")
    print("5. Go back")
    print("6. Exit")
    choice = int(input("Enter your choice(1-6)::"))

    if choice == 1:
        create_user()
    elif choice == 2:
        book_action()
    elif choice == 3:
        issue_return()
    elif choice == 4:
        borrower_related_action()
    elif choice == 5:
        main()
    elif choice == 6:
        print("Now terminating the program...")
        time.sleep(3)
        quit()

    else:
        print("Invalid input!!!")
    time.sleep(3)
    admin_panel()


# Main function
def main():
    user = input("What is your user type(admin or borrower) or exit::")

    # Admin type
    if user == 'admin':
        flag = int(admin_check())
        if flag == 1:
            print("Login Successful...")
            admin_panel()

    elif user == 'borrower':
        borrower()

    elif user == 'exit':
        print("Now terminating the program...")
        time.sleep(3)
        quit()

    else:
        print("Invalid input!!!\nPlease try again...")
    time.sleep(3)
    main()


# Start of Library managment system
print("*****WECLOME TO LIBRARY MANGMENT SYSTEM*****")
main()

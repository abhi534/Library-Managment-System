The purpose of this application is to manage a library for the following stakeholders:
I. Admin
II. Borrowers
Admin will have the following functionalities:
I. Create more admins and borrowers.
II. View book details and borrowing history based on the BookID.
III. Add more books to the library. A book will have the following details:
a. BookID - This will be generated automatically by the application.
b. Book Title
c. Author Name
d. Total Pages
e. The number of copies available in the library.
f. ISBN - 13 digits number unique for each edition of the book.
g. Published Year
IV. Edit these books based on BookID. All the information apart from BookID can be updated by the admin.
V. Delete book based on BookID.
VI. List all borrowers and view their details like account info and borrowing history.
VII. Give a book to a borrower by entering the BookID and borrower's email address. A book can only be borrowed if there is a copy available at the library which is not
borrowed currently.
VIII. Accept book return. Charge fine of INR 100 if the book is returned 14 days after the borrowing date.
The borrower will have the following functionalities:
I. Register on the application by entering the following information:
a. Full Name
b. DOB
c. Contact Number
d. Email Address
e. Password
II. Log in to the platform using email and password.
III. View the list of the currently borrowed books along with the remaining time. A book can only be borrowed for 15 days at a time.
IV. View book details of each borrowed book.
V. View borrowing history - list of the book borrowed in the past.
Default admin:
Username: admin
Password: admin


#Library managment system
main() √
I. Admin (login function- admin_check()) (admin_panel()) √
a. Create user (create_user()) √
i. Create admin (create_admin()) √
ii. Create borrower (borrower_registration ()) √
b. Book Action (Add/View/Edit/Delete/Borrower History) (book_action()) √
i. Add (add_book()) √
ii. View (view_book()) √
1. View all books √
2. Search book based on bookid √
iii. Edit (edit_book()) √
iv. Delete (delete_book()) √
v. Borrower History (book_history()) √
c. Issue/Return book (issue_return()) √
i. Issue book (issue_book()) √
ii. Return book (return_book()) √
d. Borrower related action (borrower_related_action()) √
i. Complete account details of all borrowers √
ii. Complete Borrow history √
iii. Active Borrows √
II. Borrower(borrower())
a. Login (login function- borrower_check()) (borrower_panel()) √
i. List of books currently available in library (available_book()) √
ii. List of currently borrowed books with remaining time (remaining_time()) √
iii. Borrowed books details (borrowed_detail()) √
iv. Your borrow history (individual_history()) √
b. Register (borrower_registration()) √

# Unified Modelling Language (UML)
## System to diagram practice:


## Task 1: 
• System description (Co-Pilot generated):
• A local council wants to update its public library network with a Smart Library Borrowing System. 
• You have been asked to design the UML class diagram for the core system.

The system must support:

### 1. Users
• There are two types of users: Members and Librarians.
• All users have: userID, name, email.
• Members additionally have: membershipDate, maxBooksAllowed.
• Librarians additionally have: employeeNumber.

### 2. Books
• Each book has: ISBN, title, author, category.
• A book can have multiple physical copies.
• Each BookCopy has: copyID, condition, status (Available, Borrowed, Reserved).

### 3. Borrowing
• A Member can borrow multiple BookCopies.
• A BookCopy can only be borrowed by one Member at a time.
• A Borrowing record must store: borrowDate, dueDate, returnDate.

### 4. Reservations
• Members can reserve books (not specific copies).
• A reservation includes: reservationDate, status (Active, Fulfilled, Cancelled).
• A book can have multiple reservations, but a member can only have one active reservation per book.

### 5. Notifications
• When a reserved book becomes available, the system sends a notification.
• A Notification has: notificationID, message, dateSent.

### 6. System Rules
• A Member cannot borrow more than their maxBooksAllowed.
• A BookCopy cannot be borrowed if its status is not “Available”.
• When a BookCopy is returned, the system checks if there are active reservations and assigns it accordingly.

## Your Task
• Create a UML class diagram that includes:
• Classes and attributes
• Methods (only where meaningful, e.g., borrowBook(), reserveBook())
• Associations between classes
• Multiplicities (e.g., 1..*, 0..1)
• Inheritance (User → Member / Librarian)
• Aggregation or composition (Book → BookCopy is a good candidate)


# Task 1 - walkthrough

### 1. Identify Classes
Library
User
Librarian
Member
Book
Reservation
Borrowing
Notification




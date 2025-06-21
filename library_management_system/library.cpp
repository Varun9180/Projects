#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Book {
public:
    int id;
    string title;
    string author;
    bool isAvailable;

    Book(int id, string title, string author) {
        this->id = id;
        this->title = title;
        this->author = author;
        this->isAvailable = true;
    }

    void display() {
        cout << "ID: " << id << ", Title: " << title
             << ", Author: " << author
             << ", Status: " << (isAvailable ? "Available" : "Borrowed") << endl;
    }
};

class Library {
private:
    vector<Book> books;

public:
    void addBook(int id, string title, string author) {
        books.push_back(Book(id, title, author));
        cout << "Book added!\n";
    }

    void viewBooks() {
        if (books.empty()) {
            cout << "No books in library.\n";
            return;
        }
        for (auto& book : books) {
            book.display();
        }
    }

    void searchBook(string keyword) {
        bool found = false;
        for (auto& book : books) {
            if (book.title.find(keyword) != string::npos) {
                book.display();
                found = true;
            }
        }
        if (!found) cout << "No matching book found.\n";
    }

    void deleteBook(int id) {
        auto it = remove_if(books.begin(), books.end(), [id](Book& b) {
            return b.id == id;
        });
        if (it != books.end()) {
            books.erase(it, books.end());
            cout << "Book removed!\n";
        } else {
            cout << "Book ID not found.\n";
        }
    }

    void sortBooks() {
        sort(books.begin(), books.end(), [](Book& a, Book& b) {
            return a.title < b.title;
        });
        cout << "Books sorted by title.\n";
    }
};

int main() {
    Library lib;
    int choice;

    while (true) {
        cout << "\n=== Library Menu ===\n";
        cout << "1. Add Book\n";
        cout << "2. View All Books\n";
        cout << "3. Search Book by Title\n";
        cout << "4. Remove Book by ID\n";
        cout << "5. Sort Books by Title\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            int id;
            string title, author;
            cout << "Enter ID: "; cin >> id;
            cin.ignore();
            cout << "Enter Title: "; getline(cin, title);
            cout << "Enter Author: "; getline(cin, author);
            lib.addBook(id, title, author);
        }
        else if (choice == 2) {
            lib.viewBooks();
        }
        else if (choice == 3) {
            cin.ignore();
            string keyword;
            cout << "Enter title keyword to search: ";
            getline(cin, keyword);
            lib.searchBook(keyword);
        }
        else if (choice == 4) {
            int id;
            cout << "Enter Book ID to delete: ";
            cin >> id;
            lib.deleteBook(id);
        }
        else if (choice == 5) {
            lib.sortBooks();
        }
        else if (choice == 6) {
            cout << "Exiting...\n";
            break;
        }
        else {
            cout << "Invalid choice. Try again.\n";
        }
    }

    return 0;
}

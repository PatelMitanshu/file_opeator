# Here's a simple implementation of a personal journal application in Python that uses object-oriented programming principles, text file handling, and exception handling. The program allows users to create, read  and delete journal entries.

class Journal:
    def __init__(self, filename):
        self.filename = filename

    def add_entry(self, content):
        from datetime import datetime
        entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{entry_time} - {content}\n"
        try:
            with open(self.filename, 'a') as file:
                file.write(entry)
            print("Entry added successfully.")
        except Exception as e:
            print(f"An error occurred while adding the entry: {e}")

    def view_entries(self):
        try:
            with open(self.filename, 'r') as file:
                entries = file.readlines()
                if not entries:
                    print("No entries found.")
                else:
                    for entry in entries:
                        print(entry.strip())
        except FileNotFoundError:
            print("No journal file found. Please add an entry first.")
        except Exception as e:
            print(f"An error occurred while reading the entries: {e}")

    def search_entries(self, keyword):
        try:
            with open(self.filename, 'r') as file:
                entries = file.readlines()
                found_entries = [entry for entry in entries if keyword.lower() in entry.lower()]
                if not found_entries:
                    print(f"No entries found containing the keyword: {keyword}")
                else:
                    for entry in found_entries:
                        print(entry.strip())
        except FileNotFoundError:
            print("No journal file found. Please add an entry first.")
        except Exception as e:
            print(f"An error occurred while searching the entries: {e}")

    def delete_entries(self):
        try:
            with open(self.filename, 'w') as file:
                file.write("")
            print("All entries deleted successfully.")
        except Exception as e:
            print(f"An error occurred while deleting the entries: {e}")



def main():
    journal = Journal("journal.txt")
    while True:
        print("\nPersonal Journal Application")
        print("1. Add Entry")
        print("2. View All Entries")
        print("3. Search Entries")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            content = input("Enter your journal entry: ")
            journal.add_entry(content)
        elif choice == '2':
            journal.view_entries()
        elif choice == '3':
            keyword = input("Enter a keyword to search for: ")
            journal.search_entries(keyword)
        elif choice == '4':
            confirm = input("Are you sure you want to delete all entries? (yes/no): ")
            if confirm.lower() == 'yes':
                journal.delete_entries()
            else:
                print("Deletion canceled.")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
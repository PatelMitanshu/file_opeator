# file_opeator

## Project Overview

`file_opeator.py` is a simple Python personal journal application built with object-oriented programming, text file handling, and basic exception handling. It lets the user store journal entries in a text file, view them later, search by keyword, and delete all saved entries.

The program works from a console menu and saves data in `journal.txt` in the same folder as the script.

## Features

- Add a new journal entry with a timestamp
- View all saved entries
- Search entries by keyword
- Delete all entries from the journal file
- Handle missing file and runtime errors gracefully

## How To Run

Run the script with Python:

```bash
python file_opeator.py
```

## Menu Options And Output

When the program starts, it shows this menu:

```text
Personal Journal Application
1. Add Entry
2. View All Entries
3. Search Entries
4. Delete All Entries
5. Exit
```

### 1. Add Entry

Input a journal message and the program saves it with the current date and time.

Example output:

```text
Enter your choice: 1
Enter your journal entry: Today I learned file handling in Python.
Entry added successfully.
```

### 2. View All Entries

Displays every saved journal entry from `journal.txt`.

Example output:

```text
Enter your choice: 2
2026-07-02 10:15:00 - Today I learned file handling in Python.
2026-07-02 10:20:45 - I practiced exception handling.
```

If the file does not exist yet:

```text
Enter your choice: 2
No journal file found. Please add an entry first.
```

### 3. Search Entries

Searches the journal file for entries that contain the keyword.

Example output:

```text
Enter your choice: 3
Enter a keyword to search for: Python
2026-07-02 10:15:00 - Today I learned file handling in Python.
```

If no match is found:

```text
Enter your choice: 3
Enter a keyword to search for: travel
No entries found containing the keyword: travel
```

### 4. Delete All Entries

Clears the journal file after confirmation.

Example output:

```text
Enter your choice: 4
Are you sure you want to delete all entries? (yes/no): yes
All entries deleted successfully.
```

If the user cancels deletion:

```text
Enter your choice: 4
Are you sure you want to delete all entries? (yes/no): no
Deletion canceled.
```

### 5. Exit

Closes the application.

Example output:

```text
Enter your choice: 5
Exiting the application.
```

## Notes

- Journal data is stored in `journal.txt`
- Each entry is saved with a timestamp
- The application continues running until option `5` is selected
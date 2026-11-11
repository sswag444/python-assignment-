import os


def sort_files():
    folder = input("Enter folder path: ").strip().strip('"')

    if not os.path.isdir(folder):
        print("Folder does not exist!")
        return

    for file in os.listdir(folder):
        old_path = os.path.join(folder, file)

        if os.path.isfile(old_path):
            extension = os.path.splitext(file)[1][1:].upper()

            if extension == "":
                extension = "NO_EXTENSION"

            new_folder = os.path.join(folder, extension)
            new_path = os.path.join(new_folder, file)

            if os.path.exists(new_path):
                print("Skipped:", file)
                continue

            os.makedirs(new_folder, exist_ok=True)
            os.rename(old_path, new_path)
            print("Moved:", file)

    print("Sorting complete!")


def rename_files():
    folder = input("Enter folder path: ").strip().strip('"')

    if not os.path.isdir(folder):
        print("Folder does not exist!")
        return

    name = input("Enter the new name: ").strip()

    if not name or any(c in name for c in '<>:"/\\|?*'):
        print("Enter a valid name!")
        return

    files = []

    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file)):
            files.append(file)

    files.sort()
    new_names = []

    for i, file in enumerate(files, start=1):
        extension = os.path.splitext(file)[1]
        new_name = name + "_" + str(i) + extension
        new_path = os.path.join(folder, new_name)

        if os.path.exists(new_path) and new_name != file:
            print("Name already exists:", new_name)
            print("Choose a different name.")
            return

        new_names.append(new_name)

    for old_name, new_name in zip(files, new_names):
        if old_name != new_name:
            old_path = os.path.join(folder, old_name)
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)
            print(old_name, "->", new_name)

    print("Renaming complete!")


def delete_files():
    folder = input("Enter folder path: ").strip().strip('"')

    if not os.path.isdir(folder):
        print("Folder does not exist!")
        return

    extension = input("Enter extension or ALL: ").strip().lower()
    extension = extension.lstrip(".")

    files = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            file_extension = os.path.splitext(file)[1][1:].lower()

            if extension == "all" or file_extension == extension:
                files.append(file)

    if not files:
        print("No matching files found.")
        return

    for file in files:
        print(file)

    confirm = input("Type DELETE to confirm: ")

    if confirm != "DELETE":
        print("Deletion cancelled.")
        return

    for file in files:
        os.remove(os.path.join(folder, file))
        print("Deleted:", file)

    print("Deletion complete!")


while True:
    print("\n=== Bulk File Organizer ===")
    print("1. Sort files")
    print("2. Rename files")
    print("3. Delete files")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        sort_files()
    elif choice == "2":
        rename_files()
    elif choice == "3":
        delete_files()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
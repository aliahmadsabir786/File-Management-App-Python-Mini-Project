import os


def create_file(filename):
    try:
        with open(filename, 'x') as file:
            print(f"✅ Your file '{filename}' has been created successfully!")
    except FileExistsError:
        print(f"⚠️ The file '{filename}' already exists!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


def view_file():
    files = os.listdir()
    if not files:
        print("📂 There are no files in this directory.")
    else:
        print("📂 Files available in this directory:")
        for file in files:
            print(f"   ➡️ {file}")


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"🗑️ File '{filename}' was successfully deleted.")
    except FileNotFoundError:
        print("⚠️ File not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


def reading_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"📖 Contents of '{filename}':\n{'-'*40}\n{content}\n{'-'*40}")
    except FileNotFoundError:
        print("⚠️ File not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


def edit_file(filename):
    try:
        with open(filename, 'a') as file:
            content1 = input("✍️ Enter content to add: ")
            file.write(content1 + "\n")
            print(f"✅ Content was successfully added to '{filename}'.")
    except FileNotFoundError:
        print("⚠️ File does not exist.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


def main():
    while True:
        print("\n✨ --- File Management App --- ✨")
        print("1️⃣  Create a File")
        print("2️⃣  View Files")
        print("3️⃣  Delete a File")
        print("4️⃣  Read a File")
        print("5️⃣  Edit a File")
        print("6️⃣  Exit")

        choice = input("👉 Enter a choice (1-6): ")

        if choice == "1":
            filename = input("📝 Enter a filename to create: ")
            create_file(filename)
        elif choice == "2":
            view_file()
        elif choice == "3":
            filename = input("🗑️ Enter a filename to delete: ")
            delete_file(filename)
        elif choice == "4":
            filename = input("📖 Enter a filename to read: ")
            reading_file(filename)
        elif choice == "5":
            filename = input("✍️ Enter a filename to edit: ")
            edit_file(filename)
        elif choice == "6":
            print("👋 Exiting the File Manager... Goodbye!")
            break
        else:
            print("⚠️ Invalid input, please try again.")


if __name__ == "__main__":
    main()

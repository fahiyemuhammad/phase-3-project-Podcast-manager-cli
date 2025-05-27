from models.user import User
from models.podcast import Podcast
from tabulate import tabulate

def main_menu():
    while True:
        print("\n🎧 Podcast Manager Menu")
        print("1. Manage Users")
        print("2. Manage Podcasts")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            user_menu()
        elif choice == "2":
            podcast_menu()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid input. Please try again.")


def user_menu():
    while True:
        print("\n👤 User Menu")
        print("1. Create User")
        print("2. Delete User") 
        print("3. View All Users")
        print("4. Find User by ID")                   
        print("5. View User's Podcasts")
        print("6. Back to Main Menu")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            name = input("Enter user's name: ").strip()
            email = input("Enter user's email: ").strip()
            try:
                user = User.create_user(name, email)
                print(f"✅ Created user: {user}")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                if User.delete_by_id(user_id):
                    print("✅ User deleted.")
                else:
                    print("❌ User not found.")
            except ValueError:
                print("❌ Invalid ID. Please enter a number.")

        elif choice == "3":
            users = User.get_all()
            if users:
                table = [[user.id, user.name, user.email] for user in users]
                print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="fancy_grid"))
            else:
                print("ℹ️ No users found")    

        elif choice == "4":
            try:
                user_id = int(input("Enter user ID: ").strip())
                user = User.find_by_id(user_id)
                print(user if user else "❌ User not found.")
            except ValueError:
                print("❌ Invalid ID. Please enter a number.")

        elif choice == "5":
            try:
                user_id = int(input("Enter user ID: ").strip())
                user = User.find_by_id(user_id)
                if user:
                    if user.podcasts:
                        table = [[p.id, p.title, p.genre] for p in user.podcasts]
                        print(tabulate(table, headers=["ID", "Title", "Genre"], tablefmt="fancy_grid"))
                    else:
                        print("ℹ️ This user has no podcasts.")
                else:
                    print("❌ User not found.")
            except ValueError:
                print("❌ Invalid ID. Please enter a number.")

        elif choice == "6":
            break
        else:
            print("❌ Invalid input. Try again.")      


def podcast_menu():
    while True:
        print("\n🎙 Podcast Menu")            
        print("1. Create Podcast")            
        print("2. Delete Podcast")            
        print("3. View All Podcasts")            
        print("4. Find Podcast by ID")
        print("5. Update Podcast")         
        print("6. Back to Main Menu") 

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            title = input("Enter podcast title: ").strip()
            genre = input("Enter genre: ").strip()
            try:
                user_id = int(input("Enter user ID (owner): ").strip())
                podcast = Podcast.create_podcast(title, genre, user_id)
                print(f"✅ Created podcast: {podcast}")
            except ValueError:
                print("❌ Invalid user ID. Please enter a number.")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            try:
                podcast_id = int(input("Enter podcast ID to delete: ").strip())
                if Podcast.delete_by_id(podcast_id):
                    print("✅ Podcast deleted.")
                else:
                    print("❌ Podcast not found.")
            except ValueError:
                print("❌ Invalid podcast ID. Please enter a number.")

        elif choice == "3":
            podcasts = Podcast.get_all()
            if podcasts:
                table = [[p.id, p.title, p.genre, p.user_id] for p in podcasts]
                print(tabulate(table, headers=["ID", "Title", "Genre", "User_ID"], tablefmt="fancy_grid"))
            else:
                print("ℹ️ No podcasts found.")    

        elif choice == "4":
            try:
                podcast_id = int(input("Enter podcast ID: ").strip())
                podcast = Podcast.find_by_id(podcast_id)
                print(podcast if podcast else "❌ Podcast not found.")
            except ValueError:
                print("❌ Invalid podcast ID. Please enter a number.")

        
        elif choice == "5":
            podcast_id = int(input("Enter podcast ID to edit: ").strip())
            podcast = Podcast.find_by_id(podcast_id)

            if podcast:
                print(f"Editing: {podcast}")
                new_title = input("New title (press Enter to keep current): ").strip()
                new_genre = input("New genre (press Enter to keep current): ").strip()
                new_user_id = int(input("New user ID (press Enter to keep current): ").strip())
                
                podcast.update(
                    title = new_title if new_title else None,
                    genre = new_genre if new_genre else None,
                    user_id = new_user_id if new_user_id else None
                )

                print("✅ Podcast updated successfully.")

            else:
                print("❌ Podcast not found.")


        elif choice == "6":
            break
        else:
            print("❌ Invalid input. Try again.")
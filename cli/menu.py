from models.user import User
from models.podcast import Podcast

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
        print("\n User Menu")
        print("1. Create User")
        print("2. Delete User") 
        print("3. View all Users")
        print("4. Find User by ID")                   
        print("5. View User's Podcasts")
        print("6. Back to Main Menu")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            name = input("Enter user's name: ").strip()
            email = input("Enter user's email: ").strip()
            try:
                user = User.create_user(name, email)
                print(f"Created user: {user}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            user_id = input("Enter user ID to delete: ").strip
            if User.delete_by_id(user_id):
                print("User deleted.")
            else:
                print("User not found.")
        elif choice == "3":
            users = User.get_all()
            for user in users:
                print(user)
        elif choice == "4":
            user_id = input("Enter user ID: ").strip()
            user = User.find_by_id(user_id)
            if user:
                print(user)
            else:
                print("User not found.")  
        elif choice == "5":
            user_id = input("Enter user ID: ").strip()
            user = User.find_by_id(user_id)
            if user:
                if user.podcasts:
                    for p in user.podcasts:
                        print(p)
                else:
                    print("ℹ️ This user has no podcasts.")  

            else:
                print("❌ User not found.")

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
        print("5. Back to Main Menu") 

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter podcast title: ").strip()
            genre = input("Enter genre: ").strip()
            user_id = input("Enter user ID (owner): ").strip()
            try:
                podcast = Podcast.create_podcast(title, genre, user_id)
                print(f"✅ Created podcast: {podcast}")
            except Exception as e:
                print(f"❌ Error: {e}")    

        elif choice == "2":
            podcast_id = input("Enter podcast ID to delete: ").strip()
            if podcast.delete_by_id(podcast_id):
                print("Podcast Deleted.")
            else:
                print("❌ Podcast not found.")    

        elif choice ==  "3":
            podcasts = Podcast.get_all()
            for podcast in podcasts:
                print(podcast)

        elif choice == "4":
            podcast_id = input("Enter podcast ID: ").strip()
            podcast = Podcast.find_by_id(podcast_id)
            if podcast:
                print(podcast)
            else:
                print("❌ Podcast not found.")  

        elif choice == "5":
            break
        else:
            print("❌ Invalid input. Try again.")
                       





            
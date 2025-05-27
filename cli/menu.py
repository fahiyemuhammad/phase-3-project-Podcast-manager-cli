from models.user import User
from models.podcast import Podcast
from models.episodes import Episode
from tabulate import tabulate



def main_menu():
    while True:
        print("\n🎧 Podcast Manager Menu")
        print("1. Manage Users")
        print("2. Manage Podcasts")
        print("3. Manage Episodes")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            user_menu()
        elif choice == "2":
            podcast_menu()
        elif choice == "3":
            episode_menu()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid input. Please try again.")


# ----------------------------- User Menu -----------------------------
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
                user_id = int(input("Enter user ID to delete: "))
                if User.delete_by_id(user_id):
                    print("✅ User deleted.")
                else:
                    print("❌ User not found.")
            except ValueError:
                print("❌ Invalid ID.")

        elif choice == "3":
            users = User.get_all()
            if users:
                table = [[u.id, u.name, u.email] for u in users]
                print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="fancy_grid"))
            else:
                print("ℹ️ No users found.")

        elif choice == "4":
            try:
                user_id = int(input("Enter user ID: "))
                user = User.find_by_id(user_id)
                print(user if user else "❌ User not found.")
            except ValueError:
                print("❌ Invalid ID.")

        elif choice == "5":
            try:
                user_id = int(input("Enter user ID: "))
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
                print("❌ Invalid ID.")

        elif choice == "6":
            break
        else:
            print("❌ Invalid input. Try again.")


# ----------------------------- Podcast Menu -----------------------------
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
                user_id = int(input("Enter user ID (owner): "))
                podcast = Podcast.create_podcast(title, genre, user_id)
                print(f"✅ Created podcast: {podcast}")
            except ValueError:
                print("❌ Invalid user ID.")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            try:
                podcast_id = int(input("Enter podcast ID to delete: "))
                if Podcast.delete_by_id(podcast_id):
                    print("✅ Podcast deleted.")
                else:
                    print("❌ Podcast not found.")
            except ValueError:
                print("❌ Invalid podcast ID.")

        elif choice == "3":
            podcasts = Podcast.get_all()
            if podcasts:
                table = [[p.id, p.title, p.genre, p.user_id] for p in podcasts]
                print(tabulate(table, headers=["ID", "Title", "Genre", "User_ID"], tablefmt="fancy_grid"))
            else:
                print("ℹ️ No podcasts found.")

        elif choice == "4":
            try:
                podcast_id = int(input("Enter podcast ID: "))
                podcast = Podcast.find_by_id(podcast_id)
                print(podcast if podcast else "❌ Podcast not found.")
            except ValueError:
                print("❌ Invalid podcast ID.")

        elif choice == "5":
            try:
                podcast_id = int(input("Enter podcast ID to edit: "))
                podcast = Podcast.find_by_id(podcast_id)
                if podcast:
                    print(f"Editing: {podcast}")
                    new_title = input("New title (Enter to skip): ").strip()
                    new_genre = input("New genre (Enter to skip): ").strip()
                    new_user_id = input("New user ID (Enter to skip): ").strip()
                    podcast.update(
                        title=new_title or None,
                        genre=new_genre or None,
                        user_id=int(new_user_id) if new_user_id else None
                    )
                    print("✅ Podcast updated.")
                else:
                    print("❌ Podcast not found.")
            except ValueError:
                print("❌ Invalid ID.")

        elif choice == "6":
            break
        else:
            print("❌ Invalid input. Try again.")


# ----------------------------- Episode Menu -----------------------------
def episode_menu():
    while True:
        print("\n🎬 Episode Menu")
        print("1. Create Episode")
        print("2. View All Episodes")
        print("3. View Episodes by Podcast")
        print("4. Mark Episode as Listened/Unlistened")
        print("5. Rate and Add Note to Episode")
        print("6. Delete Episode")
        print("7. Back to Main Menu")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            title = input("Enter episode title: ").strip()
            try:
                duration = input("Enter duration (e.g., 25:30): ").strip()
            except:
                print("❌ Invalid duration. Please enter a number.")
                continue  
    
            try:
                podcast_id = int(input("Enter podcast ID: "))
                episode = Episode.create_episode(title, duration, podcast_id)
                print(f"✅ Episode created: {episode}")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            episodes = Episode.get_all()
            if episodes:
                table = [[ep.id, 
                          ep.title, 
                          f"{ep.duration} mins" if ep.duration else "N/A", 
                          "✅" if ep.listened else "❌", 
                          ep.rating if 1 <= ep.rating <= 10 else "Please enter a rating within the range 1-10", 
                          ep.note if ep.note else "No note",
                          ep.podcast_id
                          ] for ep in episodes]
                print(tabulate(table, headers=["ID", "Title", "Duration in mins", "Listened", "Rating", "Notes","Podcast ID"], tablefmt="fancy_grid"))
            else:
                print("ℹ️ No episodes found.")

        elif choice == "3":
            try:
                podcast_id = int(input("Enter podcast ID to view episodes: ").strip())
            except ValueError:
                print("❌ Invalid podcast ID.")
                continue

            episodes = Episode.get_by_podcast(podcast_id)
            if episodes:
                    table = [[ep.id, ep.title, ep.duration, ep.listened] for ep in episodes]
                    print(tabulate(table, headers=["ID", "Title", "Duration", "Listened"], tablefmt="fancy_grid"))
            else:
                    print("ℹ️ No episodes for this podcast.")
            

        elif choice == "4":
            try:
                episode_id = int(input("Enter episode ID: "))
            except ValueError:
                print("❌ Invalid ID.")    
                continue

            episode = Episode.find_by_id(episode_id)
            if episode:
                status = input("Mark as listened? (yes/no): ").strip().lower()
                episode.update(listened=(status == "yes"))
                print("✅ Episode updated.")
            else:
                print("❌ Episode not found.")
            

        elif choice == "5":
            try:
                episode_id = int(input("Enter episode ID: ").strip())
            except ValueError:
                print("❌ Invalid episode ID. Please enter a number.")
                continue

            episode = Episode.find_by_id(episode_id)
            if episode:
                while True:
                    try:
                        rating = input("Rate the episode (1-10, leave blank to skip): ").strip()
                        if rating == "":
                            rating = None
                            break
                        rating = int(rating)
                        if rating < 1 or rating > 10:
                            print("❌ Rating must be between 1 and 10.")
                            continue
                        break
                    except ValueError:
                        print("❌ Invalid rating. Enter a number between 1 and 5.")

                note = input("Add a note (leave blank to skip): ").strip()
                note = note if note else None

                episode.update(rating=rating, note=note)
                print("✅ Episode updated with rating and note.")
            else:
                print("❌ Episode not found.")

        elif choice == "6":
            try:
                episode_id = int(input("Enter episode ID to delete: ").strip())
            except ValueError:
                print("❌ Invalid episode ID. Please enter a number.")
                continue

            episode = Episode.find_by_id(episode_id)
            if episode:
                confirm = input(f"Are you sure you want to delete episode '{episode.title}'? (y/n): ").strip().lower()
                if confirm == 'y':
                    if Episode.delete_by_id(episode_id):
                        print("✅ Episode deleted.")
                    else:
                        print("❌ Could not delete episode.")
                else:
                    print("❌ Deletion cancelled.")
            else:
                print("❌ Episode not found.")
                
        elif choice == "7":
            break
        else:
            print("❌ Invalid input. Try again.")
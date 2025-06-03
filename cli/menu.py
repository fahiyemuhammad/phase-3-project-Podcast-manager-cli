from models.user import User
from models.podcast import Podcast
from models.episodes import Episode
from tabulate import tabulate

def menu():
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
            print("ℹ️ Invalid input. Please try again.")


# ----------------------------- User Menu -----------------------------
def user_menu():
    while True:
        print("\n👤 User Menu")
        print("1. Create User")
        print("2. View All Users")
        print("3. View User's Podcasts")
        print("4. Find User by ID")
        print("5. Update User")
        print("6. Delete User")
        print("7. Back to Main Menu")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            name = input("Enter user's name: ").strip()
            email = input("Enter user's email: ").strip()
            try:
                user = User.create_user(name, email)
                print(f"✅ Created user: {user}")
            except Exception as e:
                print(f"ℹ️ Error: {e}")

        elif choice == "2":
            users = User.get_all()
            if users:
                table = [[u.id, u.name, u.email] for u in users]
                print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="fancy_grid"))
            else:
                print("ℹ️ No users found.") 

        elif choice == "3":
            try:
                podcast_id = int(input("Enter podcast ID: "))
                podcast = Podcast.find_by_id(podcast_id)
        
                if podcast:
            # Create a table with one row containing podcast details
                    table = [[
                    podcast.id,
                    podcast.title,
                    podcast.genre,
                    podcast.user_id
                ]]
                    print(tabulate(table, 
                         headers=["ID", "Title", "Genre", "User ID"],
                         tablefmt="fancy_grid"))
                else:
                    print(f"❌ No podcast found with ID {podcast_id}")
            
            except ValueError:
                print("❌ Invalid input. Please enter a numeric podcast ID.")
            except Exception as e:
                print(f"❌ An error occurred: {e}")


        elif choice == "4":
            try:
                user_id = int(input("Enter user ID: "))
                user = User.find_by_id(user_id)
                if user:
                    table = [[user.id, user.name, user.email]]
                    print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="fancy_grid"))
                else:
                    print("ℹ️ User not found.")
            except ValueError:
                print("ℹ️ Invalid ID.") 

        elif choice == "5":
            try:
                user_id = input("Enter the user ID you wish to Edit: ").strip()
                user = User.find_by_id(user_id)
                if user:
                    new_name =  input(f"Enter a  new name for user with the id of '{user_id}' (Enter to skip): ").strip()
                    new_email = input(f"Enter a new email for the user with the id of '{user_id}': (Enter to skip)").strip()
                    confirm = input("Are you sure you want to update the user's details? (y/n): ").strip().lower()
                    if confirm in ("y","yes"):
                        user.update_user(new_name, new_email)
                        print("✅ User updated successfully: ")
                    elif confirm in ("n", "no"):
                        print("Thank you for your confirmation! 👍 The user details were not changed. ")
                        continue  
                    else:
                        print("Invalid input! Try again with either (y/n) ")  
                else: 
                    print("ℹ️ User not found")
            except ValueError:
                print("ℹ️ Invalid ID")        



        elif choice == "6":
            try:
                user_id = int(input("Enter user ID to delete: "))
                confirm = input("Are you sure you want to delete the user? y/n: ").strip().lower()
                if confirm == "y" or confirm == "yes":
                    if User.delete_by_id(user_id):
                        print("✅ User deleted.")
                    else:
                        print("ℹ️ User not found.")
                elif confirm in ("n", "no"):
                    print("Thank you for your confirmation 👍. The user was not deleted!")                    
                    continue
                else:
                    print("Please enter y or n ")
                    continue        
            except ValueError:
                print("ℹ️ Invalid ID.")

       


        
        elif choice == "7":
            break
        else:
            print("ℹ️ Invalid input. Try again.")


# ----------------------------- Podcast Menu -----------------------------
def podcast_menu():
    while True:
        print("\n🎙 Podcast Menu")
        print("1. Create Podcast")
        print("2. View All Podcasts")
        print("3. Find Podcast by ID")
        print("4. Update Podcast")
        print("5. Delete Podcast")
        print("6. Back to Main Menu")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            title = input("Enter podcast title: ").strip()
            genre = input("Enter genre: ").strip()
            try:
                user_id = int(input("Enter user ID (owner): "))
                podcast = Podcast.create_podcast(title, genre, user_id)
                print("✅ Created podcast: ")
            except ValueError:
                print("ℹ️ Invalid user ID.")
            except Exception as e:
                print(f"ℹ️ Error: {e}")

       

        elif choice == "2":
            podcasts = Podcast.get_all()
            if podcasts:
                table = [[p.id, p.title, p.genre, p.user_id] for p in podcasts]
                print(tabulate(table, headers=["ID", "Title", "Genre", "User_ID"], tablefmt="fancy_grid"))
            else:
                print("ℹ️ No podcasts found.")

        elif choice == "3":
            try:
                podcast_id = int(input("Enter podcast ID: "))
                podcast = Podcast.find_by_id(podcast_id)
                if podcast:
                    table = [[podcast.id, podcast.title, podcast.genre, podcast.user_id]]
                    print(tabulate(table, headers=["ID", "Title", "Genre", "User_ID"], tablefmt="fancy_grid"))
                else:
                    print("ℹ️ Podcast not found.")
            except ValueError:
                print("ℹ️ Invalid podcast ID.")

        elif choice == "4":
            try:
                podcast_id = int(input("Enter podcast ID to edit: "))
                podcast = Podcast.find_by_id(podcast_id)
                if podcast:
                    print(f"Editing: {podcast}")
                    new_title = input("New title (Enter to skip): ").strip()
                    new_genre = input("New genre (Enter to skip): ").strip()
                    new_user_id = input("New user ID (Enter to skip): ").strip()
                    confirm = input("Are you sure you want to Update the podcast details? (y/n): ").strip().lower()
                    if confirm in ("y","yes"):
                        podcast.update(
                            title=new_title or None,
                            genre=new_genre or None,
                            user_id=int(new_user_id) if new_user_id else None
                        )
                        print("✅ Podcast Updated successfully")
                    elif confirm in ("n", "no"):    
                        print("Thank you for your confirmation! The podcast details were not changed. ")
                    else:
                        print("ℹ️ Invalid input. Please try again with either (y/n) ")    
                else:
                    print("ℹ️ Podcast not found.")
            except ValueError:
                print("ℹ️ Invalid ID.")

        elif choice == "5":
            try:
                podcast_id = int(input("Enter podcast ID to delete: "))
                confirm = input(f"Are you sure you want to delete Podcast? y/n: ").strip().lower()
                if confirm == "y" or confirm == "yes":
                    if Podcast.delete_by_id(podcast_id):
                        print("✅ Podcast deleted.")
                    else:
                        print("ℹ️ Podcast not found.")
                elif confirm == "n" or confirm == "no":
                    print("Thank you for your confirmation 👍. The podcast was not deleted!")      
                    continue
                else:
                    print("Please enter y or n")      
            except ValueError:
                print("ℹ️ Invalid podcast ID.") 


        elif choice == "6":
            break
        else:
            print("ℹ️ Invalid input. Try again.")


# ----------------------------- Episode Menu -----------------------------
def parse_duration(duration_str):
    try:
        if ':' in duration_str:
            minutes, seconds = map(int, duration_str.split(':'))
            total_minutes = minutes + (seconds / 60)
            return int(round(total_minutes))
        else:
            return int(duration_str)
    except:
        return None

def episode_menu():
    while True:
        print("\n🎧 Episode Menu")
        print("1. Create Episode")
        print("2. Delete Episode")
        print("3. View All Episodes")
        print("4. Find Episode by ID")
        print("5. Mark Episode Listened")
        print("6. Rate Episode")
        print("7. Add/Edit Note")
        print("8. Update Episode")
        print("9. Back to Main Menu")

        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            title = input("Enter episode title: ").strip()
            duration_str = input("Enter duration (e.g., 25:30 or 25): ").strip()
            duration = parse_duration(duration_str)
            if duration is None:
                print("ℹ️ Invalid duration format.")
                continue
            try:
                podcast_id = int(input("Enter podcast ID: "))
                episode = Episode.create_episode(title, duration, podcast_id)
                print(f"✅ Created episode: {episode}")
            except ValueError:
                print("ℹ️ Invalid podcast ID.")
            except Exception as e:
                print(f"ℹ️ Error: {e}")

        elif choice == "2":
            try:
                episode_id = int(input("Enter episode ID to delete: "))
                confirm = input("Are you sure you want to delete episode? y/n: ").strip().lower()
                if confirm in ("y", "yes"):
                    if Episode.delete_by_id(episode_id):
                        print("✅ Episode deleted.")
                    else:
                        print("ℹ️ Episode not found.")
                elif confirm in ("n", "no"):
                    print("Thank you for your confirmation 👍. The episode was not deleted!")        
                else:
                    print("Please enter y or n.")    
            except ValueError:
                print("ℹ️ Invalid episode ID.")

        elif choice == "3":
            episodes = Episode.get_all()
            if episodes:
                table = [[e.id, e.title, e.duration, e.listened, e.rating, e.note, e.podcast_id] for e in episodes]
                print(tabulate(table, headers=["ID", "Title", "Duration", "Listened", "Rating", "Note", "Podcast_ID"], tablefmt="fancy_grid"))
            else:
                print("ℹ️ No episodes found.")

        elif choice == "4":
            try:
                episode_id = int(input("Enter episode ID: "))
                episode = Episode.find_by_id(episode_id)
                print(episode if episode else "ℹ️ Episode not found.")
            except ValueError:
                print("ℹ️ Invalid episode ID.")

        elif choice == "5":
            try:
                episode_id = int(input("Enter episode ID to mark listened: "))
                episode = Episode.find_by_id(episode_id)
                if episode:
                    episode.mark_listened()
                    print("✅ Episode marked as listened.")
                else:
                    print("ℹ️ Episode not found.")
            except ValueError:
                print("ℹ️ Invalid episode ID.")

        elif choice == "6":
            try:
                episode_id = int(input("Enter episode ID to rate: "))
                episode = Episode.find_by_id(episode_id)
                if episode:
                    rating = int(input("Enter rating (1-10): "))
                    if 1 <= rating <= 10:
                        episode.update(rating=rating)
                        print("✅ Episode rated.")
                    else:
                        print("ℹ️ Rating must be between 1 and 10.")
                else:
                    print("ℹ️ Episode not found.")
            except ValueError:
                print("ℹ️ Invalid input.")

        elif choice == "7":
            try:
                episode_id = int(input("Enter episode ID to add/edit note: "))
                episode = Episode.find_by_id(episode_id)
                if episode:
                    note = input("Enter note: ").strip()
                    episode.update(note=note)
                    print("✅ Note updated.")
                else:
                    print("ℹ️ Episode not found.")
            except ValueError:
                print("ℹ️ Invalid episode ID.")

        elif choice == "8":
            try:
                episode_id = int(input("Enter episode ID to update: "))
                episode = Episode.find_by_id(episode_id)
                if episode:
                    print(f"Editing: {episode}")
                    new_title = input("New title (Enter to skip): ").strip()
                    new_duration_str = input("New duration (e.g., 25:30 or 25, Enter to skip): ").strip()
                    new_duration = parse_duration(new_duration_str) if new_duration_str else None
                    new_listened = input("Listened? (y/n, Enter to skip): ").strip().lower()
                    new_listened_val = None
                    if new_listened in ("y", "yes"):
                        new_listened_val = True
                    elif new_listened in ("n", "no"):
                        new_listened_val = False
                    new_rating_str = input("New rating (1-10, Enter to skip): ").strip()
                    new_rating = int(new_rating_str) if new_rating_str.isdigit() else None
                    new_note = input("New note (Enter to skip): ").strip()
                    new_note_val = new_note if new_note else None

                    episode.update(
                        title=new_title or None,
                        duration=new_duration,
                        listened=new_listened_val,
                        rating=new_rating,
                        note=new_note_val
                    )
                    print("✅ Episode updated.")
                else:
                    print("ℹ️ Episode not found.")
            except ValueError:
                print("ℹ️ Invalid input.")

        elif choice == "9":
            break
        else:
            print("ℹ️ Invalid input. Try again.")
import json
from chatbot import chat_with_ai

ROOMS_FILE = "rooms.json"

def load_rooms():
    with open(ROOMS_FILE, "r") as f:
        return json.load(f)

def save_rooms(data):
    with open(ROOMS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def list_rooms():
    rooms = load_rooms()["rooms"]
    print("\nAvailable Rooms:")
    for room in rooms:
        status = "✅ Available" if not room["reserved"] else "❌ Reserved"
        print(f"Room {room['id']}: {room['name']} - {status}")

def reserve_room(room_id):
    data = load_rooms()
    for room in data["rooms"]:
        if room["id"] == room_id:
            if room["reserved"]:
                print(f"Room {room_id} is already reserved ❌")
                return
            else:
                room["reserved"] = True
                save_rooms(data)
                print(f"Room {room_id} has been reserved successfully ✅")
                return
    print("Room not found!")

def main():
    print("🏡 Welcome to Smart Room Reservation System 🏡")
    while True:
        print("\nOptions:")
        print("1. List rooms")
        print("2. Reserve a room")
        print("3. Chat with AI")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            list_rooms()
        elif choice == "2":
            try:
                room_id = int(input("Enter room number: "))
                reserve_room(room_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            msg = input("You: ")
            print("AI:", chat_with_ai(msg))
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again!")


from core.organizer import FileOrganizer
import os

def test_organizer():
    organizer = FileOrganizer(base_path="./test_organized")
    
    # Create test file
    with open("test_move.txt", "w") as f: f.write("test")
    
    res = organizer.move_file("test_move.txt", "TextFiles")
    print(f"Move result: {res}")
    
    if res and os.path.exists(res):
        print("Move successful.")
        # Cleanup
        os.remove(res)
    
    if os.path.exists("./test_organized"):
        import shutil
        shutil.rmtree("./test_organized")

if __name__ == "__main__":
    test_organizer()

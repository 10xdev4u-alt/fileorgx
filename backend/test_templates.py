from utils.templates import apply_template, get_available_templates
import os
import shutil

def test_templates():
    print(f"Templates: {get_available_templates()}")
    
    res = apply_template("./test_template", "Media")
    if res and os.path.exists("./test_template/Photos"):
        print("Template applied successfully.")
        shutil.rmtree("./test_template")

if __name__ == "__main__":
    test_templates()

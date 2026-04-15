from utils.ignore import IgnoreMatcher

def test_ignore():
    matcher = IgnoreMatcher()
    
    files = [
        "data.txt",
        "error.log",
        "temp_file.tmp",
        "node_modules/index.js",
        ".git/HEAD",
        "README.md"
    ]
    
    print("Testing ignore patterns:")
    for f in files:
        ignored = matcher.should_ignore(f)
        print(f"{f}: {'Ignored' if ignored else 'Kept'}")
        
    assert matcher.should_ignore("error.log")
    assert not matcher.should_ignore("README.md")

if __name__ == "__main__":
    test_ignore()

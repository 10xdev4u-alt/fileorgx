from utils.taxonomy import suggest_category_for_tag, get_all_categories

def test_taxonomy():
    print(f"Categories: {get_all_categories()}")
    print(f"Category for 'Invoice': {suggest_category_for_tag('Invoice')}")
    print(f"Category for 'Photo': {suggest_category_for_tag('Photo')}")

if __name__ == "__main__":
    test_taxonomy()

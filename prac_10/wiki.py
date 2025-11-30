import wikipedia

def main():
    """Prompt for page title  and show wikipedia page details."""
    title = input("Enter page title: ")
    while title != "":
        get_page(title)
        print()
        title = input("Enter page title: ")
    print("Thank you.")

def get_page(title):
    """Return wikipedia page for the given title"""
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)

    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)

    except wikipedia.exceptions.PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')


if __name__ == "__main__":
    main()


SHOWS = [
    "the Family MAN",
    "   croOks",
    "the Simpsons",
    "the Office",
    "the BIG Bang THEORY",
    "  the Good Place",
    "the Walking Dead",
    "  the Handmaid's Tale",
    "the Flash",
]
def main():
    cleaned_shows = []
    for show in SHOWS:
        # print(show.title().strip())
        cleaned_shows.append(show.title().strip())
    print(' , '.join(cleaned_shows))

main()
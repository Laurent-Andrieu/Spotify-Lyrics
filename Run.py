def run():
    try:
        import Spotify
        import Lyrics
        import Link
    except ImportError as err:
        return err
    else:
        conn = Spotify.Connexion(client_id="0bd78e654f754f129dc80d43520bac30",
                                 client_secret="921955a7e0ad45a687676d23f927f046",
                                 redirect_url="http://localhost:8000/",
                                 user="213tzif5o7rzyxtijuqdgtfuq",
                                 scope="user-read-currently-playing")
        conn.get_token()
        song = conn.track_data()
        path = r'C:\Users\Laurent\Documents\geckodriver-v0.26.0-win64\geckodriver.exe'
        finder = Link.Link(song, path)
        link = finder.search()
        lyrics = Lyrics.Find(link)
        lyrics = lyrics.print_lyrics()
        print(lyrics)


if __name__ == '__main__':
    run()

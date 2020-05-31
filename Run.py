def run():
    try:
        import Spotify
        import Lyrics
        import Link
    except ImportError as err:
        return err
    else:
        # Establishing a connexion to Spotify Personnal Application
        conn = Spotify.Connexion(client_id="",
                                 client_secret="",
                                 redirect_url="http://localhost:8000/",
                                 user="",
                                 scope="user-read-currently-playing")
        # Get a token
        conn.get_token()
        # Ask for the current playing song
        song = conn.track_data()
        # Pass needful data for web scraping
        link = Link.Link(song, path)
        # Search for the song
        song_page = link.search()
        # Get the lyrics
        lyrics = Lyrics.Find(song_page)
        lyric = lyrics.print_lyrics()


path = r''


if __name__ == '__main__':
    run()

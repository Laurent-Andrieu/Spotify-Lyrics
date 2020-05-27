def run():
    try:
        import Spotify
    except ImportError as err:
        return err
    else:
        conn = Spotify.Connexion(client_id="",
                                 client_secret="",
                                 redirect_url="http://localhost:8000/",
                                 user="",
                                 scope="user-read-currently-playing")
        conn.get_token()
        artist, name = conn.track_data()
        print(artist, name)


if __name__ == '__main__':
    run()

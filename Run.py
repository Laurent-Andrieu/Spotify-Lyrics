import Spotify
import Lyrics
import Driver
import time


def run():
    # Pass the arguments
    conn = Spotify.Connexion(client_id="",
                             client_secret="",
                             redirect_url="http://localhost:8000/",
                             user="",
                             scope="user-read-currently-playing")
    # Get a token
    conn.get_token()
    path = r''
    # Initiate the driver parameters
    driver = Driver.Link(path)

    # While token is valid, if the song changes
    actual = None
    while conn.token:
        song = conn.track_data()
        time.sleep(1)
        if song != actual:
            actual = song
            print(actual)
            if not driver.state['running']:
                driver.start_driver()
                driver.window_handle()
                driver.search(actual)
                driver.browse()
            elif driver.state['running']:
                driver.window_handle()
                driver.search(actual)
                driver.browse()


if __name__ == '__main__':
    run()

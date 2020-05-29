from spotipy.util import prompt_for_user_token
import spotipy
import os


class SetCreditentials:

    def __init__(self, client_id: str, client_secret: str, redirect_url: str):
        self.CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
        self.CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
        self.REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
        os.environ['SPOTIPY_CLIENT_ID'] = client_id
        os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret
        os.environ['SPOTIPY_REDIRECT_URI'] = redirect_url


class Connexion:
    def __init__(self, client_id, client_secret, redirect_url, user, scope):
        """

        :type client_id: str
        :type client_secret: str
        :type redirect_url: str
        :type user: str
        :type scope: str
        """
        # Authorization Code Flow
        self.user = user
        self.scope = scope
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url
        self.token = None

    def get_token(self):
        try:
            SetCreditentials(self.client_id, self.client_secret, self.redirect_url)
            token = prompt_for_user_token(self.user, self.scope)
        except Exception as token_err:
            print(f"Can't get a token:\n{token_err}")
        else:
            self.token = token

    def track_data(self):
        if self.token:
            track = spotipy.Spotify(self.token).current_user_playing_track()
            if track:
                track_data = [t for i, t in enumerate(track.items())]
                track_data = track_data[3][1]["album"]["artists"][0]["name"] + ' ' + track_data[3][1]["name"]
                return track_data
            else:
                print("No track is being played")
                exit()
        elif self.token is None:
            return "Token was not set or is no longer valid"
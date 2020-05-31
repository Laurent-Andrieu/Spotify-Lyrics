# Spotify-Lyrics

This python script allows you to see the lyrics of your current playing song on Spotify.

![Spotify Developer](https://developer.spotify.com/assets/FBImage.png)

---

## Clone the repository

### Windows Users
* Download & Install [Git Bash](https://gitforwindows.org/)

### Linux Users
* Type `sudo apt install git` on your terminal

After Git installation type `git clone https://github.com/Laurent-Andrieu/Spotify-Lyrics/` to clone the repository.

---

## Requirements

###  Python Version 3.8
###  Spotipy Version 2.12.0
* Type `pip install spotipy --upgrade` in your terminal

[Spotipy repository](https://github.com/plamere/spotipy/blob/2.12.0/docs/index.rst) | [Spotipy documentation](https://spotipy.readthedocs.io/en/2.12.0/)
----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------
### [Gecko driver](https://github.com/mozilla/geckodriver/releases)
### For windows users:
### [Visual studio](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)
---

# Create your spotify app

##  Developer portal
Log in the [Developer portal](https://developer.spotify.com/dashboard/login) with your account and create and app.

Once created, go to **EDIT SETTINGS** > **Redirect URIs** and add any link to your local machine, targetting any free port (eg : `https://localhost:8000`)


# Use Spotify-Lyrics

##  [Run.py](https://github.com/Laurent-Andrieu/Spotify-Lyrics/blob/Version1/Run.py)
To run the program, simply call this file. Before you run it, make sure you add your **Profile ID**, your **CLIENT_ID** and **CLIENT_SECRET** from the Developer portal.
You can find your **Profile ID** by going to your account on the **Spotify App** and click on **`...`** > **`Share`** > Copy the Spotify URI. (eg : spotify:user:**`213tzif5o7rzyxtijuqdgtfuq`**)

##  [Spotify.py](https://github.com/Laurent-Andrieu/Spotify-Lyrics/blob/Version2/Spotify.py)
This program contains the `SetCreditential` Class witch will add your IDs in environement variables passed by the `Connexion` Class.
The `Connexion` Class performs the connexion throught the **Authorization Code Flow** authentification method via the `get_token()` function.
It also allows you to call the `track_data()` function to retrive the author and name of the song being played.

##  [Link.py](https://github.com/Laurent-Andrieu/Spotify-Lyrics/blob/Version2/Link.py)
Scrapes [Genius]() for the song returned by `Spotify.Connexion().track_data()`. Also requires the full path of your gecko driver to work.
Searches for the song's 'mini card' and returns its [href]().

## [Lyrics.py](https://github.com/Laurent-Andrieu/Spotify-Lyrics/blob/Version2/Lyrics.py)
Searches for the lyrics of the song.
Returns the lyrics.

---

##  Future immplements
- [ ]  `Terminal.py` : **Lyrics display**.  Prints the lyrics on a terminal.
- [ ]  `View.py` : **GUI**.  Allows the user to see the lyrics on an python based small application.
- [ ]  `Higlight.py`: **Current lyrics higlighting**. Highlights the lyrics in realtime.

##  Commit info
**Author**  | **Date**  | **Improvements**
----------- | --------- | ----------------
Laurent Andrieu | May 31 2020 02:33pm | - [x] `README.md`
  | | | - [x] Version 2 repository
  | | | - [x] + Lyrics.py
  | | | - [x] + Link.py

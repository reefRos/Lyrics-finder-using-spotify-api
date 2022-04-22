import lyricsgenius as lg
import spotipy
from tkinter import *
from tkinter import scrolledtext
from PIL import Image,ImageTk

class LyricsFinder:
    #class variables
    spotify_client_id = None
    spotify_secret = None
    spotify_redirect_url = None
    genius_access_token = None
    window = None
    topFrame = None
    textFrame = None
    authorLabel = None
    lyricsText = None
    oauth_object = None
    prevSong = ''

    #empty constructor
    def __init__(self):
        return None

    #Class constructor
    def __init__(self,spotify_client_id,spotify_secret,genius_access_token):
        self.spotify_client_id = spotify_client_id
        self.spotify_secret = spotify_secret
        self.genius_access_token = genius_access_token
        self.spotify_redirect_url = 'https://google.com'
        self.__initWindow()
        self.window.withdraw()




    def __initWindow(self):
        try:
            self.window = Tk()
            self.window.title("Found song!")
            self.topFrame = Frame(self.window)
            self.topFrame.pack()
            self.textFrame = Frame(self.window)
            self.textFrame.pack()
            self.authorLabel = Label(self.topFrame)
            self.authorLabel.grid(row=0,column=0)
            self.lyricsText = scrolledtext.ScrolledText(self.textFrame,
                                                        width=50,
                                                        height=30,
                                                        font=("Arial", 14))
            self.lyricsText.pack()
            # set the scope of this app to only the users current playing song
            scope = 'user-read-currently-playing'
            # SpotifyOAuth is a class which Creates a Client Credentials Flow Manager and is used in server-to-server authentication
            self.oauth_object = spotipy.SpotifyOAuth(client_id=self.spotify_client_id,
                                                     client_secret=self.spotify_secret,
                                                     redirect_uri=self.spotify_redirect_url,
                                                     scope=scope)
            refreshButton = Button(self.topFrame,text="refresh",command=self.updateText)
            refreshButton.grid(row=0,column=1)
        except Exception as e:
            print(e)


    def updateText(self):# method to refresh the lyrics on the text area. Invoked by clicking refresh button
        try:
            self.window.destroy()
            self.__initWindow()
            self.initProgram()
            self.window.mainloop()
        except Exception as e:
            print(e)

    #Method that initializes the spotipy object and genius object. searches for the song and lyrics
    def initProgram(self):
        try:
            token_dict = self.oauth_object.get_access_token()
            token = token_dict['access_token']

            # our spotify object
            spotify_object = spotipy.Spotify(auth=token)

            # our genius object - grants us access to lyrics
            genius_object = lg.Genius(self.genius_access_token)


            # current song playing - access is granted from spotify object we created earlier.
            current = spotify_object.currently_playing()
            status = current['currently_playing_type']


            # get artists name from "current" object (can also be printed as json using json.dump)
            artist_name = current['item']['album']['artists'][0]['name']
            # get current song's name
            song_title = current['item']['name']
            self.authorLabel.config(text=song_title + " by " + artist_name)
            self.authorLabel.update()

        except Exception as e:
            print(e)
            return None


        # use "genius" object's search song method inorder to look up the songs lyrics. return None if failed
        song = genius_object.search_song(title=song_title, artist=artist_name)
        # returns a string that holds current songs lyrics
        if song is None:
            lyrics = "Couldn't find lyrics for " + song_title + " by " + artist_name
        else:
            lyrics = song.lyrics


        self.lyricsText.delete(1.0,END)
        self.lyricsText.insert('insert',
                               lyrics)
        self.lyricsText.config()
        self.window.deiconify()
        return 1

import random

class Song():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
    
    def __ne__(self, other):
        return not (self == other)
    
    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))


class mediaPlayerQueue:
    def __init__(self, data = 0, current = False):
        self.queue = []
        self.data(data)
        self.currentlyPlaying(current)

    def data(self, index):
        self.data = index


    def add(self, song):

        if self.size() > 0: 
            self.queue.insert(self.size() + 1, song)
        else:
            self.queue.insert(0, song)


    def remove(self, title):
            song_index = 0
            for item in self.queue:
                if item.title == title:
                    break
                song_index += 1
            self.queue.pop(song_index)

    def play(self, song_index):
        self.data = song_index
        self.currentlyPlaying(True)
        
     def next(self):
         if self.curently_playing:
            x = len(self.queue) - 1   
            if self.data == x:
                next_song = 0
            else:
                next_song = self.data + 1
            self.play(next_song)
        else:
            print('\n Please play a song as no song is playing.')
        
    def prev(self):
        if self.curently_playing:
            x = len(self.queue) - 1
            if self.data == 0:
                prev_song = x
            else:
                prev_song = self.data - 1
            self.play(prev_song)
        else:
            print('\n Please play a song as no song is playing.')
            
    def shuffle(self):
        z = self.size()
        
        for i in range(z // 2):
            x = self.queue.pop(0)
            self.queue.append(x)
        
        for i in range(z):
            randomNum = random.randint(0, z - 1)
            x = self.queue.pop(randomNum)
            self.queue.append(x)         

    def currentlyPlaying(self, current):
        self.curently_playing = current
    
    def currentSong(self):
        if self.curently_playing:
            print(self.queue[self.data])
        else:
            print('\n Please play a song as no song is playing.')
    
    def size(self):
        return len(self.queue)

    def playList(self):
        x = 1
        print("\nSong List:\n")
        for item in self.queue:
            print(str(x) + '. ' + str(item))
            x += 1

def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")
    print('\n')
    
mediaPlayer = mediaPlayerQueue()

mediaPlayer.add(Song('Watch the World Burn', 'Falling In Reverse'))
mediaPlayer.add(Song('Thunderstruck', 'AC/DC'))
mediaPlayer.add(Song('Cemetary Gates', 'Pantera'))
mediaPlayer.add(Song('Last Resort', 'Papa Roach'))
mediaPlayer.add(Song('Kashmir', 'Led Zeppelin'))
mediaPlayer.add(Song('One', 'Metallica'))


while True:
    menu()
    choice = int(input())
    
    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        addSong = input('Please enter the song title: ')
        addArtist = input('Please enter the artist name: ')
        # Add song to playlist
        newSong = Song(addSong, addArtist)
        mediaPlayer.add(newSong)
        print("New Song Added to Playlist: ", addSong, addArtist)
    elif choice == 2:
        # Prompt user for Song Title 
        title = input('Enter the Song Title to be Removed: ')
        # remove song from playlist
        mediaPlayer.remove(title)
        print("Removed from Playlist: ", title)
    elif choice == 3:
        # Play the playlist from the beginning
        mediaPlayer.play(0)
        # Display song name that is currently playing
        print("Playing....")
        mediaPlayer.currentSong()       
    elif choice == 4:
        # Skip to the next song on the playlist
        mediaPlayer.next()
        # Display song name that is now playing
        print("Skipping....") 
        mediaPlayer.currentSong()                    
    elif choice == 5:
        # Go back to the previous song on the playlist
        mediaPlayer.prev()
        # Display song name that is now playing
        print("Replaying....")  
        mediaPlayer.currentSong()
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        mediaPlayer.shuffle()
        mediaPlayer.play(0)
        # Display song name that is now playing
        print("Shuffling....") 
        mediaPlayer.currentSong()         
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")
        mediaPlayer.currentSong()    
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        mediaPlayer.playList()
    elif choice == 0:
        print("Goodbye.")
        break

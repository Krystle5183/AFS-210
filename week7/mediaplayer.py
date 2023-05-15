import _random


class Song:
    def __init__(self,title,artist):
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
    
class MediaPlayer:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0
        
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def playList_size(self) -> int:
        return self.count
    
    def addSong(self, data) -> None:
        node = Song(data)
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            
    def delete(self, data) -> None:
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next
            
    def merge(nlist,lefthalf,righthalf):
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
        return 
    
while True:
    menu()
    choice = int(input())
    
    playList = MediaPlayer()
      
    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        newSongTitle = input('Enter the song title: ')
        newSongArtist = input('Enter the artist name: ')
        newSong = Song(newSongTitle, newSongArtist)
        # Add song to playlist
        newSong.addSong()
        print("New Song Added to Playlist")
        print(playList)
    elif choice == 2:
        # Prompt user for Song Title 
        deleteSongTitle = input('Enter song title to be removed: ')
        # remove song from playlist
        playList.delete(deleteSongTitle)
        print("Song Removed to Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        playList(newSong)
        # Display song name that is currently playing
        print(playList.getTitle)
        print("Playing....")        
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")                     
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        playList.merge(lefthalf, righthalf)
        print(playList[0])
        # Display song name that is now playing
        print(newSongTitle)
        print("Shuffling....")          
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print(newSongTitle)
        print(newSongArtist)
        print("Currently playing: ", end=" ")    
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        print(playList)
    elif choice == 0:
        print("Goodbye.")
        break

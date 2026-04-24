print("--- The DJ Playlist Robot ---")

# Let's create a list of songs!
playlist = ["Twinkle Twinkle", "Happy Birthday", "Baby Shark", "Shakira", "BTS song"]

print("\nStarting the playlist automatically...")

# A FOR LOOP
# "song" is a temporary variable that holds the current item.
# The loop will happen 3 times because there are 3 songs in the list!
for song in playlist:
    print("Now singing:" "My favourite song is:", song)

print("\nPlaylist finished. Notice how Python did the repetitive work for me!")
playlist.append("yoyo")
print(playlist)
for song in playlist:
    print(song)

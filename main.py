from pytube import Playlist

p = input("Enter the url of the playlist: \t")
purl = Playlist(p)

print(f'Downloading: {p.title}')

for video in purl.videos:
    print(f'Current: {video.title}')
    st = video.streams.get_highest_resolution()
    st.download()
    #video.streams.first().download()
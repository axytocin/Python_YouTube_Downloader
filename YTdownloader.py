import pytube

link = input('Enter The Link: ')
yt = pytube.YouTube(link)
yt.streams.first().download()
print(f'Downloaded {link}')

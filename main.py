import os
from pytube import Playlist


# Fonction pour nettoyer les titres de vidéos
def clean_title(title):
    # Remplacez les caractères non valides par des tirets ou un autre caractère valide
    return "".join([c if c.isalnum() or c in " -_" else "-" for c in title])

# Remplacez l'URL ci-dessous par l'URL de votre playlist YouTube
playlist_url = p = input("Enter the url of the playlist: \t")

playlist = Playlist(playlist_url)

# Affiche le nombre de vidéos dans la playlist
print(f'Nombre de vidéos dans la playlist: {playlist.title} -- {len(playlist.video_urls)}')

# Télécharge toutes les vidéos de la playlist en haute qualité avec numérotation
for i, video in enumerate(playlist.videos, 1):
    print(f'En cours: {video.title} \n')
    # Sélectionnez le flux avec la résolution la plus élevée disponible
    stream = video.streams.get_highest_resolution()
    # Obtenez l'extension du fichier à partir du flux
    file_extension = stream.mime_type.split('/')[-1]
    # Formatte le numéro avec un zéro initial si nécessaire
    video_number = f'{i:02d}'
    # Ajoute le numéro au début du titre de la vidéo
    video_title_with_number = f'{video_number} - {clean_title(video.title)}.{file_extension}'
    # Télécharge la vidéo avec le nouveau titre
    stream.download(filename=video_title_with_number)
    print(f'Téléchargement terminé en haute qualité: {video_title_with_number} \n')
    print('-----------------------------------------\n')

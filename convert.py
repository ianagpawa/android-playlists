import os

def convertPlaylist(filename, output_filename):
    playlist = open(filename, 'r+', encoding='utf-8')
    arr = playlist.readlines()
    newArr = []
    newPlaylist = open(output_filename, 'w+', encoding='utf-8')
    for song_path in arr:
        newPlaylist.writelines(song_path.replace("\\", "/"))
    playlist.close()
    newPlaylist.close()

def convertAll():
    origin = os.getcwd()
    original_folder = origin + "\playlists"
    os.chdir(original_folder)

    playlist_names = os.listdir(original_folder)
    for playlist in playlist_names:
        if playlist.endswith("m3u"):
            filename = "%s/%s" % (original_folder, playlist)
            output_filename ="%s/output/%s" % (origin, playlist)
            convertPlaylist(filename, output_filename)
            print("%s has been converted" % playlist)

    print("All playlilsts have been converted!")
    os.chdir(origin)

convertAll()
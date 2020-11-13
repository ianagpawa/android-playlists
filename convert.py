import os
import subprocess
import shutil

def replaceFileName(file_name):
    return file_name.replace("\\", "/")

# string = str("..\Music\Yazoo\Upstairs at Eric's\09 - Situation.mp3")
# # print("this= ", replaceFileName(u"..\Music\Yazoo\Upstairs at Eric's\09 - Situation.mp3"))
# print(string)

def convertPlaylist(filename, destination_filename):
    playlist = open(filename, 'r+')
    arr = playlist.readlines()
    newArr = []
    newPlaylist = open(destination_filename, 'w+')
    for song_path in arr:
        newPlaylist.writelines(replaceFileName(song_path))
    playlist.close()
    newPlaylist.close()

convertPlaylist("./playlists/Coolin'.m3u", "./output/Coolin'.m3u")
# convertPlaylist("./playlists/Frou.m3u", "./output/Frou.m3u")
convertPlaylist("./playlists/Chillipity hop.m3u", "./output/Chillipity hop.m3u")
convertPlaylist("./playlists/Cuts.m3u", "./output/Cuts.m3u")
convertPlaylist("./playlists/Howlin.m3u", "./output/Howlin.m3u")
convertPlaylist("./playlists/Oneirophrenia.m3u", "./output/Oneirophrenia.m3u")

def get_m3u(filename):
    return filename[-3:] == 'm3u'


# def convertAll():
#     origin = os.getcwd()

#     destination_folder = origin + "C:\Users\onyx\Desktop\playlists"
#     destination_copy = origin + "C:\Users\onyx\Desktop\original"

#     playlist_folder = "C:\Users\onyx\Desktop\original"

#     os.chdir(playlist_folder)

#     playlist_names = os.listdir(playlist_folder)

#     for playlist in playlist_names:
#         if get_m3u(playlist):
#             convertPlaylist(playlist, destination_folder)
#             print "%s has been converted" % playlist

#             source = playlist_folder + "/" + playlist
#             dest_cp = destination_copy + "/" + playlist
#             shutil.copy2(source, dest_cp)
#             print "%s has been copied to Playlists directory\n" % playlist

#     print "All playlilsts have been converted!"
#     os.chdir(origin)

# # convertAll()

# test_playlist = "Playlists/80s.m3u"
# destination_test = '80s.m3u'
#
# convertPlaylist(test_playlist, destination_test)
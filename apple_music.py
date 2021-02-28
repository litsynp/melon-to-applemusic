"""

POST https://api.music.apple.com/v1/me/library/playlists

{
   "attributes":{
      "name":"Some Playlist",
      "description":"My description"
   },
   "relationships":{
      "tracks":{
         "data":[
            {
               "id":"900032829",
               "type":"songs"
            }
         ]
      }
   }
}

Add a track to playlist
POST https://api.music.apple.com/v1/me/library/playlists/{id}/tracks
{
   "data":[
      {
         "id":"201281527",
         "type":"songs"
      },
      {
         "id":"639032181",
         "type":"music-videos"
      }
   ]
}
"""


class AppleMusic:
    """
    A class to manage and manipulate data for Apple Music.
    """

    def get_playlists(self):
        """
        Fetch all the library playlists in alphabetical order.
        """
        # GET https://api.music.apple.com/v1/me/library/playlists

    def create_playlist(self, playlist_name):
        """
        Create a new library playlist to the Apple Music account.
        """
        if playlist_name is None:
            print('Please specify the name of the playlist to create.')
            return

        # POST https://api.music.apple.com/v1/me/library/playlists

    def add_tracks_to_playlist(self, playlist_id, music_id_list):
        """
        Add a new track to a library playlist.
        """
        if playlist_id is None:
            print('Please specify the ID of the playlist to add.')
            return

        if len(music_id_list) < 1:
            print('Please include at least one ID of a track to add to the playlist.')
            return

        # POST https://api.music.apple.com/v1/me/library/playlists/{id}/tracks

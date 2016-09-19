from datetime import timedelta
from typing import List
from collections import Counter, defaultdict
from random import shuffle as shuffle_list
import json


class Song:
    def __init__(self, title: str, artist: str, album: str, length: str):
        split_len = length.split(':')

        if len(split_len) == 3:
            self._hours, self._minutes, self._seconds = map(int, split_len)
        elif len(split_len) == 2:
            self._hours = 0
            self._minutes, self._seconds = map(int, split_len)
        else:
            raise ValueError('Invalid length: {}'.format(length))

        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def get_length(self, seconds=False, minutes=False, hours=False):
        time = timedelta(hours=self._hours, minutes=self._minutes, seconds=self._seconds)

        total_seconds = time.total_seconds()

        if seconds:
            return round(total_seconds, 2)
        elif minutes:
            return round(total_seconds / 60, 2)
        elif hours:
            return round(total_seconds / 3600, 2)

        return time

    def __str__(self):
        return '{} - {} [{}] ({})'.format(self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist

    def __hash__(self):
        return hash((self.title, self.artist))


class Playlist:
    def __init__(self, name: str, repeat: bool=False, shuffle: bool=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self._songs = []

    def add_song(self, song: Song):
        if song not in self._songs:
            self._songs.append(song)
        else:
            print('{} is already in the playlist.'.format(song))

    def remove_song(self, song: Song):
        if song in self._songs:
            self._songs.remove(song)
        else:
            print('{} is not in the playlist.'.format(song))

    def add_songs(self, songs: List[Song]):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        return len(self._songs)

    def artists(self):
        artists = Counter([song.artist for song in self._songs])

        for artist, songs in sorted(artists.items()):
            print('{} - {} '.format(artist, songs), end='')
            print('song.' if songs == 1 else 'songs.')

    def next_song(self):
        if self.shuffle:
            self._songs = shuffle_list(self._songs)

        ...

    @staticmethod
    def _print_split_lines(string_format, artist_padding, title_padding, length_padding):
        print(string_format.format(
            '-' * artist_padding, artist_padding,
            '-' * title_padding, title_padding,
            '-' * length_padding, length_padding
        ))

    def pprint_playlist(self):
        artist_str = 'Artist'
        song_str = 'Song'
        length_str = 'Length'

        artist_padding = max([len(song.artist) for song in self._songs])
        title_padding = max([len(song.title) for song in self._songs])
        length_padding = max([len(song.length) for song in self._songs])

        artist_padding = artist_padding if artist_padding >= len(artist_str) else len(artist_str)
        title_padding = title_padding if title_padding >= len(song_str) else len(song_str)
        length_padding = length_padding if length_padding >= len(length_str) else len(length_str)

        string_format = '| {:<{}} | {:<{}} | {:<{}} |'

        print(string_format.format(
            artist_str, artist_padding,
            song_str, title_padding,
            length_str, length_padding
        ))
        self._print_split_lines(string_format, artist_padding, title_padding, length_padding)

        for song in sorted(self._songs, key=lambda s: s.artist):
            print(string_format.format(
                song.artist, artist_padding,
                song.title, title_padding,
                song.length, length_padding
            ))

        self._print_split_lines(string_format, artist_padding, title_padding, length_padding)

    def save(self):
        filename = self.name.replace(' ', '-') + '.json'

        playlist = defaultdict(dict)

        for song in self._songs:
            playlist[song.artist][song.album] = {
                s.title: s.length
                for s in filter(lambda s: s.artist == song.artist and s.album == song.album, self._songs)
            }

        with open(filename, mode='w') as f:
            json.dump(playlist, f, indent=4)

    @staticmethod
    def load(filename: str):
        playlist = Playlist(name=filename.replace('-', ' ').replace('.json', ''))

        with open(filename, mode='r') as f:
            playlist_data = json.load(f)

            for artist in playlist_data:
                for album in playlist_data[artist]:
                    for title, length in playlist_data[artist][album].items():
                        s = Song(title=title, artist=artist, album=album, length=length)
                        playlist.add_song(s)

        return playlist

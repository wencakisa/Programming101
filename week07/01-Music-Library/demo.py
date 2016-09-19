import sys

from music import Song, Playlist


def main():
    p = Playlist(name='za ceniteli')

    p.add_songs([
        Song(title='Domination', artist='Pantera', album='Cowboys From Hell', length='05:04'),
        Song(title='This Love', artist='Pantera', album='Vulgar display of power', length='04:54'),
        Song(title='Walk', artist='Pantera', album='Vulgar display of power', length='03:54'),
        Song(title='Momicheto', artist='Hipodil', album='Nadurveni vuglishta', length='03:09')
    ])

    p.pprint_playlist()
    p.save()

    print('*' * 50)

    p = Playlist.load('za-ceniteli.json')

    p.add_songs([
        Song(title='Vurtianalen SEX', artist='Hipodil', album='Nadurveni vuglishta', length='04:04'),
        Song(title='Kolio Piqndeto', artist='Obraten Efekt', album='Efekten Obrat', length='03:31'),
        Song(title='Polet', artist='Obraten Efekt', album='Vervaite ni', length='03:50'),
        Song(title='Choki', artist='Obraten Efekt', album='Vervaite ni', length='04:09')
    ])

    p.pprint_playlist()
    p.save()

if __name__ == '__main__':
    sys.exit(main())

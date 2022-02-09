class Show:
    def __init__(self, name, year):
        self.__name = name.title()
        self.year = year
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @property
    def likes(self):
        return self.__likes

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()

    @likes.setter
    def likes(self, value):
        self.__likes = value

    def __str__(self):
        return f"{self.name} - {self.year} - {self.likes}"


class Movie(Show):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f"{self.name} - {self.year} - {self.duration} min - {self.likes} likes"


class Series(Show):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f"{self.name} - {self.year} - {self.seasons} seasons - {self.likes} likes"


class Playlist:
    def __init__(self, name, shows):
        self.name = name
        self.__shows = shows

    def __getitem__(self, item):
        return self.__shows[item]

    def __len__(self):
        return len(self.__shows)


# Testing
# avengers = Filme("avengers", 2018, 160)
# atlanta = Serie("atlanta", 2018, 2)
# tring = Filme("The ring", 2002, 100)
# daredevil = Serie("daredevil", 2016, 2)
#
# avengers.dar_like()
# atlanta.dar_like()
# tring.dar_like()
# daredevil.dar_like()
# daredevil.dar_like()
#
# movies_series = [avengers, atlanta, daredevil, tring]
# weekend_playlist = Playlist("weekend", movies_series)
#
# print(f"Playlist size: {len(weekend_playlist)}")
#
# for programa in weekendplaylist:
#     print(shows)

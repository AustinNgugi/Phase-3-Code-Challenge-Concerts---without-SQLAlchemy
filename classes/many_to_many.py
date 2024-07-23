class Band:
    def __init__(self, name, hometown):
        self._name = None
        self.name = name  
        self._hometown = hometown
        self.concert_list = []  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(value, 'capitalize') and callable(getattr(value, 'capitalize')):
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def hometown(self):
        return self._hometown
    @hometown.setter
    def hometown(self, value):
        if isinstance(value, str) and hasattr(value, '__len__') and len(value) > 0:
            self._hometown = value
        else:
            raise ValueError("Hometown must be a non-empty string")
    @property
    def concerts(self):
        return self.concert_list

    @property
    def venues(self):
        return list(set([concert.venue for concert in self.concert_list]))

    def play_in_venue(self, venue, date):
        new_concert = Concert(date, self, venue)
        self.concert_list.append(new_concert)
        venue.add_concert(new_concert)
        return new_concert

    def all_introductions(self):
        if not self.concerts:
            return None
        introductions = []
        for concert in self.concerts:
            introductions.append(concert.introduction())
        return introductions


class Concert:
    def __init__(self, date, band, venue):
        self._date = None
        self.date = date  
        self._band = band
        self._venue = venue
        self.venue.add_concert(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError("Band must be of type Band")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError("Venue must be of type Venue")

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self._name = None
        self.name = name  
        self._city = city
        self.concerts_list = []  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string")

    def concerts(self):
        if not self.concerts_list:
            return None
        return self.concerts_list

    def bands(self):
        if not self.concerts_list:
            return None
        bands_set = set([concert.band for concert in self.concerts_list])
        return list(bands_set)

    def add_concert(self, concert):
        self.concerts_list.append(concert)

# Write your solution here:


class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.genre_list = ", ".join(self.genres)
        self.ratings = []
        self.avg_rating = 0

    def __str__(self):
        if self.avg_rating == 0:
            return f'{self.title} ({self.seasons} seasons)\ngenres: {self.genre_list}\nno ratings'
        else:
            return f'{self.title} ({self.seasons} seasons)\ngenres: {self.genre_list}\n{(len(self.ratings))} ratings, average {self.avg_rating} points'

    def rate(self, rating: int):
        self.ratings.append(rating)
        avg_rating = sum(self.ratings) / len(self.ratings)
        self.avg_rating = round(avg_rating, 1)


def minimum_grade(rating: float, series_list: list):
    results = []
    for series in series_list:
        if series.avg_rating >= rating:
            results.append(series)
    return results


def includes_genre(genre: str, series_list: list):
    results = []
    for series in series_list:
        if genre in series.genres:
            results.append(series)
    return results


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])





# s1.rate(0)
# print(s1)

# s2 = Series("South Park", 24, ["Animation", "Comedy"])
# s2.rate(3)

# s3 = Series("Friends", 10, ["Romance", "Comedy"])
# s3.rate(2)

# series_list = [s1, s2, s3]

# print("a minimum grade of 4.5:")
# for series in minimum_grade(4.5, series_list):
#     print(series.title)

# print("genre Comedy:")
# for series in includes_genre("Comedy", series_list):
#     print(series.title)

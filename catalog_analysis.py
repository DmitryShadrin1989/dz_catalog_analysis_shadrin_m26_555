import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    sum_rating = sum(m["rating"] for m in movies)

    return round(sum_rating / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = list(map(lambda film: current_year - film["year"], movies))

    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 5:
        return "хорошо" if rating >= 7 else "средне"
    else:
        return "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


def main():
    # Этап 1. Разминка: переменные, числа, math
    avg_rating = average_rating(movies=movies)
    print(f"avg_rating = {avg_rating}")

    oldest_age, newest_age, avg_age = catalog_age_stats(movies=movies)
    print(f"oldest_age = {oldest_age}, newest_age = {newest_age}, avg_age = {avg_age}")

    print(duration_in_hours(135))

    # Этап 2. Условия и match
    print(f"rating = 3, tier - {rating_tier(3)}")
    print(f"rating = 5, tier - {rating_tier(5)}")
    print(f"rating = 5.1, tier - {rating_tier(5.1)}")
    print(f"rating = 7, tier - {rating_tier(7)}")
    print(f"rating = 9, tier - {rating_tier(9)}")
    print(f"rating = 9.1, tier - {rating_tier(9.1)}")

    print(f"year = 2014, label - {decade_label(2014)}")
    print(f"year = 2015, label - {decade_label(2015)}")
    print(f"year = 2016, label - {decade_label(2016)}")
    print(f"year = 2020, label - {decade_label(2020)}")
    print(f"year = 2021, label - {decade_label(2021)}")


if __name__ == "__main__":
    main()

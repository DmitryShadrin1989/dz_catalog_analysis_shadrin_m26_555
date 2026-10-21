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


def print_non_comedy_titles(movies):
    for film in movies:
        if "comedy" in film["genres"]:
            continue
        print(film["title"])


def print_first_masterpiece(movies, above=9.0):
    index = 0
    while index < len(movies):
        film = movies[index]
        if film["rating"] > above:
            print(film["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for film in movies:
        if film["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    words_list = title.split()
    result = ""
    for word in words_list:
        if result != "":
            result += " "
        result += word[0].upper() + word[1:]
    return result


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


def show_examples():
    def print_stage(stage):
        print("-----------------------------------------------------------")
        print(stage)
        print("-----------------------------------------------------------")

    print_stage("Этап 1. Разминка: переменные, числа, math")
    avg_rating = average_rating(movies=movies)
    print(f"avg_rating = {avg_rating}")
    oldest_age, newest_age, avg_age = catalog_age_stats(movies=movies)
    print(f"oldest_age = {oldest_age}, newest_age = {newest_age}, avg_age = {avg_age}")
    print(duration_in_hours(135))

    print_stage("Этап 2. Условия и match")
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

    print_stage("Этап 3. Циклы")
    print("Фильмы не в жанре comedy:")
    print_non_comedy_titles(movies=movies)
    print("Первый шедевр во всем каталоге:")
    print_first_masterpiece(movies=movies)
    print("Первый шедевр в первых трех фильмах:")
    print_first_masterpiece(movies=movies[:3])
    print(f"Фильмов длиннее 120 минут: {count_long_movies(movies=movies)}")

    print_stage("Этап 4. Строки")
    print("Результат normalize_title:")
    print(normalize_title(title="silent hours"))
    print("Результат make_slug:")
    print(make_slug(title="Silent Hours"))
    print("Результат format_report_line:")
    print(format_report_line(movie=movies[0]))
    print(format_report_line(movie=movies[1]))
    print(format_report_line(movie=movies[2]))


def main():
    show_examples()


if __name__ == "__main__":
    main()

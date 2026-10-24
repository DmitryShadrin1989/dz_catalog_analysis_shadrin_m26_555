# Анализ каталога фильмов

Домашнее задание по Python: функции для анализа небольшого каталога фильмов
и итоговый консольный отчёт по нему.

Выполнил: Шадрин Дмитрий, группа М26-555.

## Требования

- [uv](https://docs.astral.sh/uv/) версии 0.5 и выше
- Python 3.12 (uv скачает его сам, если он не установлен)

## Установка

```bash
uv sync
```

Команда создаст виртуальное окружение `.venv` и установит зависимости
из `uv.lock`.

## Запуск

```bash
uv run catalog_analysis.py
```

Скрипт выводит итоговый отчёт: средний рейтинг и возраст фильмов, топ-3
по рейтингу, количество фильмов по жанрам и список всех жанров.

Демонстрация работы функций этапов 1–8 собрана в `show_examples()`.
Чтобы её увидеть, раскомментируйте вызов `show_examples()` в блоке запуска
в конце `catalog_analysis.py`.

## Проверка качества кода

```bash
uv run ruff check .
uv run ruff format --check .
```

Настройки линтера лежат в секции `[tool.ruff]` файла `pyproject.toml`.

## Этапы

| Этап | Тема | Функции |
|---|---|---|
| 1 | Переменные, числа, `math` | `average_rating`, `catalog_age_stats`, `duration_in_hours` |
| 2 | Условия и `match` | `rating_tier`, `decade_label` |
| 3 | Циклы | `print_non_comedy_titles`, `print_first_masterpiece`, `count_long_movies` |
| 4 | Строки | `normalize_title`, `make_slug`, `format_report_line` |
| 5 | Списки | `titles_sorted_by_rating`, `top_n_by_rating` |
| 6 | Словари | `count_by_genre`, `actor_filmography`, `above_average_ratings` |
| 7 | Множества | `all_genres`, `common_actors`, `genres_only_in_one` |
| 8 | Итераторы и генераторы | `iter_high_rated` |
| 9 | Итоговый отчёт | `build_report` |
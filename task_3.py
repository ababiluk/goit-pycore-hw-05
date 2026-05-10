import sys
import os

def parse_log_line(line: str) -> dict:
    # Розбиваємо рядок на 4 частини: дата, час, рівень, повідомлення
    parts = line.split(' ', 3)
    if len(parts) < 4:
        return {}
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2].upper(),
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> list:
    logs = []
    # Перевіряємо, чи файл взагалі існує (вимога завдання)
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не знайдено.")
        return []
    
    # Відкриваємо файл і читаємо кожен рядок
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parsed_line = parse_log_line(line)
            if parsed_line:
                logs.append(parsed_line)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    # Простий фільтр: беремо тільки ті записи, де рівень збігається
    return [log for log in logs if log['level'] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['level']
        # Рахуємо: якщо рівня ще немає в словнику, ставимо 0 і додаємо 1
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: dict):
    # Виводимо таблицю. <17 та <10 — це просто відступи для рівності стовпчиків
    print(f"{'Рівень логування':<17} | {'Кількість':<10}")
    print("-" * 18 + "|" + "-" * 11)
    for level, count in counts.items():
        print(f"{level:<17} | {count:<10}")

def main():
    # Перевіряємо, чи ввів користувач шлях до файлу в терміналі
    if len(sys.argv) < 2:
        print("Потрібно вказати шлях до файлу: python task_3.py logfile.log")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    
    if not logs:
        return

    # Рахуємо статистику і показуємо таблицю
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Якщо користувач дописав рівень (наприклад, info), показуємо деталі
    if len(sys.argv) > 2:
        level_to_filter = sys.argv[2]
        filtered = filter_logs_by_level(logs, level_to_filter)
        print(f"\nДеталі логів для рівня '{level_to_filter.upper()}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()
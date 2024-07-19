import sys
from collections import Counter
from typing import List, Dict


def parse_log_line(line: str) -> Dict:
    date, time, level, message=line.split(" ", 3)
    dict_log = {'date':date, 'time': time, 'level': level, 'message':message}
    return dict_log
    

def load_logs(file_path: str) -> List:
    logs = []
    try:    
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                logs.append(parse_log_line(line.strip()))           

    except FileNotFoundError:
        print(f'File {file_path} not found.')
    except Exception as e:
        print(f'An error occurred while reading the file: {e}')
    return logs



def filter_logs_by_level(logs: list, level: str) -> List:
    return [log for log in logs if log['level'] == level]


def count_logs_by_level(logs: list) -> Dict:
    levels = [log['level'] for log in logs]
    return Counter(levels)
    

def display_log_counts(counts: dict)-> None:
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")



def main():
    if len(sys.argv) < 2:
        print('Error: Specify the directory path. Example input: python3 task_3/task_3.py /path/to/your/logfile [log_level]')
        
    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)

    if not logs:
        return

    counts = count_logs_by_level(logs)
    print(counts)
    display_log_counts(counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level.upper())
        if filtered_logs:
            print(f"\nDetails of the logs for the level '{log_level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"No entries found for '{log_level.upper()}' level.")



if __name__ == "__main__":
    main()
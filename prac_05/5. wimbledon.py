"""
Wimbledon
Estimate: 40 minutes
Actual:   45 minutes
"""


def load_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split(',')
            data.append(parts)
    return data


def count_champions(data):
    champion_counts = {}
    for row in data:
        champion = row[2]
        champion_counts[champion] = champion_counts.get(champion, 0) + 1
    return champion_counts


def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(countries)


def display_results(champion_counts, countries):
    print("Wimbledon Champions: ")
    for champion, count in champion_counts.items():
        print(f"{champion} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(', '.join(countries))


def main():
    data = load_data("wimbledon.csv")
    champion_counts = count_champions(data)
    countries = get_countries(data)
    display_results(champion_counts, countries)


if __name__ == "__main__":
    main()
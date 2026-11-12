# 08-03 Standard library tour
import itertools
import math
import random
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta

# Example 1: math
print(math.sqrt(2), math.pi)
print(math.isclose(0.1 + 0.2, 0.3))
print(math.log10(1000), math.exp(0))
print(math.dist((0, 0), (3, 4)))

# Example 2: random - always seed it when you need repeatable results
rng = random.Random(42)
print(rng.randint(1, 6), rng.randint(1, 6), rng.randint(1, 6))
print(rng.choice(["rock", "paper", "scissors"]))
cards = ["A", "K", "Q", "J"]
rng.shuffle(cards)
print(cards)
print(rng.sample(range(100), 3))

# Example 3: datetime - dates and times as objects
release = date(2026, 3, 14)
print(release, release.year, release.strftime("%A %d %B %Y"))
print(date.fromisoformat("2026-11-11").weekday())
print(release + timedelta(days=30))
print((date(2026, 12, 25) - date(2026, 11, 11)).days)
moment = datetime(2026, 11, 11, 9, 30)
print(moment.isoformat(), moment.hour)
print(datetime.strptime("11/11/2026 14:05", "%d/%m/%Y %H:%M"))

# Example 4: Counter - the counting pattern in one line
words = "the cat and the hat and the bat".split()
counts = Counter(words)
print(counts["the"], counts["dog"])
print(counts.most_common(2))

# Example 5: defaultdict - grouping without "if key not in"
people = [("Ada", "London"), ("Alan", "Leeds"), ("Grace", "London")]
by_city = defaultdict(list)
for name, city in people:
    by_city[city].append(name)
print(dict(by_city))

# Example 6: itertools
print(list(itertools.combinations(["a", "b", "c"], 2)))
print(list(itertools.permutations([1, 2, 3], 2))[:4])
print(list(itertools.product(["S", "M"], ["red", "blue"])))
print(list(itertools.chain([1, 2], [3], [4, 5])))
print(list(itertools.accumulate([1, 2, 3, 4])))

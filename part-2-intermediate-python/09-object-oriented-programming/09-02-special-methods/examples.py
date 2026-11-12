# 09-02 Special methods


# Example 1: without special methods, printing an object is unhelpful
class PlainPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


print(repr(PlainPoint(1, 2)).startswith("<__main__.PlainPoint object at 0x"))
print(PlainPoint(1, 2) == PlainPoint(1, 2))


# Example 2: __repr__ and __str__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
print(repr(point))
print(str(point))
print(point)
print([point, Point(3, 4)])
print(f"The point is {point}")

# Example 3: __eq__ makes == compare values
print(Point(1, 2) == Point(1, 2), Point(1, 2) == Point(2, 1))
print(Point(1, 2) == "not a point")

# Example 4: __add__ makes + work
print(Point(1, 2) + Point(10, 20))


# Example 5: __len__ makes len() work
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = list(songs)

    def __len__(self):
        return len(self.songs)

    def __repr__(self):
        return f"Playlist({self.name!r}, {len(self)} songs)"


road_trip = Playlist("Road trip", ["Song A", "Song B", "Song C"])
print(len(road_trip))
print(road_trip)
print(bool(Playlist("Empty", [])))


# Example 6: __lt__ makes objects sortable
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student({self.name!r}, {self.grade})"

    def __lt__(self, other):
        return self.grade < other.grade


students = [Student("Ada", 91), Student("Alan", 78), Student("Grace", 85)]
print(sorted(students))
print(max(students))

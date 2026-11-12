# 11-03 Style and readability
# A messy script and the same logic rewritten, producing identical results.


# Example 1: the "before" version - it works, but is hard to read and change
def f(d):
    r = {}
    for x in d:
        if x[1] != None and x[1] >= 0 and x[1] <= 100:
            if x[0].strip().lower() in r:
                r[x[0].strip().lower()].append(x[1])
            else:
                r[x[0].strip().lower()] = [x[1]]
    o = {}
    for k in r:
        a = sum(r[k]) / len(r[k])
        if a >= 70:
            g = "pass"
        else:
            g = "fail"
        o[k] = (round(a, 1), g)
    return o


raw_scores = [("Ada ", 91), ("alan", 64), ("ADA", 85), ("Grace", None), ("alan", 120), ("Grace", 72)]
print(f(raw_scores))

# Example 2: the "after" version - named constants and small functions
PASS_MARK = 70
MIN_SCORE = 0
MAX_SCORE = 100


def normalise_name(name: str) -> str:
    """Return the name stripped and lower-cased, so variants match."""
    return name.strip().lower()


def is_valid_score(score) -> bool:
    """Return True if score is present and within the allowed range."""
    return score is not None and MIN_SCORE <= score <= MAX_SCORE


def group_scores(records):
    """Group valid scores by normalised student name."""
    scores_by_student = {}
    for name, score in records:
        if is_valid_score(score):
            scores_by_student.setdefault(normalise_name(name), []).append(score)
    return scores_by_student


def summarise_student(scores):
    """Return (average rounded to 1 place, "pass" or "fail")."""
    average = sum(scores) / len(scores)
    result = "pass" if average >= PASS_MARK else "fail"
    return round(average, 1), result


def class_report(records):
    """Return a summary for each student with at least one valid score."""
    return {
        student: summarise_student(scores)
        for student, scores in group_scores(records).items()
    }


print(class_report(raw_scores))
print(class_report(raw_scores) == f(raw_scores))

# Example 3: each small piece can now be checked on its own
print(normalise_name("  ADA "), is_valid_score(120), summarise_student([60, 90]))

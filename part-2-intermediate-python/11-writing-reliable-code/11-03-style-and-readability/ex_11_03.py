"""Exercises for 11-03 Style and readability.

Each docstring contains a messy version that works. Write a clean version
with the same behaviour: good names, named constants, small helpers.
"""


def shipping_cost(weight_kg, express=False):
    """Return the shipping cost of a parcel.

    Messy version:
        def s(w, e=False):
            if w <= 0:
                raise ValueError("bad")
            if w <= 2:
                c = 4.5
            elif w <= 10:
                c = 4.5 + (w - 2) * 1.25
            else:
                c = 4.5 + 8 * 1.25 + (w - 10) * 0.8
            if e:
                c = c * 1.5
            return round(c, 2)

    Example: shipping_cost(5) returns 8.25
    """
    raise NotImplementedError


def order_summary(lines):
    """`lines` is a list of (item, quantity, unit_price) tuples.

    Messy version:
        def o(l):
            t = 0
            n = 0
            m = None
            mp = 0
            for x in l:
                t = t + x[1] * x[2]
                n = n + x[1]
                if x[2] > mp:
                    mp = x[2]
                    m = x[0]
            return {"total": round(t, 2), "items": n, "most_expensive": m}

    Example: order_summary([("pen", 2, 1.5), ("pad", 1, 4.0)])
    returns {"total": 7.0, "items": 3, "most_expensive": "pad"}
    """
    raise NotImplementedError


def format_receipt(lines):
    """Return receipt text for a list of (item, quantity, unit_price) tuples.

    Messy version:
        def r(l):
            s = ""
            for x in l:
                s = s + x[0].ljust(10) + str(x[1]).rjust(3) + " x " + ("%.2f" % x[2]).rjust(6) + "\\n"
            s = s + "TOTAL".ljust(10) + ("%.2f" % sum([x[1] * x[2] for x in l])).rjust(12) + "\\n"
            return s

    Example: format_receipt([("pen", 2, 1.5)]) returns
    "pen         2 x   1.50\\nTOTAL             3.00\\n"
    """
    raise NotImplementedError

"""Solutions for 11-03 Style and readability."""

BASE_COST = 4.50
BASE_WEIGHT_KG = 2
MID_WEIGHT_LIMIT_KG = 10
MID_RATE_PER_KG = 1.25
HEAVY_RATE_PER_KG = 0.80
EXPRESS_MULTIPLIER = 1.5

NAME_WIDTH = 10
QUANTITY_WIDTH = 3
PRICE_WIDTH = 6
TOTAL_WIDTH = 12


def shipping_cost(weight_kg, express=False):
    """Return the shipping cost of a parcel."""
    if weight_kg <= 0:
        raise ValueError(f"weight must be positive, got {weight_kg}")
    cost = BASE_COST
    # Each band only charges for the weight that falls inside it.
    mid_band_weight = min(weight_kg, MID_WEIGHT_LIMIT_KG) - BASE_WEIGHT_KG
    if mid_band_weight > 0:
        cost += mid_band_weight * MID_RATE_PER_KG
    heavy_band_weight = weight_kg - MID_WEIGHT_LIMIT_KG
    if heavy_band_weight > 0:
        cost += heavy_band_weight * HEAVY_RATE_PER_KG
    if express:
        cost *= EXPRESS_MULTIPLIER
    return round(cost, 2)


def line_total(line):
    """Return quantity times unit price for one order line."""
    _, quantity, unit_price = line
    return quantity * unit_price


def order_summary(lines):
    """Summarise order lines: total price, item count, most expensive item."""
    most_expensive = None
    highest_price = 0
    for item, _, unit_price in lines:
        if unit_price > highest_price:
            highest_price = unit_price
            most_expensive = item
    return {
        "total": round(sum(line_total(line) for line in lines), 2),
        "items": sum(quantity for _, quantity, _ in lines),
        "most_expensive": most_expensive,
    }


def format_receipt(lines):
    """Return receipt text, one line per item plus a total line."""
    receipt_lines = [
        f"{item:<{NAME_WIDTH}}{quantity:>{QUANTITY_WIDTH}} x {unit_price:>{PRICE_WIDTH}.2f}"
        for item, quantity, unit_price in lines
    ]
    grand_total = sum(line_total(line) for line in lines)
    receipt_lines.append(f"{'TOTAL':<{NAME_WIDTH}}{grand_total:>{TOTAL_WIDTH}.2f}")
    return "\n".join(receipt_lines) + "\n"

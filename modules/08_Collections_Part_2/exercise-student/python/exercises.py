"""
Exercises generated from Java repository.
"""

def animalGroupName(animalName: str) -> str:
    """
    * Given the name of an animal, return the name of a group of that animal
    * (e.g. "Elephant" -> "Herd", "Rhino" - "Crash").
    *
    * The animal name should be case insensitive so "elephant", "Elephant", and
    * "ELEPHANT" should all return "herd".
    *
    * If the name of the animal is not found, null, or empty, return "unknown".
    *
    * Rhino -> Crash
    * Giraffe -> Tower
    * Elephant -> Herd
    * Lion -> Pride
    * Crow -> Murder
    * Pigeon -> Kit
    * Flamingo -> Pat
    * Deer -> Herd
    * Dog -> Pack
    * Crocodile -> Float
    *
    * animalGroupName("giraffe") → "Tower"
    * animalGroupName("") -> "unknown"
    * animalGroupName("walrus") -> "unknown"
    * animalGroupName("Rhino") -> "Crash"
    * animalGroupName("rhino") -> "Crash"
    * animalGroupName("elephants") -> "unknown"
    *
"""
    pass


def isItOnSale(itemNumber: str) -> float:
    """
    * Given an String item number (a.k.a. SKU), return the discount percentage if the item is on sale.
    * If the item is not on sale, return 0.00.
    *
    * If the item number is empty or null, return 0.00.
    *
    * "KITCHEN4001" -> 0.20
    * "GARAGE1070" -> 0.15
    * "LIVINGROOM"	-> 0.10
    * "KITCHEN6073" -> 0.40
    * "BEDROOM3434" -> 0.60
    * "BATH0073" -> 0.15
    *
    * The item number should be case insensitive so "kitchen4001", "Kitchen4001", and "KITCHEN4001"
    * should all return 0.20.
    *
    * isItOnSale("kitchen4001") → 0.20
    * isItOnSale("") → 0.00
    * isItOnSale("GARAGE1070") → 0.15
    * isItOnSale("dungeon9999") → 0.00
    *
"""
    pass



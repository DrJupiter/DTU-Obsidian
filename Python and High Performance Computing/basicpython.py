from typing import List, Tuple
def listsum(array: List[float | int]) -> float | int:
    return sum(array)

def deduplicate(array: List) -> List:
    return list(set(array))

def deduplicate(array):
    return list(set(array))

def sorttuples(array):
    array = array.copy()
    array.sort(key = lambda x: x[-1])
    return array

def squarecubes(array):
    return list(map(lambda x: x**2, array)), list(map(lambda x: x**3, array))


if __name__ == "__main__":
    pass
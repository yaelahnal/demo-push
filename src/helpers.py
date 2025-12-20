# Helper utilities for small experiments

def clamp(value, lower=0, upper=1): return max(lower, min(value, upper))

def as_list(obj): return obj if isinstance(obj, list) else [obj]

def is_empty(seq): return not seq

def chunk(items, size):

        yield items[i:i+size]

def safe_get(mapping, key, default=None):

    return mapping.get(key, default)

def ensure_int(value): return int(value)

def ensure_int(value): return int(value)

def normalize(value): return value / 100.0

def as_list(obj): return obj if isinstance(obj, list) else [obj]

def is_empty(seq): return not seq

def chunk(items, size):

    for i in range(0, len(items), size):

    for i in range(0, len(items), size):

    return mapping.get(key, default)

def ensure_int(value): return int(value)

[auto-update]


[auto-update]


[auto] small helper update
[auto] small helper update
A playground for Git push practices.
Experimenting with repository updates.


def first_element(seq): return seq[0]


def get_last_element(seq): return seq[-1]


def negate(number): return -number


def count_occurrences(items, item_to_count): return items.count(item_to_count)


def stringify(value): return str(value)


def reverse_string(s): return s[::-1]


def get_first_or_default(sequence, default=None): return sequence[0] if sequence else default


def sum_list_elements(numbers): return sum(numbers)


def is_even(number): return number % 2 == 0


def divide_safe(numerator, denominator, default=0): return numerator / denominator if denominator != 0 else default


def get_value_at_index(sequence, index, default=None): return sequence[index] if index < len(sequence) else default


def get_middle_element(seq): return seq[len(seq) // 2]


def get_random_element(seq): return seq[random.randint(0, len(seq) - 1)]


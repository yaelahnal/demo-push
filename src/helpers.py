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


import random
def get_random_element(seq): return seq[random.randint(0, len(seq) - 1)]


def find_max_in_list(numbers): return max(numbers)


def unique_elements(items): return list(set(items))


def is_odd(number): return number % 2 != 0


def get_max_by_key(sequence, key_func): return max(sequence, key=key_func)


def calculate_average(numbers): return sum(numbers) / len(numbers) if numbers else 0


def find_min_in_list(numbers): return min(numbers)


def capitalize_first_letter(s): return s.capitalize()


def remove_duplicates_and_sort(items): return sorted(list(set(items)))


def get_keys_from_dict(d): return list(d.keys())


def get_list_length(lst): return len(lst)


def get_file_extension(filename): return filename.split('.')[-1]


def get_nested_value(data, keys, default=None): return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys, data)


from functools import reduce
def join_list_elements(items, separator=''): return separator.join(map(str, items))


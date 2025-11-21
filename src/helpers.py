# Helper utilities for small experiments

def clamp(value, lower=0, upper=1): return max(lower, min(value, upper))

def as_list(obj): return obj if isinstance(obj, list) else [obj]

def is_empty(seq): return not seq

def chunk(items, size):


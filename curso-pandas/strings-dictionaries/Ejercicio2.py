def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    return [enum for enum, x in enumerate(doc_list) if keyword.lower() in [y.rstrip('.,').lower() for y in x.split()]]
    pass

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
print(word_search(doc_list, 'Casinoville'))
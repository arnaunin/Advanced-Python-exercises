# Text Analysis with Memoization

This project demonstrates the use of Python's `functools.lru_cache` for memoization to optimize the calculation of word frequency in text analysis. It includes preprocessing steps to clean the text and exclude common words.

## Features

1. **Word Frequency Calculation**:
   - The `calculate_word_frequency` function computes the frequency of words in a given text.
   - Preprocessing steps include:
     - Converting text to lowercase.
     - Removing punctuation and unwanted characters.
     - Excluding common words (e.g., "el", "la", "de", etc.).

2. **Memoization**:
   - The function is decorated with `functools.lru_cache` to cache results for previously processed texts, improving performance for repeated calls with the same input.

3. **Performance Comparison**:
   - The script compares the execution time of the function with and without memoization.

4. **Example Texts**:
   - Two sample texts are analyzed to demonstrate the functionality:
     - A passage from *Don Quixote*.
     - A short example text with repeated words.

## How It Works

- The `calculate_word_frequency` function processes the text, removes common words, and calculates the frequency of the remaining words.
- The `functools.lru_cache` decorator caches the results of previous calculations, so if the function is called again with the same text, the cached result is returned instead of recalculating.
- The script measures and prints the execution time for both memoized and non-memoized calls.

### Example Output
For the provided texts, the output might look like this:
```
Word frequency for text_1 without memoization: {'lugar': 1, 'mancha': 1, 'cuyo': 1, ...}
Word frequency for text_2 without memoization: {'otro': 1, 'ejemplo': 2, 'análisis': 1, ...}
Word frequency for text_1 with memoization: {'lugar': 1, 'mancha': 1, 'cuyo': 1, ...}
Word frequency for text_2 with memoization: {'otro': 1, 'ejemplo': 2, 'análisis': 1, ...}
Time without memoization: 0.001234
Time with memoization: 0.000001
```

## Contributing
Contributions are welcome! Please follow these steps:
1. **Fork the Repository**
2. **Create a Feature Branch (`git checkout -b feature-branch`)**
3. **Commit Your Changes (`git commit -m 'Add some feature'`)**
4. **Push to the Branch (`git push origin feature-branch`)**
5. **Open a Pull Request**

'''
Authorship Identification Example.

This file begins by breaking down the authorship identification task into
smaller subtasks, and then provides a simple implementation of each subtask.
Each subtask is implemented as a function, and the main function combines
the results of the subtasks to produce a final authorship prediction.

The main function is `identify_author`, which takes a text as input and returns
the predicted author. The subtasks are implemented as helper functions that
extract features from the text, compare the features to known authors, and
make a prediction based on the comparisons.

The features used in this example are as follows:
- Average word length
- Average sentence length
- Vocabulary richness (type-token ratio)
- Frequency of common function words (e.g., "the", "and", "is")
- Frequency of punctuation marks (e.g., ".", ",", "!", "?")
- Frequency of specific n-grams (e.g., "in the", "of the")

The code is structured as follows:
- `extract_features(text)`: Extracts features from the input text.
- `distance(features1, features2)`: Computes the distance between two sets of features.
- `identify_author(text, dataset)`: Identifies the author of the input text
    based on a dataset of known authors and their features.
- `load_dataset()`: Loads a sample dataset of authors and their features.
- `average_word_length(text)`: Computes the average word length in the text.
- `average_sentence_length(text)`: Computes the average sentence length in the text.
- `vocabulary_richness(text)`: Computes the vocabulary richness (type-token ratio).
- `function_word_frequency(text)`: Computes the frequency of common function words.
- `punctuation_frequency(text)`: Computes the frequency of punctuation marks.
- `ngram_frequency(text, n=2)`: Computes the frequency of specific n-grams.

- `main()`: Example usage of the `identify_author` function with a sample dataset.
'''

def average_word_length(text):
    words = text.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

def average_sentence_length(text):
    sentences = text.split('.')
    sentences = [s for s in sentences if s.strip()]
    if not sentences:
        return 0
    return sum(len(s.split()) for s in sentences) / len(sentences)

def vocabulary_richness(text):
    words = text.split()
    if not words:
        return 0
    unique_words = set(words)
    return len(unique_words) / len(words)

def function_word_frequency(text):
    function_words = ['the', 'and', 'is', 'in', 'to', 'of', 'a', 'that', 'it', 'for']
    words = text.lower().split()
    total_words = len(words)
    if total_words == 0:
        return {word: 0 for word in function_words}
    freq = {word: words.count(word) / total_words for word in function_words}
    return freq

def punctuation_frequency(text):
    punctuation_marks = ['.', ',', '!', '?', ';', ':']
    total_chars = len(text)
    if total_chars == 0:
        return {mark: 0 for mark in punctuation_marks}
    freq = {mark: text.count(mark) / total_chars for mark in punctuation_marks}
    return freq 

def ngram_frequency(text, n=2):
    words = text.split()
    ngrams = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    total_ngrams = len(ngrams)
    if total_ngrams == 0:
        return {}
    freq = {}
    for ngram in ngrams:
        freq[ngram] = freq.get(ngram, 0) + 1
    for ngram in freq:
        freq[ngram] /= total_ngrams
    return freq

def extract_features(text):
    features = {}
    features['avg_word_length'] = average_word_length(text)
    features['avg_sentence_length'] = average_sentence_length(text)
    features['vocab_richness'] = vocabulary_richness(text)
    features.update(function_word_frequency(text))
    features.update(punctuation_frequency(text))
    ngram_freqs = ngram_frequency(text, n=2)
    for ngram, freq in ngram_freqs.items():
        features[f'ngram_{ngram}'] = freq
    return features

def distance(features1, features2):
    dist = 0
    for key in features1:
        if key in features2:
            dist += (features1[key] - features2[key]) ** 2
        else:
            dist += features1[key] ** 2
    for key in features2:
        if key not in features1:
            dist += features2[key] ** 2
    return dist ** 0.5

def identify_author(text, dataset):
    text_features = extract_features(text)
    min_dist = float('inf')
    predicted_author = None
    for author, features in dataset.items():
        dist = distance(text_features, features)
        if dist < min_dist:
            min_dist = dist
            predicted_author = author
    return predicted_author

def load_dataset():
    '''
    The dataset is a directory with files named after authors. Each file simply contains
    text written by the author.
    '''
    path = 'data/authors/'
    import os
    dataset = {}
    for filename in os.listdir(path):
        if filename.endswith('.txt'):
            author = filename[:-4]
            with open(os.path.join(path, filename), 'r', encoding='utf-8') as f:
                text = f.read()
                features = extract_features(text)
                dataset[author] = features
    return dataset

def main():
    dataset = load_dataset()
    sample_text = "This is a sample text to identify the author. It contains several sentences."
    author = identify_author(sample_text, dataset)
    print(f"The predicted author is: {author}")

if __name__ == "__main__":
    main()

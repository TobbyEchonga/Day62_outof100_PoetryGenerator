import markovify

# Load the corpus
with open("corpus.txt") as f:
    text = f.read()

# Build the Markov chain model
text_model = markovify.Text(text)

# Generate and print a poem
for _ in range(5):  # Generate 5 lines of poetry
    poem = text_model.make_sentence()
    print(poem)

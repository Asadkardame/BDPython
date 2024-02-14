# Define the map function
def mapper(input_line):
    # Split the input line into words
    words = input_line.strip().split()
    
    # Emit key-value pairs for each word
    for word in words:
        yield (word, 1)

# Define the reduce function
def reducer(word, counts):
    # Sum up the counts for each word
    total_count = sum(counts)
    
    # Emit the word and its total count
    yield (word, total_count)

# Read input data from the file
input_file = r"C:\Users\asadk\Documents\BDPython\Python\All Chapters\sample.txt"

with open(input_file, "r") as file:
    # Map step: Apply the mapper function to each input line
    mapped_data = [pair for line in file for pair in mapper(line)]

# Shuffle and Sort step: Group key-value pairs by key
grouped_data = {}
for word, count in mapped_data:
    if word not in grouped_data:
        grouped_data[word] = []
    grouped_data[word].append(count)

# Reduce step: Apply the reducer function to each group of key-value pairs
reduced_data = [pair for word, counts in grouped_data.items() for pair in reducer(word, counts)]

# Output the result
print(reduced_data)

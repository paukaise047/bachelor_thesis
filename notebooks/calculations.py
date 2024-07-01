import dat

# Initialize a Model instance with the provided GloVe model and words file
model = dat.Model("divergent-association-task/glove.840B.300d.txt", "divergent-association-task/words.txt")

def compute_dat_scores(words_content, num_iterations, output_file):
    iteration_ranges = [(i * 7, (i + 1) * 7) for i in range(num_iterations)]
    total_dat_score = 0

    with open(output_file, 'w') as f:
        for i, (start, end) in enumerate(iteration_ranges, start=1):
            words_subset = words_content[start:end]
            dat_score = model.dat(words_subset)
            if dat_score is not None:
                total_dat_score += dat_score
                f.write(f"{dat_score}\n")
            else:
                print(f"Warning: DAT score is None for words subset {i}")

    print("Total DAT score for all iterations:", total_dat_score)


# Read the content of the words file into a variable
with open('words_script.txt', 'r') as file:
    words_content = file.read().split(', ')
# Specify the number of iterations
num_iterations = 1

# Specify the output file
output_file = 'score_script.txt'

# Compute DAT scores for the specified number of iterations and save them to the output file
compute_dat_scores(words_content, num_iterations, output_file)

import random
import time

# Define the file name
file_name = "giveawaynames.txt"
# Create dictionaries to store names and their corresponding entries
story_shares = {}
going_entries = {}
insta_comments = {}
# Open the file and read each line
with open(file_name, 'r') as file:
	current_category = None
	for line in file:
		line = line.strip()
		if line == "Giveaway story shares":
			current_category = "story"
		elif line == "FB said going entries":
			current_category = "going"
		elif line == "insta comments":
			current_category = "comments"
		elif current_category == "story":
			story_shares[line] = story_shares.get(line, 0) + 3
		elif current_category == "going":
			going_entries[line] = going_entries.get(line, 0) + 2
		elif current_category == "comments":
			# Check if the line is not empty
			if line:
				# Split the line into name and tags
				parts = line.split()
				name = parts[0]
				tags = parts[1:]
				num_tags = len(tags)
				insta_comments[name] = insta_comments.get(name, 0) + 1 + num_tags
# Combine all entries into a single dictionary
all_entries = {}
for name in set(story_shares.keys()) | set(going_entries.keys()) | set(insta_comments.keys()):
	all_entries[name] = story_shares.get(name, 0) + going_entries.get(name, 0) + insta_comments.get(name, 0)
# Randomly select 5 winners
winners = random.sample(sorted(all_entries.items()), 5)
# Print the winners with a fake loading progress bar
print("Loading winners...")
for i, winner in enumerate(winners, 1):
	print(f"Winner {i}: {winner[0]}")
	time.sleep(0.5)  # Simulate a delay
	print("█" * (i * 10 // 5) + " " * (10 - i * 10 // 5), end="\r")
print("\nCongratulations to the winners!")

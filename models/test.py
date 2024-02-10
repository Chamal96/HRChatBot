
# # Read the contents of the file
# with open('../data/hrchat.txt', 'r') as file:
#     lines = file.readlines()
#
# # Reverse the order of lines where the employee speaks with the chatbot
# for i in range(0, len(lines), 2):
#     lines[i], lines[i+1] = lines[i+1], lines[i]
#
# # Write the modified lines back to the file
# with open('../data/flipped_file.txt', 'w') as file:
#     file.writelines(lines)



# Read the contents of the file
with open('../other/hrchat.txt', 'r') as file:
    lines = file.readlines()

# Remove the words "Chatbot" and "Employee" from each line
for i in range(len(lines)):
    lines[i] = lines[i].replace('Chatbot:', '').replace('Employee:', '')

# Combine the lines with a tab space between them
combined_lines = []
for i in range(0, len(lines), 2):
    combined_lines.append(lines[i].strip() + '\t' + lines[i+1].strip())

# Write the combined lines back to the file
with open('../data/chat/combined_file.txt', 'w') as file:
    file.write('\n'.join(combined_lines))


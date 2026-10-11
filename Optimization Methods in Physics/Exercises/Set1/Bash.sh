#!/bin/bash
##################################################
# Task A
root_directory="/Users/user/Optimization"

times_list=""

# Iterate over all python files in the root directory
for file in "$root_directory"/*.py; do
    # Extract the file name and remove the file extension
    file_name=$(basename "$file")
    file_name="${file_name%.*}"
    
    # Create a directory with the same name as the python file
    directory_name="$root_directory/$file_name"
    mkdir -p "$directory_name"
    
    # Move the python file into the associated directory
    mv "$file" "$directory_name"
    
    # Run the python file and measure the elapsed time
    start_time=$(date +%s.%N)
    python3 "$directory_name/$file_name.py"
    end_time=$(date +%s.%N)
    
    # Calculate the elapsed time
    elapsed_time=$(echo "$end_time - $start_time" | bc)
    
    # Save the elapsed time into a file named "time+index" inside the directory
    time_file="$directory_name/time${file_name#file}.txt"
    echo "$elapsed_time" > "$time_file"
    
    # Add the elapsed time to the times list
    times_list+="$(basename "$time_file")\n"
done

# Save the times list in the root directory
echo -e "$times_list" > "$root_directory/times_list.txt"
##################################################
# Task B: 
sentence_file="$root_directory/sentence.txt"

for directory in "$root_directory"/*/; do
    echo "Directory: $(basename "$directory")" >> "$sentence_file"
    
    for file in "$directory"/*; do
        echo "File: $(basename "$file")" >> "$sentence_file"
        cat "$file" >> "$sentence_file"
        echo >> "$sentence_file"
    done
    
    echo >> "$sentence_file"
done
##################################################
# Task C:
for i in {1..10}; do
    echo "Loop iteration: $i"
done
##################################################
# Task D:
new_directory="$root_directory/new_directory"
mkdir -p "$new_directory"

new_file="$new_directory/new_file.txt"
touch "$new_file"
##################################################
# Task E: 
input_file="$root_directory/input.txt"
output_file="$root_directory/output.txt"

while IFS= read -r line; do
    echo "$line" >> "$output_file"
done < "$input_file"
##################################################
# Task F: 
echo "Running a simple program..."
python3 -c "print('Hello, World!')"
##################################################
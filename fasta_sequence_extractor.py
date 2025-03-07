def extract_fasta_from_file(fasta_file, description, output_file, single_file, line_length):
    # Open the FASTA file and read the content
    with open(fasta_file, 'r') as f:
        lines = f.readlines()

    # Initialize variables
    sequence = None

    # Loop through the lines to find the requested description
    for i in range(len(lines)):
        if lines[i].startswith(f">{description}"):
            sequence = ""
            # Collect the sequence lines for the requested description
            for j in range(i + 1, len(lines)):
                if lines[j].startswith(">"):  # Next header found
                    break
                sequence += lines[j].strip()
            break

    # Check if sequence was found and write to output
    if sequence:
        if single_file:
            # Write to the single output file (append mode)
            with open(output_file, 'a') as out_f:
                out_f.write(f">{description}\n")
                # Split the sequence into user-specified chunks
                for i in range(0, len(sequence), line_length):
                    out_f.write(f"{sequence[i:i+line_length]}\n")
            print(f"Sequence for {description} has been appended to {output_file}")
        else:
            # Write to separate file
            output_filename = f"{description}.fasta"
            with open(output_filename, 'w') as out_f:
                out_f.write(f">{description}\n")
                # Split the sequence into user-specified chunks
                for i in range(0, len(sequence), line_length):
                    out_f.write(f"{sequence[i:i+line_length]}\n")
            print(f"Sequence for {description} has been written to {output_filename}")
    else:
        print(f"Error: Sequence with description '{description}' not found in the file. Please try again or type 'done' to exit.")


# Main logic to prompt user for input and extract the fasta
if __name__ == "__main__":
    # Print instructions for the user
    print("""
Welcome to the FASTA Sequence Extractor!

    Instructions:
    1. You will be prompted to enter the path of the FASTA file.
    2. Then, you can choose to either store all sequences in a single file or separate files.
    3. You can also specify the number of characters per line when saving the sequences.
    4. You can enter any description (e.g., the header line starting with '>') to extract the sequence.
    5. If you enter 'done', the script will stop.
    

    Please follow the prompts to extract the desired sequences.
    """)

    # Ask the user for the location of the FASTA file
    fasta_file = input("Please enter the path to your FASTA file (e.g., /home/user/sequences.fasta): ").strip()
    
    # Check if the FASTA file exists
    try:
        with open(fasta_file, 'r') as file:
            pass  # Successfully opened the file, no action needed
    except FileNotFoundError:
        print(f"Error: The file at '{fasta_file}' was not found. Please check the path and try again.")
        exit(1)

    # Ask for the output preference: single file or separate files
    file_choice = input("Do you want all sequences in a single file (enter 'single') or separate files (enter 'separate')? ").strip().lower()

    # Validate the user's input choice
    if file_choice not in ['single', 'separate']:
        print("Invalid choice. Please enter 'single' or 'separate'.")
        exit(1)

    # If single file, ask for the output file name
    if file_choice == 'single':
        output_file = input("Enter the name for the output file (e.g., all_sequences.fasta): ").strip()
    else:
        output_file = None  # Separate files don't need an output file name

    # Set the flag for output mode (single or separate)
    single_file = True if file_choice == 'single' else False

    # Ask the user for custom sequence length (line length)
    try:
        line_length = int(input("Enter the sequence line length (e.g., 60 characters per line): ").strip())
        if line_length <= 0:
            print("Error: Line length must be a positive integer. Exiting.")
            exit(1)
    except ValueError:
        print("Error: Please enter a valid integer for line length.")
        exit(1)

    # Loop to ask the user for description identifiers
    while True:
        description = input("Enter the sequence description (e.g., '>geneX', '>proteinY') or type 'done' to exit: ").strip()
        
        if description.lower() == 'done':
            print("\nYou have chosen to exit. Thank you for using the script!")
            break
        elif description.startswith(">"):
            extract_fasta_from_file(fasta_file, description[1:], output_file, single_file, line_length)
        else:
            print("Invalid input. Please enter a valid description starting with '>' or type 'done' to exit.")


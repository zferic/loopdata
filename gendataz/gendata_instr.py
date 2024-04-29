import csv
import os


def extract_number_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            line = file.readline()  # Read the first (and only) line
            parts = line.split()  # Split the line into parts
            if len(parts) == 2 and parts[0] == "Result":  # Validate format
                return int(parts[1])  # Convert the second part to integer and return
            else:
                raise ValueError("File content is not in the expected format.")
    except FileNotFoundError:
        print("The specified file was not found.")
    except ValueError as e:
        print(e)


# Function to extract hex instructions from a file
def extract_hex_instructions(file_path):
    hex_instructions = []  # List to store the hex instructions
    main_list = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split('\t')
            try:
                stuff = parts[1]
                parts_hex = stuff.split()
                main_list.append(parts_hex)
            except:
                main_list.append(parts)
                continue
    return main_list


# Function to extract hex instructions from a file
def extract_hex_instrumentation(file_path):
    hex_instructions = []  # List to store the hex instructions
    main_list = []
    with open(file_path, 'r') as file:
        for line in file:

            
            parts = line.split('\t')
            try:
                stuff = parts[1]
                parts_hex = stuff.split()
                main_list.append(parts_hex)
            except:
                main_list.append(parts)
                continue
    return main_list

# Function to extract hex instructions from a file
def extract_hex_instrumentation(file_path, start_address='0x401cb5', end_address='401ce6'):
    hex_instructions = []  # List to store the hex instructions
    capture = False  # Flag to start capturing Bytes

    with open(file_path, 'r') as file:
        for line in file:
            # Check if the line starts with "Address:" to determine the current address
            if line.startswith("Address:"):
                address = line.split(',')[0].split()[1]  # Extract the address
                
                # Check if the current address is the starting address
                if address == start_address:
                    capture = True  # Start capturing Bytes lines
                # Check if the current address is the ending address
                elif address == end_address:
                    capture = False  # Stop capturing Bytes lines after processing this block
                
            # Capture the Bytes lines
            elif "Bytes:" in line and capture:
                # Extracting the hex bytes and appending them to the list
                bytes_part = line.strip().split('Bytes: ')[1]
                hex_instructions.extend(bytes_part.split())

    return hex_instructions

# Function to extract data between '_init' and newline
def extract_between_init_and_newline(list_of_lists):
    start_extraction = False
    extracted_items = []
    for sublist in list_of_lists:
        if start_extraction:
            if sublist == ['\n']:
                break
            extracted_items.append(sublist)
        if any('<loopgiggidy>' in item for item in sublist):
            start_extraction = True
    temp = ''
    for x in extracted_items:
        temp += ''.join(x)
    return temp





# CSV file to write the data
csv_file_path1 = '/media/zman/extrahd/gem5-22.0.0.1/gendataz/extracted_data_objdump.csv'
csv_file_path2 = '/media/zman/extrahd/gem5-22.0.0.1/gendataz/extracted_data_instr.csv'

benchmarkDirs = [
                '/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoopAdd/',
             ]

#benchmarkDirs = ['/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoopSub/',
#             ]

# Open the CSV file for writing
with open(csv_file_path1, mode='w', newline='') as csv_file1:
    with open(csv_file_path2, mode='w', newline='') as csv_file2:
        
        writer1 = csv.writer(csv_file1)
        writer2 = csv.writer(csv_file2)
        # Write the header row
        #swriter.writerow(['Extracted Items', 'Step*Iters'])
        #print(files)

        for benchmarkDir in benchmarkDirs:
            print(benchmarkDir)
            
            dirsAssembly = benchmarkDir + 'diffversions/'
            dirsResults = benchmarkDir + 'results/'
            dirsInstrument = benchmarkDir + 'instrument/'

            files = os.listdir(dirsAssembly)

            for file in files:
                if '.txt' in file:

                    print(file)
                    file_instrument = file.replace("bench","instrument")
                    print(file_instrument)
                    print("muahssad")
                    
                    file_path = dirsAssembly + file
                    file_path2 = dirsResults + file
                    file_path3 = dirsInstrument + file_instrument

                    hex_instrumented = extract_hex_instrumentation(file_path3)
                    print(len(hex_instrumented))
                    
                    print(file_path)
                    hex_instructions = extract_hex_instructions(file_path)
                    extracted_items = extract_between_init_and_newline(hex_instructions)
                    
                    
                    result = extract_number_from_file(file_path2)

                    hex_instrumented_all = ''.join(hex_instrumented)

                    writer1.writerow([extracted_items, result])
                    writer2.writerow([hex_instrumented_all, result])
            
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



# Function to extract data between '_init' and newline
def extract_between_init_and_newline(list_of_lists):
    start_extraction = False
    extracted_items = []
    for sublist in list_of_lists:
        if start_extraction:
            if sublist == ['\n']:
                break
            extracted_items.append(sublist)
        if any('<looptarget>' in item for item in sublist):
            start_extraction = True
    temp = ''
    for x in extracted_items:
        temp += ''.join(x)
    return temp


# CSV file to write the data
csv_file_path = '/media/zman/extrahd/gematria/data/gendataz/extracted_data.csv'

benchmarkDirs = [
'/media/zman/extrahd/gematria/data/loops/ForLoopNonLinear/',    
#'/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoopFibonacci/',
#'/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoopPrime/',
#'/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoopExpGrow/',
#'/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoopAddDouble/',
#'/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoopAdd/',
#'/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoopSub/',
##'/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoopMul/',
#'/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoopAddCond/',
#'/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoopAddCond2/',
             ]

#benchmarkDirs = ['/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoopSub/',
#             ]

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Write the header row
    #swriter.writerow(['Extracted Items', 'Step*Iters'])
    #print(files)

    for benchmarkDir in benchmarkDirs:
        print(benchmarkDir)
        
        dirsAssembly = benchmarkDir + 'diffversions/'
        dirsResults = benchmarkDir + 'results/'

        files = os.listdir(dirsAssembly)

        for file in files:
            if '.txt' in file:
                file_path = dirsAssembly + file
                file_path2 = dirsResults + file
                print(file_path)
                hex_instructions = extract_hex_instructions(file_path)
                extracted_items = extract_between_init_and_newline(hex_instructions)
                
                result = extract_number_from_file(file_path2)
                
                # Extract step and iters values from the filename or another source
                # Assuming filename format: "bench_step_iters.X86.txt"
                #parts = file.split('_')
                #step = int(parts[1])
                #iters = int(parts[2].split('.')[0])
                
                # Write the filename, extracted items,
                writer.writerow([extracted_items, result])
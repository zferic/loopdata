import subprocess

def modify_and_compile(filename, new_step, new_iters):

    prepath = '/media/zman/extrahd/gem5-22.0.0.1/microbench/ForLoop/'
    diffversions_folder = 'diffversions/'  # Define the folder name
    # Ensure the folder exists or create it
    subprocess.run(['mkdir', '-p', prepath + diffversions_folder], check=True)
    
    # Step 1: Read the original C program
    with open(prepath + filename, 'r') as file:
        content = file.read()
    
    # Step 2: Replace STEP and ITERS values
    new_content = content.replace('#define STEP   5', f'#define STEP   {new_step}', 1)
    new_content = new_content.replace('#define ITERS   32', f'#define ITERS   {new_iters}', 1)
    
    # Step 3: Save the modified version
    modified_filename = f"{filename.rsplit('.', 1)[0]}_{new_step}_{new_iters}.c"
    with open(prepath + diffversions_folder + modified_filename, 'w') as file:
        file.write(new_content)
    
    # Step 4: Compile the modified program with the provided command
    output_executable = prepath + diffversions_folder + f"bench_{new_step}_{new_iters}.X86"
    compile_command = ['gcc', '-O0', '-I../', f'-DMAGIC', prepath + diffversions_folder + modified_filename, '--static', '--std=c99', '-lm', '-o', output_executable]
    subprocess.run(compile_command, check=True)
    
    # Step 5: Use objdump to disassemble the compiled program and save the output to a text file
    disassembly_file = output_executable + ".txt"
    objdump_command = ['objdump', '-d', output_executable]
    with open(disassembly_file, 'w') as file:
        subprocess.run(objdump_command, stdout=file, check=True)
    
    print(f"Compiled and disassembled {modified_filename} into {diffversions_folder} with STEP={new_step} and ITERS={new_iters}")

# Define the parameter combinations dynamically as needed
parameter_combinations = []
for Step in range(5,100,5):
    for iters in range(32,1000,64):
        parameter_combinations.append((Step, iters))

# Loop through each combination, modifying, compiling, and disassembling the C program
for step, iters in parameter_combinations:
    modify_and_compile('bench.c', step, iters)

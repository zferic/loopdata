import subprocess
import os
import shutil

def modify_and_compile(filename, new_step, new_iters, paths):

    prepath = paths
    diffversions_folder = 'diffversions/'  # Define the folder name
    results_folder = 'results/'
    results_instrument = 'instrument/'

    # Ensure the folder exists or create it
    subprocess.run(['mkdir', '-p', prepath + diffversions_folder], check=True)
    subprocess.run(['mkdir', '-p', prepath + results_folder], check=True)
    subprocess.run(['mkdir', '-p', prepath + results_instrument], check=True)
    
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
    
    # Step 4: Compile the modified program
    output_executable = prepath + diffversions_folder + f"bench_{new_step}_{new_iters}.X86"
    compile_command = ['gcc', '-O0', '-I../', f'-DMAGIC', prepath + diffversions_folder + modified_filename, '--static', '--std=c99', '-lm', '-o', output_executable]
    try:
        subprocess.run(compile_command, check=True, cwd=prepath, timeout=60)
    except subprocess.TimeoutExpired:
        print(f"Timeout expired during compilation of {modified_filename}")

    # Step 5: Disassemble the compiled program
    disassembly_file = output_executable + ".txt"
    objdump_command = ['objdump', '-d', output_executable]
    try:
        with open(disassembly_file, 'w') as file:
            subprocess.run(objdump_command, stdout=file, check=True, timeout=30)
    except subprocess.TimeoutExpired:
        print(f"Timeout expired during disassembly of {output_executable}")
    
    # Step 6: Run the compiled program and capture its output
        
    output_executable = prepath + diffversions_folder + f"bench_{new_step}_{new_iters}.X86"
    
    run_command = [output_executable]
    output_executable2 = prepath + results_folder + f"bench_{new_step}_{new_iters}.X86"
    run_output_file = output_executable2 + ".txt"
    
    try:
        with open(run_output_file, 'w') as file:
            subprocess.run(run_command, stdout=file, check=True, timeout=120)
        print(f"Compiled, disassembled, and ran {modified_filename}. Output saved to {run_output_file}")
    except subprocess.TimeoutExpired:
        print(f"Timeout expired during execution of {output_executable}")

    
    print(f"Compiled, disassembled, and ran {modified_filename}. Output saved to {run_output_file}")


    # Step 7: Run the instrumentation program and capture its output
    pin_exe = '/home/zman/pin-3.27-98718-gbeaa5d51e-gcc-linux/pin'
    pin_tool = '/home/zman/pin-3.27-98718-gbeaa5d51e-gcc-linux/source/tools/MyPinTool_Count/obj-intel64/MyPinTool.so'
    program_executable = prepath + diffversions_folder + f"bench_{new_step}_{new_iters}.X86"
    output_file= prepath + results_instrument + f"instrument_{new_step}_{new_iters}.X86.txt"
    '''
    run_command = [
     pin_exe,
    "-t", pin_tool,
    "-o", output_file,
    "--", program_executable]
    '''
    subprocess.run(run_command, check=True)
    
    #print(f"Compiled, disassembled, and ran {modified_filename}. Output saved to {run_output_file}")

# Define the parameter combinations dynamically as needed
parameter_combinations = []
for Step in range(5,10,5):
    for iters in range(1,32,1):
        parameter_combinations.append((Step, iters))

# Loop through each combination, modifying, compiling, and disassembling the C program

import os

print(os.listdir('/media/zman/extrahd/gematria/data/loops/'))

path = '/media/zman/extrahd/gematria/data/loops/'

dirsToRun = ['ForLoopAdd3', 'ForLoopReverse', 'ForLoopPrime', 'ForLoopExp', 'ForLoopAdd4', 'ForLoopFibonacci', 'ForLoopMul', 
             'ForLoopExpGrow', 'ForLoopAddCond', 'ForLoopModulo', 'ForLoopAddCond2', 'ForLoopNonLinear', 'ForLoopSub', 'ForLoopDecrement', 
             'ForLoopAdd', 'ForLoopAddDouble', 'ForLoopAdd2', 'ForLoopAdd1', 'ForLoopIncrement', 'ForLoopExp3']

diffversions_folder = 'diffversions/'  # Define the folder name
results_folder = 'results/'


for dirRun in dirsToRun:
    dirRun = path + dirRun + '/'
    print(dirRun)
    # Check if the folder exists and remove it if it does
    if os.path.exists(dirRun + diffversions_folder):
        shutil.rmtree(dirRun + diffversions_folder)
    if os.path.exists(dirRun + results_folder):
        shutil.rmtree(dirRun + results_folder)


    for step, iters in parameter_combinations:
        modify_and_compile('bench.c', step, iters,dirRun)

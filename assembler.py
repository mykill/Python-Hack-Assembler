import commandParser, time
from time import clock
from symbolTable import symbol_Table # Import the symbol table that holds RAM/ROM addresses for Variable/Label Symbols
from commandParser import destination, compute ,jump

var_sym_start = 16 # Set a counter defining where memory allocation starts for Variable (RAM) symbols
asm_file_name = input('Enter the name of the .asm file to process: ') #assembly filename (assumes .asm file is in same directory as script)
asm = open(asm_file_name + '.asm') # open .asm file
lines = asm.readlines() # get lines from .asm file

commands = commandParser.commandType(lines,symbol_Table) # turn lines into command objects using parser2's parse function

hack_file = open(asm_file_name+'1' + '.hack', 'w') # Open the .hack file for writing
start = time.clock()
#commandParser.compute(commands)
#commandParser.destination(commands)
#commandParser.jump(commands)
commandParser.Acommands(commands,symbol_Table, var_sym_start)
commandParser.writeCommands(commands, hack_file,symbol_Table, var_sym_start) # Send list of commands to parser to write to .hack file
elapsed = (time.clock() - start)
print(elapsed, 'seconds')
hack_file.close() # Close the .hack file.
print('Done')

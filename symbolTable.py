# Create the Symbol Table as a dict symbolTable. This dict stores RAM/ROM addresses for Variable/Label symbols.
# The symbolTable has some initialized values
symbol_Table = {
	'SP' : 0,
	'LCL' : 1,
	'ARG' : 2,
	'THIS' : 3,
	'THAT' : 4,
	'R0' : 0,
	'R1' : 1,
	'R2' : 2,
	'R3' : 3,
	'R4' : 4,
	'R5' : 5,
	'R6' : 6,
	'R7' : 7,
	'R8' : 8,
	'R9' : 9,
	'R10' : 10,
	'R11' : 11,
	'R12' : 12,
	'R13' : 13,
	'R14' : 14,
	'R15' : 15,
	'SCREEN' : 16384,
	'KBD' : 24576
	}
def addEntry(symbol, addr):
        symbol_Table.update(symbol, addr)

def contains(symbol)
        return symbol in symbol_Table
    
def getAddress(symbol)
        if  symbol in symbol_Table:
            return symbol_Table.get(symbol)
        else:
            return -1
            

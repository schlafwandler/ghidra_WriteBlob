# Write the content of a file to the current cursor location
#@author schlafwandler
#@category Memory
#@keybinding 
#@menupath 
#@toolbar 

def main():
    input_filename = str(askFile("Select file to insert", "Load"))
    data = open(input_filename,"rb").read()
    currentProgram.getMemory().setBytes(currentAddress,data)

main()

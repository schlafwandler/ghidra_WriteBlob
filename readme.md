# WriteBlob
## A Ghidra script to paste a raw blob into an analysed binary
This is a really simple script to paste the raw content of a file into a binary analysed with ghidra.

The original use case for this script was to easily replace an obfuscated function in a binary with a de-obfuscated version dumped from memory. 

## Installation
Copy `WriteBlob.py` to your Ghidra scripts directory (the Script Manager has a button to show you all directories where Ghidra is looking for scripts).

If the script is not shown in the Script Manager, try the 'Refresh Script List` button.

## Usage
  * Place the cursor in ghidra's listing window at the position where you want to insert the file.
  If there are currently defined code bytes at the location, clear them (`c` in ghidra).
  * Run the `WriteBlob.py` script and select the file you want to paste.

The script will write the file's content as a blob to the selected position, overwriting the current bytes.

To save the modifications back to the binary, check out my [SavePatch](https://github.com/schlafwandler/ghidra_SavePatch) script.

## Bugs/Limitations
This script simply pastes the content of the file as a binary blob.
It does not handle any other task needed to make the process run smoothly, like redefining the function in ghidra or update relocation entries.


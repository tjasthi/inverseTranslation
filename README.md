The program inverseTranslation opens 2 files, whose filenames iare specified by the user as a command-line argument. The first file is a FASTA file from a filename supplied by a user as a command-line argument and a codon usage table.
Reads of the FASTA sequence and implements the related codon sequence using the apropriate codon table.

When outputting the sequence:
End with a stop codon, but not contain any in-frame premature stop codons,
Be a length multiple of three (i.e. no "half" codons),
Translate to the corresponding input sequence from protein.fasta, according to the genetic code specified in codonUsage.txt,
Be in valid FASTA format, using the same name as the input sequence.

The output sequence should be optimized:
The more frequent codons from the codon usage table should be used, where possible,
Codon repetition should be avoided, where possible (especially close repetitions),
Secondary structure should be avoided, where possible.

Your program should exit gracefully (that is, report an error and stop execution, e.g. by raising a Python exception) if any of the following error conditions are met:
The user did not specify a filename argument on the command line
The file named by the user does not exist, or is not readable
The file named by the user is not in FASTA format
The file named by the user contains sequences that are not DNA

Where possible, you should recover from other "typical" errors with minimal disruption to the user of your script.

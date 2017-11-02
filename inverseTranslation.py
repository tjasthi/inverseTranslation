import sys

#Reading the file
try:
	sequence_file = sys.argv[1]
	codon_file = sys.argv[2]
except:
	raise Exception("Did not specify a correct filename argument on the command line")
try:
	sequence_reader = open(sequence_file, 'r')
	codon_reader = open(codon_file, 'r')
	#write_me = sys.stdout
	write_me = open('output.txt', 'w')
except:
	raise Exception("Files do not exist, or are not readable")

class Amino:
    """An amino acid object with relevent fields.

    Attributes:
    	name: name of the codon
        codons: dictionary of fraction keys with codon as the value
    """
    def __init__(self, amino_acid_name):
        """Return an Amino object with the specified fields."""
        self.name = amino_acid_name
        self.codons = {}

    def add_codon(self, codon, fraction):
    	"""Adds a codon and fraction to the dictionary"""
    	while(self.codons.has_key(fraction)):
    		fraction = float(fraction) + 0.01
    	self.codons[float(fraction)] = codon

    def get_codon(self, placing):
    	"""Gets the codon with the specified placing.
    	If placing is out of bounds, then return the worst codon."""
    	fractions = self.codons.keys()
    	fractions.sort()
    	fractions.reverse()
    	if (placing - 1 > len(fractions) - 1):
    		return self.codons.get(fractions[len(fractions) - 1])
    	else:
    		return self.codons.get(fractions[placing - 1])

F = Amino("F")
L = Amino("L")
I = Amino("I")
M = Amino("M")
V = Amino("V")
S = Amino("S")
P = Amino("P")
T = Amino("T")
A = Amino("A")
Y = Amino("Y")
Stop = Amino("*")
H = Amino("H")
Q = Amino("Q")
N = Amino("N")
K = Amino("K")
D = Amino("D")
E = Amino("E")
C = Amino("C")
W = Amino("W")
R = Amino("R")
S = Amino("S")
E = Amino("E")
G = Amino("G")
amino_dict = {'F':F, 'L':L, 'I':I, 'M':M, 'V':V, 'S':S, 'P':P, 'T':T, 'A':A, 'Y':Y, '*':Stop, \
	'H':H, 'Q':Q, 'N':N, 'K':K, 'D':D, 'E':E, 'C':C, 'W':W, 'R':R, 'S':S, 'E':E, 'G':G}

def main():
	readCodonFile()
	#Write the first line of the input
	line = sequence_reader.readline()
	if (line[0] == '>'):
		write_me.write('>codons' + '\n')
	else:
		raise Exception("Not in FASTA format, needs a label")

	#Looping through all lines in the file
	last = ""
	for line in sequence_reader:
		if (line[0] == '>'):
			codon = convert(amino_dict.get('*').get_codon(1))
			write_me.write(codon + '\n' + '>codons' + '\n')
			last = ""
		elif (amino_dict.has_key(line[0])):
			if (len(line) < 50) or (len(line) > 81):
				raise Exception("Not in FASTA format, should have 50-80 characters per line")
			else:
				for i in range(len(line)):
					if (line[i] != '\n'):
						try:
							if (last != line[i]):
								codon = amino_dict.get(line[i]).get_codon(1)
								last = line[i]
							else:
								codon = amino_dict.get(line[i]).get_codon(2)
								last = ""
						except:
							raise Exception("Unidentified amino acid")
					else:
						break
					codon = convert(codon)
					write_me.write(codon)
		else:
			raise Exception("Not in FASTA format")

	codon = convert(amino_dict.get('*').get_codon(1))
	write_me.write(codon + '\n')

	#Exit and save
	sequence_reader.close()
	write_me.close()

"""
Converts a codon into lowercase DNA bases
"""
def convert(codon):
	try:
		letter_dict = {'A':'a', 'U':'t', 'C':'c', 'G':'g'}
		char1 = letter_dict.get(codon[0])
		char2 = letter_dict.get(codon[1])
		char3 = letter_dict.get(codon[2])
		return char1 + char2 + char3
	except:
		raise Exception("Incorrectly formatted codon file")

"""
Reads the codon file, storing relevent codons and frequencies in the global dictionary, codons.
"""
def readCodonFile():
	for line in codon_reader:
		if (len(line) < 102):
			continue
		try:
			codon1 = line[0:3]
			acid1 = line[4]
			fraction1 = float(line[6:10])

			codon2 = line[26:29]
			acid2 = line[30]
			fraction2 = float(line[32:36])

			codon3 = line[52:55]
			acid3 = line[56]
			fraction3 = float(line[58:62])

			codon4 = line[78:81]
			acid4 = line[82]
			fraction4 = float(line[84:88])

			amino_dict.get(acid1).add_codon(codon1, fraction1)
			amino_dict.get(acid2).add_codon(codon2, fraction2)
			amino_dict.get(acid3).add_codon(codon3, fraction3)
			amino_dict.get(acid4).add_codon(codon4, fraction4)
		except:
			raise Exception("Incorrectly formatted codon file")
	codon_reader.close()

if __name__== "__main__":
	main()
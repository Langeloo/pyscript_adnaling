#DOM Elements
from multiprocessing.connection import wait


fasta_1 = Element("fasta_1")
fasta_2 = Element("fasta_2")

#button fasta action
def fasta_action(*args, **kws):
    print("Action fasta event")


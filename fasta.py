#DOM Elements
fasta_1 = Element("fasta_1")
fasta_2 = Element("fasta_2")

#button fasta action
global_aling_fasta = Element("global_aling_fasta")
local_aling_fasta = Element("local_aling_fasta")

def input_event(evt):
    print("input_event upload fasta")
    document = fasta_1.element.files[0]
    print(document)
    #document = evt.target.files[0]
    #with open(document, "r") as f:
        #txtread = f.read()
        #print(document)
    print(fasta_1.element.value)
    
fasta_1.element.onchange = input_event
fasta_2.element.onchange = input_event

def gl_aling_fasta(*args, **kws):
    print("gl_aling_fasta")
    
def lc_aling_fasta(*args, **kws):
    print("lc_aling_fasta")
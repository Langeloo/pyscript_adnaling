# alineamiento de secuencias
#from pyodide import create_proxy
#console.log("Iniciando alineamiento de secuencias")

#seq1 = Element("first-sequence").element.value.replace(" ", "").upper()
#seq2 = Element("second-sequence").element.value.replace(" ", "").upper()
sequence1 = Element("first-sequence")
sequence2 = Element("second-sequence")
global_button = Element('global_aling')
local_button = Element('local_aling')
slidermin1 = Element('lower')
slidermax1 = Element('upper')
slidermin2 = Element('lower2')
slidermax2 = Element('upper2')
alert_seq1 = Element('alert_seq1')
alert2_seq1 = Element('alert2_seq1')
alert_seq2 = Element('alert_seq2')
alert2_seq2 = Element('alert2_seq2')

#lower = Element("lower").element.value
#upper = Element("upper").element.value
#lower2 = Element("lower2").element.value
#upper2 = Element("upper2").element.value


result_p = Element("result")


result = []
#sec_zip = zip(seq1, seq2)
#print(seq1)
#print(seq2)
#print(list(sec_zip))



class bcolors:
    OK = "\033[92m"  # GREEN
    WARNING = "\033[93m"  # YELLOW
    FAIL = "\033[91m"  # RED
    RESET = "\033[0m"  # RESET COLOR


caracters_error = (
    bcolors.OK
    + "Error: La secuencia solo debe tener caracteres ACTG"
    + bcolors.RESET
)


def verify_caracters():
    for i, j in sec_zip:
        if i not in "ACTG" or j not in "ACTG":
            alert_seq1.write(caracters_error)
            return False
        else:
            return True
        
def ver_text(sequence1, sequence2):
    #sequence1
    flagca_seq1 = False
    flagco_seq1 = False
    #sequence2
    flagca_seq2 = False
    flagco_seq2 = False
    
    for i in sequence1:
        if i not in "ACTG":
            flagca_seq1 = True
            
    for i in sequence2:
        if i not in "ACTG":
            flagca_seq2 = True
            
    if len(sequence1) < 40 or len(sequence1) > 60:
        flagco_seq1 = True
    
    if len(sequence2) < 40 or len(sequence2) > 60:
        flagco_seq2 = True
        
    if flagca_seq1:
        alert_seq1.write('Error: La secuencia solo debe tener caracteres ACTG')
    else:
        alert_seq1.write('OK')
        
    if flagco_seq1:
        alert2_seq1.write('Error: La secuencia debe tener entre 40 y 60 caracteres')
    else:
        alert2_seq1.write('OK')
        
    if flagca_seq2:
        alert_seq2.write('Error: La secuencia solo debe tener caracteres ACTG')
    else:
        alert_seq2.write('OK')
        
    if flagco_seq2:
        #print(alert2_seq2.element.value)
        pass
    else:
        #print(alert2_seq2.element.value)
        pass
        
    #alerts
    if flagca_seq1 or flagco_seq1 or flagca_seq2 or flagco_seq2:
        local_button.element.disabled = True
        global_button.element.disabled = True
        slidermin1.element.disabled = True
        slidermin2.element.disabled = True
        slidermax1.element.disabled = True
        slidermax2.element.disabled = True
    else:
        local_button.element.disabled = False
        global_button.element.disabled = False
        slidermin1.element.disabled = False
        slidermin2.element.disabled = False
        slidermax1.element.disabled = False
        slidermax2.element.disabled = False
        slidermin1.element.max = len(sequence1)
        slidermax1.element.max = len(sequence1)
        slidermax1.element.value = len(sequence1)
        slidermin2.element.max = len(sequence2)
        slidermax2.element.max = len(sequence2)
        slidermax2.element.value = len(sequence2)
    


def global_aling():
        equal = True if len(sequence1.element.value) == len(sequence2.element.value) else False
        
        
        if equal:
            print(bcolors.OK + "Las secuencias son iguales" + bcolors.RESET)
            # return True



def local_aling(seq1_init, seq2_init, seq1_final, seq2_final):
    if verify_caracters():
        seq1_local = seq1[seq1_init - 1 : seq1_final - 1]
        seq2_local = seq2[seq2_init - 1 : seq2_final - 1]
        seq_zip = zip(seq1_local, seq2_local)
        equal = True if seq1_final - seq1_init == seq2_final - seq2_init else False
        return aling(seq_zip, equal)
    else:
        return caracters_error


def aling(seq_zip, equal):
    for i, j in seq_zip:
        result.append(True) if i == j else result.append(False)
    if equal:
        similarity = (
            "La similitud es: "
            + ((result.count("1") / len(result)) * 100).round(2)
            + "%"
        )
    else:
        similarity = "No es posible hallar el porcentaje de similitud, cadenas de diferente longitud"

    return {"seqs": sec_zip, "result": result, "similarity": similarity}

#input_event()
def input_event(evt=None):
    ver_text(sequence1.element.value.replace(" ", "").upper(), sequence2.element.value.replace(" ", "").upper())
    
sequence1.element.onkeypress = input_event
sequence2.element.onkeypress = input_event



#button global aling
def gl_aling(*args, **kws):
    #local_button.element.disabled = True
    slidermin1.element.max = 90
    slidermax1.element.max = 90
    #print(seq1)
    
    
#button local aling
def lc_aling(*args, **kws):
    #global_button.element.disabled = True
    #print(seq2, upper, lower, upper2, lower2)
    result_p.write('Element write')
    
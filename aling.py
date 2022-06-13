# alineamiento de secuencias
#from pyodide import create_proxy
#console.log("Iniciando alineamiento de secuencias")

seq1 = Element("first-sequence").element.value.replace(" ", "").upper()
seq2 = Element("second-sequence").element.value.replace(" ", "").upper()
sequence1 = Element("first-sequence")
sequence2 = Element("second-sequence")

lower = Element("lower").element.value
upper = Element("upper").element.value
lower2 = Element("lower2").element.value
upper2 = Element("upper2").element.value


result_p = Element("result")


result = []
sec_zip = zip(seq1, seq2)
print(seq1)
print(seq2)
print(list(sec_zip))



class bcolors:
    OK = "\033[92m"  # GREEN
    WARNING = "\033[93m"  # YELLOW
    FAIL = "\033[91m"  # RED
    RESET = "\033[0m"  # RESET COLOR


caracters_error = (
    bcolors.OK
    + "Error: Alguno de los caracteres no es una secuencia de ADN"
    + bcolors.RESET
)


def verify_caracters():
    for i, j in sec_zip:
        if i not in "ACTG" or j not in "ACTG":
            print(caracters_error)
            return False
        else:
            return True


def global_aling():
    if verify_caracters():
        equal = True if len(seq1) == len(seq2) else False
        if equal:
            print(bcolors.OK + "Las secuencias son iguales" + bcolors.RESET)
            # return True
        return aling(sec_zip, equal)
    else:
        return caracters_error


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
    print(sequence1.element.value)
    
sequence1.element.onkeypress = input_event
sequence2.element.onkeypress = input_event


#button global aling
def gl_aling(*args, **kws):
    print(seq1)
    
    
#button local aling
def lc_aling(*args, **kws):
    print(seq2, upper, lower, upper2, lower2)
    result_p.write('Element write')
    
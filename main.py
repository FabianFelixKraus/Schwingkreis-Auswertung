from import_data import get_data
from theorie import get_theo_values
from fit import get_fit
from create_output_file import create_file
from names import get_names

storage = []

for run, name in enumerate(get_names()):

    #print("run",run)
    #Daten holen
    #Format data = [[alle x Werte], [alle dazugehörigen y-Werte], PP-Spannung(=U_max)]
    data = get_data(name)
    #Einhüllende finden

    #Theoretischen Wert bestimmen
    #Format output theo_value = (Dämpfung,Eigenfrequenz,Fall,L) Fall 1 = Schwing; 2 = aper. Grenzfall; 3 = Kriechfall
    delta, omega_0, case, L = get_theo_values(name)
    #print("delta theoretisch ",delta)
    #print("w_0 theoretisch ",omega_0)
    #Check Fall richtig bestimmt also manuell vs automatisch korrekt
    #if case != int(name[0]):
    #    raise Exception("FALSCHER FALL BESTIMMT BEI " + str(name))

    #fit Berechnen
    #Format input: get_fit([x,y,max(y)], name, Will_ich_einen_Plot_?, (delta,omega_0))
    #Format output: fit_values = (Dämpfung, Eigenfrequenz)
    fit_values = get_fit(data, name, False, (delta,omega_0))
    #print(fit_values)

    besseres_R = fit_values[0] * 2 * L
    print("\n")
    #Speichert alle Information eines Schleifendurchlaufs für das auswertungs txt
    storage.append((name,(delta,omega_0),fit_values,round(besseres_R,2)))
    
create_file(storage)
    
#Plot fit vs experiment
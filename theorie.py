def get_theo_values(name):

    #Creates list information [case, Farad, F_factor, Henri, h_factor, Ohm]
    def extract_name(name):

        def convert(name):
            name = name[:-1]
            if name == "m":
                return -3
            elif name == "my":
                return -6
            elif name == "n":
                return -9

        numbers = ["1","2","3","4","5","6","7","8","9","0",".",]
        information = []
        name = name.split("_")
        #append case
        information.append(int(name[0]))
        for part in name:
            temp = str()
            for char in part:
                if char in numbers:
                    temp += char
                else:
                    information.append(float(temp))
                    information.append(None)
                    break
        information = information[:-1]
        temp = str()
        counter = 0
        for part in name:
            for i, char in enumerate(part):
                if not char in numbers:
                    temp = part[i:]
                    if counter == 0:
                        information[2] = convert(temp)
                        counter += 1
                    elif counter == 1:
                        information[4] = convert(temp)
                        counter += 1     
                    break           
        print("INFORMATINO", information)
        return information

    def calc_theo_values(info):

        output = [None,None,None,None]

        from math import sqrt
        pi = 3.14159264
        #information [case, Farad, F_factor, Henri, h_factor, Ohm]
        #R = info[5]                        #Ohm möglichst klein
        R = info[5]
        L = info[3] * 10**(info[4])              #Henri möglichst groß
        C = info[1] * 10**(info[2])              #Farad möglichst groß

        delta = R/(2*L)
        output[0] = round(delta,2)
        omega_0 = 1/sqrt(L*C)    
        output[1] = round(omega_0,2)
        output[3] = L

        def Ist_ein_Schwingfall(delta, w_0):
            if delta < w_0:
                omega = sqrt(w_0**2 - delta**2)
                frequenz = omega / 2 * pi
                T = 1/frequenz
                #print("frequenz: " + str(frequenz) + " Hz")
                #print("Periodendauer: " + str(T) + " s. Umgerechnet: " + str(T*10**3) + " ms. | " + str(T*10**6) + " mikrosek. | " + str(T*10**9) + " ns")
                return True
            elif abs(delta - w_0) < 1:
                return -1
            else:
                return False


        if Ist_ein_Schwingfall(delta, omega_0):
            print("------SCHWINGFALL--------")
            output[2] = 1
        elif not Ist_ein_Schwingfall(delta, omega_0):
            print("|||||||||||Kriechfall|||||||||||")            
            output[2] = 3
        else:
            print("+++++++aperiodischer Grenzfall+++++++")
            output [2] = 2

        return output

    return calc_theo_values(extract_name(name))


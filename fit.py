def get_fit(data, name, I_want_plot, theo_values): 
    import numpy as np
    from matplotlib import pyplot as plt
    from scipy.optimize import curve_fit
    from math import sqrt
    
    def func_schwing(t, delta, w_0, A, phi):
        #delta = 15.754
        return 2* A * np.exp(-delta*t) * np.cos(((w_0**2-delta**2)**0.5) *t + phi)

    def func_aper_grenz(t, delta, A):
        return A * np.exp(-delta * t)
        
    def func_kriechfall(t, delta, w_0, A):
        return A * np.exp(-delta*t) * np.exp(((delta**2-w_0**2)**0.5) *t)     
    
    def einh(t, delta):
        return -np.exp(-delta * t)  
        
    t = data[0]
    U = data[1]
    U_max = data[2]
    delta_theo = theo_values[0]
    w_0_theo = theo_values[1]
    initial_guess = [delta_theo,w_0_theo,U_max]
    case = name[0]

    fit = []

    if case == "1":
        initial_guess = [1575.4,31900, 4, 1]
        constants, cov = curve_fit(func_schwing, t, U, initial_guess)
        delta_fit = round(constants[0],2)
        w_0_fit = round(constants[1],2)
        A_fit = round(constants[2],2)
        phi_fit = round(constants[3],2)
        Error_delta = cov[0][0]**0.5
        Error_w = cov[1][1]**0.5
        Error_A = cov[2][2]**0.5
        Error_phi = cov[3][3]**0.5
        #print("Error_delta",Error_delta)
        #print("Error_w",Error_w)
        #print("Error_A",Error_A)
        #print("Error_phi",Error_phi)
        for element in data[0]:
            fit.append(func_schwing(element,delta_fit, w_0_fit, A_fit, phi_fit))


    elif case == "2":
        constants, cov = curve_fit(func_aper_grenz, t, U, initial_guess[::2])
        delta_fit = round(constants[0],2)
        w_0_fit = delta_fit
        A_fit = round(constants[1],2)
        Error_delta = cov[0][0]**0.5
        Error_A = cov[1][1]**0.5
        #print("Error_delta",Error_delta)
        #print("Error_A",Error_A)
        for element in data[0]:
            fit.append(func_aper_grenz(element, delta_fit ,A_fit))

    elif case == "3":
        constants, cov = curve_fit(func_kriechfall, t, U, initial_guess)
        delta_fit = round(constants[0],2)
        w_0_fit = round(constants[1],2)
        A_fit = round(constants[2],2)
        Error_delta = cov[0][0]**0.5
        Error_w = cov[1][1]**0.5
        Error_A = cov[2][2]**0.5
        #print("Error_delta",Error_delta)
        #print("Error_w",Error_w)
        #print("Error_A",Error_A)
        for element in data[0]:
            fit.append(func_kriechfall(element, delta_fit, w_0_fit, A_fit))
    else:
        print("case",case)
        raise Exception("Fehler bei Dateibennenung")


    if I_want_plot:
        data_tief = [[5e-05, 0.00025, 0.00045, 0.00066, 0.00086, 0.00106, 0.00127, 0.00148, 0.00167, 0.00188, 0.00208, 0.00249, 0.00332], [-5.2, -4.24, -3.36, -2.72, -2.24, -1.76, -1.44, -1.2, -0.96, -0.8, -0.64, -0.4, -0.24]]
        constants = curve_fit(einh, data_tief[0], data_tief[1])
        fit_func = [[],[]]
        for x in data[0]:
            fit_func[0].append(x)
            fit_func[1].append(einh(x,constants[0][0]))
        
        """
        if case == "1":
            plt.errorbar(t, U, yerr=15, fmt='o', markersize=2, capsize=5, label="Messdaten")

        elif case == "2":
            plt.errorbar(x, y, yerr=15, fmt='o', markersize=2, capsize=5, label="Messdaten")

        elif case == "3":
            plt.errorbar(x, y, yerr=15, fmt='o', markersize=2, capsize=5, label="Messdaten")
        """

        plt.plot(t,U, color = "blue", label = "Messung", marker = ".")
        plt.plot(t, fit, color = "yellow", label = "plot")
        #plt.plot(t, theo, color = "red", label = "Theo")
        plt.grid()
        plt.xlabel("t [s]")
        plt.ylabel("U [V]")
        #title = str(str(name[:-4]) + "\n" + "Fit: delta = " + str(delta_fit) +", Omega_0 = " + str(w_0_fit) +"\n Theo: delta = " + str(delta_theo) + ", Omega_0 = " + str(w_0_theo))
        if case == "1":
            title = "Schwingfall"
        elif case == "2":
            title = "aperiodischer Grenzfall"
        elif case == "3":
            title = "Kriechfall"
        
        plt.title(title)
        plt.show()

    return (delta_fit, w_0_fit)

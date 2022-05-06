def create_peak_fit(data_old):
    import numpy as np
    from matplotlib import pyplot as plt
    from scipy.optimize import curve_fit

    #fit_function
    def einh(t, delta):
        return -np.exp(delta * t)

    #Finds all maxima
    def find_peaks(data):        
        def is_minimum(ppredecessor, predecessor,me,sucessor, ssucessor):
            if ppredecessor == None or predecessor == None or me == None or sucessor == None or ssucessor == None:
                return False 
            if ppredecessor > predecessor and predecessor >= me and me <= sucessor and sucessor < ssucessor:
                return True
            return False

        output = [[],[]]
        y_values = data[1]
        for i,y in enumerate(y_values):
            if i > 1 and i < len(y_values)-2:
                ppredecessor = y_values[i-2]
                predecessor = y_values[i-1]
                sucessor = y_values[i+1]
                ssucessor = y_values[i+2]
                if is_minimum(ppredecessor, predecessor, y, sucessor, ssucessor):
                    output[0].append(data[0][i])
                    output[1].append(y)
        
        def eliminat_dublicates(data):
            save = []
            for i, y in enumerate(data[1]):
                if i > 0:
                    temp = data[1][i-1]
                    if temp == y and temp not in save:
                        output[0].append(data[0][i])
                        output[1].append(y)
                    else:
                        save.append(temp)
        
        return eliminat_dublicates(output)
            
    #Finds delta by fit
    def create_fit(data):
        constants = curve_fit(einh, data[0], data[1])
        delta = constants[0][0]
        return delta

    #creates a list for plotting the new found function
    def create_data_new(x_values,delta):
        new_data = [[],[]]
        for x in x_values:
            new_data[0].append(x)
            new_data[1].append(einh(x, delta))
        return new_data

    #plots graph with any given data
    def plot(data_old, data_new):
        plt.plot(data_old[0],data_old[1], color = "blue", label = "Messung")
        plt.plot(data_new[0],data_new[1], color = "yellow", label = "Fit")
        plt.show()
        
    #list full of points for fitting: format = [[x],[y]]
    data_for_fitting = find_peaks(data_old)
    print(data_for_fitting)

    print("MINIMUM",min(data_for_fitting))

    plot(data_old,create_data_new(data_for_fitting[0],create_fit(data_for_fitting)))
    

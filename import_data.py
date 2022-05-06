def get_data(name):

    def convert_line(line):
        line = line[1:]
        line = line[:-2]
        line = line.split(",")
        return tuple(float(a) for a in line)

    def calc_seconds(mikro):
        return mikro * 10** -6

    def calc_Volt(milli):
        return milli * 10** -3

    def get_period_factor(line):
        numbers = ["1","2","3","4","5","6","7","8","9","0","."]
        factor = str()
        for char in line.split(",")[-1]:
            if char in numbers:
                factor += char
            #elif factor == ".":
            #   pass
            else:
                break
        return float(factor)

    def verschiebe(x_rechts, save):        
        #return x_rechts - 3800
        return x_rechts-380*save

    data = []
    #C:/Users/Fabian Kraus/Programmieren/schwingkreis/
    with open(name,"r") as file:
        #n = len(file.readlines())
        for i, line in enumerate(file.readlines()):
            if i > 9:
                data.append(convert_line(line))
            elif i == 6:
                save = get_period_factor(line)
    x = []
    y = []
    
    for element in data[len(data)//2:]:
        x.append(calc_seconds(verschiebe(element[0],save)))
        y.append(calc_Volt(element[2])) 

    if abs(min(y)) > max(y):
        U_max = abs(min(y))
    else:
        U_max = max(y)

    return [x,y,U_max]



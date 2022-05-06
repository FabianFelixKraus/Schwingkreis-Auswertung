#save = name,(delta,omega_0),fit_values,round(besseres_R,2)

def create_file(save):

    final_text = "                         theoretisch               experimentell"
    final_text += "\n"
    final_text += "name                        delta    w_0        delta    w_0             besseres R"
    final_text += "\n"
    final_text += "\n"
    for data_row in save:
        final_text += str(str(data_row[0]) + str(";    ") + str(data_row[1][0]) + str(";    ") + str(data_row[1][1]) + str(";    ") + str(data_row[2][0]) + str(";    ") +str(data_row[2][1]) + str(";    ") +str(data_row[3]))
        final_text += "\n"

    final_text += "["
    for data_row in save:
        final_text += str(data_row[2][0]) + str(", ")
    final_text += "]"

    with open("auswertung.txt","w") as file:
        file.write(final_text)


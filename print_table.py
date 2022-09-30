from get_data import * 
from calculation import Calculation


class PrintTable:
    @staticmethod
    def print_table():
        end_list = Calculation.calculate_rating(GetData.data_txt("results_RUN.txt"))
        end_json = GetData.data_json("competitors2.json")
        print('Занятое место | Нагрудный номер | Имя | Фамилия | Результат')
        for i in range(len(end_list)):
            print(str(i + 1) + ' | ' + str(end_list[i][0]) + ' | ' +
                str(end_json[end_list[i][0]]["Name"]) + ' | ' +   
                str(end_json[end_list[i][0]]["Surname"]) + ' | ' + str(end_list[i][1][1]) 
                )

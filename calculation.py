class Calculation:
    '''
        Подаются параметры в виде - 16:22:30,000000, 16:24:08,264286
        Возвращается кортеж (разница в секундах, разница в нужном формате)
    '''
    @staticmethod
    def calculate_date(date1, date2): 
        time1 = date1.rstrip()
        time2 = date2.rstrip()

        h1, h2 = int(time1.split(':')[0]) * 3600, int(time2.split(':')[0]) * 3600 
        m1, m2 = int(time1.split(':')[1]) * 60, int(time2.split(':')[1]) * 60  
        s1 = float(time1.split(':')[2].replace(',', '.')) 
        s2 = float(time2.split(':')[2].replace(',', '.'))

        t1 = h1 + m1 + s1 
        t2 = h2 + m2 + s2
        dt = t2 - t1
        dt_str = str(int(dt // 60)) + ':' + str(round(dt % 60, 2)).replace('.', ',') 

        return (dt, dt_str)

    '''
        Параметр - список строк тхт-файла
        На выходе список кортежей в формате - [(номер, (время в сек, время в красивом формате))]
    '''
    @staticmethod
    def calculate_rating(data_txt):
        list_number_time1_time2 = []
        for i in range(len(data_txt)):
            if i == len(data_txt) - 1:
                break
            list_number_time1_time2.append((data_txt[i], data_txt[i + 1]))  

        for elem in list_number_time1_time2:
            if elem[0].split(' ')[0] != elem[1].split(' ')[0]:
                list_number_time1_time2.remove(elem)

        list_number_dt_dt_str = []
        for elem in list_number_time1_time2:
            list_number_dt_dt_str.append((elem[0].split(' ')[0], 
                                        Calculation.calculate_date(elem[0].split(' ')[2],
                                                            elem[1].split(' ')[2])))

        list_sort = []
        for elem in list_number_dt_dt_str:
            list_sort.append(round(elem[1][0], 2))

        list_sort = sorted(list_sort)

        end_list_sort = []
        for elem1 in list_sort:
            for elem2 in list_number_dt_dt_str:
                if elem1 == round(elem2[1][0], 2):
                    end_list_sort.append(elem2)    
                
        return end_list_sort    

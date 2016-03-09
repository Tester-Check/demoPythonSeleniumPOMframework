import xlrd


class excel_utils():

    def get_data(self,file_name, sheet_index):
        # create an empty list to store rows
        values = []
        # open the specified Excel spreadsheet as workbook
        book = xlrd.open_workbook(file_name)
        # get the first sheet
        sheet = book.sheet_by_index(sheet_index)
        # iterate through the sheet and get data from rows in list
        #for cell_index in range(0, sheet.nrows):
        print(sheet.nrows)
        print(sheet.ncols)
        for j in range(0,sheet.nrows):
            for i in range(0,sheet.ncols):
                if(sheet.cell(j,i).value is not ''):
                    values.append(sheet.cell(j, i).value)
        print(values)
        return values

    def read_cell(self, filepath, sheet_index, row, col):
        book = xlrd.open_workbook(filepath)
        sheet = book.sheet_by_index(sheet_index)
        return sheet.cell(row, col).value



    def spit_list(self, mylist, start_string, end_string):
        #list1 = excel_utils().get_data('/Users/shreyas/Documents/TestCase.xls', 0)
        list1 = mylist
        start = list1.index(start_string)
        end = list1.index(end_string)

        return list1.__getslice__(start, end+1)




#sl= excel_utils().spit_list(excel_utils().get_data('/Users/shreyas/Documents/TestCase.xls', 0), 'name','password')
#print(sl)

#cellValue= excel_utils().read_cell('/Users/shreyas/Documents/TestCase.xls', 0, 6, 1)
#print('this is the cell value '+cellValue)

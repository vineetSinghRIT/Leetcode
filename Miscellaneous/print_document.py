import collections

from itertools import groupby

class PrintDocument:

    @staticmethod
    def merge(d1: list, d2: list) -> list:

        my_list = d1+d2
        # Sort the list by the first element of each set
        sorted_list = sorted(my_list, key=lambda x: next(iter(x)))

        # Group the sets by the first element and sort each group by the minimum of the second element
        grouped_list = []
        for _, group in groupby(sorted_list, key=lambda x: next(iter(x))):
            sorted_group = sorted(group, key=lambda x: next(iter(x)), reverse=True)
            sorted_group = sorted(sorted_group, key=lambda x: next(iter(x)), reverse=False)
            grouped_list.extend(sorted_group)

        return grouped_list

if __name__ == '__main__':
    d1=[{'docA',1},{'docD',5},{'docE',2}]
    d2=[{'docA',4},{'docB',6},{'docD',3}]

    print(PrintDocument.merge(d1,d2))





"""
2) Crie um exemplo de decorador. Utilize uma função com lista de argumentos e
dicionário de chaves como parâmetros.

"""

class Supermarket():
    """
    Represents a supermarket list.
    
    """

    def print_decorator(func):
        """
        Decorator that's prints before and after the supermarket list is being
        written.

        :param func: the function that the operator modifies.
        :type func: function.
        """

        def inner(*args, **kwargs):
            """
            Function that calls the function that will be indirectly
            modified.

            :param func: the function that the operator modifies.
            :type func: function.
            :rtype: function
            """

            print("Supermarket list will be written!\n")
            func(*args, **kwargs)
            print("Supermarket list is ready!\n")
        return inner
    
    @print_decorator
    def make_list(self, list, dic): # Uses a list and a dictionary as parameters
        """
        Function that write the supermarket list.

        :param list: number of each food that have to be bought.
        :type list: list.
        :param dic: food that have to be bought.
        :type dic: dictionary.
        """

        print("Supermarket list is being written!\n")
        self.s_list = list
        self.s_dic = dic
        i = 0
        for food in dic:
            dic[food] = list[i]
            i += 1
        self.to_buy = dic

##### Usage examples #####

# Create the list instance
spm = Supermarket()

# Create the list itself
spmkt_list = [1, 2, 3, 4, 5]
spmkt_dic = {
    'apple': 0,
    'banana': 0,
    'coconut': 0,
    'orange': 0,
    'kiwi': 0
}

# Call to make the supermarket list
# Note that the operator will also be called
spm.make_list(spmkt_list, spmkt_dic)
print(spm.to_buy) # Updated supermarket list
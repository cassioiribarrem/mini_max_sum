class Mini_max_sum():
    def __init__(self, arr):
        self.arr = arr

    def create_new_lists(self):
        complete_list = []
        for i in range(0, len(self.arr)):
            new_list = self.arr.copy()
            del(new_list[i])
            complete_list.append(new_list)
        return complete_list

    def calculate_max(self):
        list = self.create_new_lists()
        max_list = []
        for i in range(0, len(list)):
            max_list.append(sum(list[i]))
        return max_list

    def comparing(self):
        list = self.calculate_max()
        for i in range(0, len(list)):
            max_sum = max(list)
            min_sum = min(list)
        print(f'{min_sum}  {max_sum}')




result = Mini_max_sum([1, 2, 3, 4, 5])
result.comparing()
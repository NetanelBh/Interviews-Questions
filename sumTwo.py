def two_sum(nums, target):
    hashmap = dict()

    for index in range(0, len(nums)):
        current_num = nums[index]
        if hashmap.get(target - current_num):
            return [hashmap.get(target - current_num), index]
        else:
            hashmap[current_num] = index


if __name__ == "__main__":
    print(two_sum([3, 2, 4], 6))

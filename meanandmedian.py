def meanfinder():
    nums = []
    while True:
        user_input = input("Enter numbers. Press 'x' to exit. ").lower()
        if user_input == 'x':
            break
        try:
            user_input = int(user_input)
            nums.append(user_input)
        except:
            print("Invalid input. Please enter numbers only.")
    if len(nums) == 0:
        print("Insufficient data.")
        return
    mean = sum(nums) / len(nums)
    return mean

#print(meanfinder())

def medianfinder():
    nums = []
    while True:
        user_input = input("Enter numbers. Press 'x' to exit. ").lower()
        if user_input == 'x':
            break
        try:
            user_input = int(user_input)
            nums.append(user_input)
        except:
            print("Invalid input. Please enter numbers only.")
    if len(nums) == 0:
        print("Insufficient data.")
        return
    nums.sort()
    if len(nums) % 2 == 1:
        median = nums[int((len(nums) - 1) / 2)]
        return median
    else:
        median = (nums[int(len(nums) / 2)] + nums[int(len(nums) / 2 - 1)]) / 2
        return median

#print(medianfinder())

user_choice = input("Enter 'mean' to find the mean or enter 'median' to find the median. ").lower()
if user_choice == "mean":
    print(meanfinder())
elif user_choice == "median":
    print(medianfinder())
else:
    print("Invalid input.")
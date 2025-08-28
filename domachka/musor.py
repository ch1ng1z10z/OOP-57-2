# def fine_plus(pip, target):
#     n = len(pip)
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 continue  # не используем один и тот же элемент по одному индексу
#             if pip[i] + pip[j] == target:
#                 print(f"{pip[i]}+{pip[j]} = {target}")
#                 return
#     print(f"No pair in {pip} sums to {target}")
#
# nums = [2, 7, 11, 15]
# vvod_chisla = [3, 2, 4]
# irolog = [3, 3]
#
# fine_plus(nums, 9)
# fine_plus(vvod_chisla, 6)
# fine_plus(irolog, 6)
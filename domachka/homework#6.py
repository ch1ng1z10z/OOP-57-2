nums = [2,7,11,15]
vvod_chisla = [3,2,4]
irolog = [3,3]
def fine_plus( pip, target):
    for i in pip:
        for t in pip:
            if target == i + t:
                return print(f"{i}+{t} = {target}")
            else:
                continue
fine_plus(nums, 9)
fine_plus(vvod_chisla, 6)
fine_plus(irolog,6)


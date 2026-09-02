# comparision operator are used to compare the two values and produce the boolean result
# ==
# <=
# >=
# !=
a=20
b=12
print(a>b)
print(a==b)



#  practise coding
nums=[2,5,7,5,8]
target=9
seen={}
for index,num in enumerate(nums):
    complement=target-num
    if complement  in seen:
        print(seen[complement],index)
        break
    else:
        seen[num]=index


# move zeroes to last
nums=[1,2,0,2,0,1,0]
pos=0
for num in range(len(nums)):
    if nums[num]!=0:
        nums[pos],nums[num]=nums[num],nums[pos]
        pos+=1
print(nums)
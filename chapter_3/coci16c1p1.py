# solution 1

# monthly_gb = int(input())
# m = int(input())

# excess = 0

# # i'm being explicit about the variable's 'don't care' status :)
# for _ in range(m):
#     used = int(input())
#     excess = monthly_gb + excess - used

# print(monthly_gb + excess)


# solution 2

# monthly_gb = int(input())
# m = int(input())

# total_gb = monthly_gb * m

# for _ in range(m):
#     used = int(input())
#     total_gb = total_gb - used

# total_gb += monthly_gb
# print(total_gb)


# solution 3

monthly_gb = int(input())
m = int(input())

total_gb = monthly_gb * (m + 1)

for _ in range(m):
    used = int(input())
    total_gb = total_gb - used

print(total_gb)

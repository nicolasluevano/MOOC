# Write your solution here
how_many = int(input("How many students on the course?"))
desired_size = int(input("Desired group size?"))
groups_formed =  -(-how_many // desired_size)
print(f'Number of groups formed: {groups_formed}')
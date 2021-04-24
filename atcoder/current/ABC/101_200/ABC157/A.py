N = input()

def num_of_paper(N):
    if N%2 == 1:
        return int(N/2) + 1
    return int(N/2)

print(num_of_paper(N))
print()
print("# # # - loading bar demo - # # # # # ")
print()
import time

for i in range(0, 41):
    print("|" + ("#"*i).ljust(40, '-') + "|\r", end='')
    time.sleep(0.2)

print()
print("loading complete")

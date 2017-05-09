item1 = {}
item1['first'] = 1
item1['second'] = 2


item2 = {}
item2['first'] = 1
item2['second'] = 2



print("## doing var comparison")

if item1 == item2:      # used to compare values
    print("matched. python (==) comparison is magical")
else:
    print("dead_dove1.jpg")

if item1 in [item2]:      # used to compare identities
    print("matched. python (in) hash match is magical")
else:
    print("dead_dove2.jpg")

if item1 is item2:      # used to compare identities
    print("matched. python (is) hash match is magical")
else:
    print("dead_dove3.jpg")

# # # # # # # # # # # # # # # # # # # # # # # #
class simpleton:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        return false

simp_a = simpleton(1, 2)
simp_b = simpleton(1, 2)


print("## doing class comparison")
if simp_a == simp_b:      # used to compare values
    print("matched. python (==) matches by recursive __eq__()")
else:
    print("dead_dove1.jpg")

if simp_a in [simp_b]:      # used to compare identities
    print("matched. python (in) matches by recursive __eq__()")
else:
    print("dead_dove2.jpg")

if simp_a is simp_b:      # used to compare identities
    print("matched. python (is) matches by object id (same pointed addr)")
else:
    print("dead_dove3.jpg")

# # # # # # # # # ## # # # # # # # #
list_a = [1, 2, 3]
list_b = [2, 1, 2, 3, 4]
if list_a in list_b:
    print("nice")
else:
    print("maximum effort")


# # # # # # # #
print("None checks")

simp_none = None
if not simp_none:
    print("this works 1")
else:
    print("this no work 1")
if simp_none == None:
    print("this works 2")
else:
    print("wtf python")


llist = []
def modifylist(llist=[]):
    llist.append(1)


print(llist)

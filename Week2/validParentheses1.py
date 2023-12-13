from queue import LifoQueue

#This is the solution with stack

correctMatches = {"(": ")", "{": "}", "[": "]"}

def isValid(sequence):
    stack = LifoQueue(maxsize=20)
    for cur in sequence:
        if stack.empty():
            if cur in ")]}":
                return False
            else:
                stack.put(cur)
        else:
            if cur in ")]}":
                lastElem = stack.get()
                if correctMatches[lastElem] != cur:
                    return False
            else:
                stack.put(cur)
    return True




sequence = input()

print(isValid(sequence))



s="()[]{}"
def vp(s):
    stack = []
    for i in range(len(s)):
        if s[i] in ["(","[","{"]:
            stack.append(s[i])
        else:
            if len(stack)==0:
                return False
            else:
                if s[i]=="}" and stack[-1]=="{":
                    stack.pop()
                elif s[i]=="]" and stack[-1]=="[":
                    stack.pop()
                elif s[i]==")" and stack[-1]=="(":
                    stack.pop()

                else:
                    return False
    return True if len(stack)==0 else False
print(vp(s))
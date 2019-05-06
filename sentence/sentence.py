from goto import with_goto

inputstr = "i+i*i#"

lang = {
    'E': ['E+T', 'T'],
    'T': ['T*F', 'F'],
    'F': ['(E)', 'i']
}

table = {
    "(": {"(": "<", "i": "<", "*": "<", "+": "<", ")": "="},
    "i": {"*": ">", "+": ">", ")": ">", "#": ">"},
    "*": {"(": "<", "i": "<", "*": ">", "+": ">", ")": ">", "#": ">"},
    "+": {"(": "<", "i": ">", "*": "<", "+": ">", ")": ">", "#": ">"},
    ")": {"*": ">", "+": ">", ")": ">", "#": ">"},
    "#": {"(": "<", "i": "<", "*": "<", "+": "<"},
}

Vt = ["(", "i", "*", "+", ")", "#"]
Vn = ['E', 'F', 'T']

def FIRSTVT(L, Vt, Vn):
    F = {}

    return F


def LASTVT():
    L = {}

    return L


def creat_TABLE():
    pass


@with_goto
def Analyse(instr, Vt, table):
    S = ["\\"] * 50
    S[1] = "#"
    i = 1
    k = 0
    try:
        label.begin
        R = instr[k]
        k += 1
        if S[i] in Vt:
            j = i
        else:
            j = i - 1
        label.jmp
        if table[S[j]][R] == ">":
            label.aftjmp
            Q = S[j]
            j = j - 1
            if not S[j] in Vt:
                j = j - 1
            if table[S[j]][Q] == "<":
                i = j + 1
                S[i] = 'N'
                if i == 2 and R == "#":
                    return True
                else:
                    goto.jmp
            else:
                goto.aftjmp

        else:
            i = i + 1
            S[i] = R
            goto.begin
        return False
    except:
        return False


print(Analyse(inputstr, Vt, table))

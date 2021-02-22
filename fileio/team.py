f1=open("teams","r")
f2=open("drop","r")
st1=set()
st2=set()

for lines in f1:
    st1.add(lines.rstrip("\n"))

for lines in f2:
    st2.add(lines.rstrip("\n"))

qualifiers=st1-st2
print(qualifiers)




#2

ft=open("teams","r")
fd=open("drop")


def get_team_set(f)
    st=set()
    for lines in f:
        st.add(lines.rstrip("\n"))
    return st
st1=get_team_set(ft)
st2=get_team_set(fd)
qualifiers=st1-st2
print(qualifiers)
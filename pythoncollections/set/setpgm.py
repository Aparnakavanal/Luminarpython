st={}
print(type(st))

st=set()
print(type(st))

st={10,20,20,30,"hello",30,40}
print(st)
st2={100,200}
st.update(st2)
print(st)


lst=[10,20,20,30]
st=set(lst)
print(st)
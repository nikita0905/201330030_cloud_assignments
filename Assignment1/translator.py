file1=open("32_bit.asm")
l=file1.readlines()
st1=""
for i in l:
    #print i
    if i=="int 0x80\n":
        st1=st1+"syscall"+'\n'
    elif i=="mov eax, 4\n":
        st1=st1+"mov rax, 1\n"
    elif i=="mov eax, 1\n":
        st1=st1+"mov rax, 60\n"
    else:
        st1=st1+i
#print st1
st2=st1
st2=st2.split('\n')
#print st2
op=""
for i in st2:
    i=i.split(" ")
    for w in i:
        if w=='eax,':
            w='rax,'
        if w=='ebx,':
            w='rdi,'
        if w=='ecx,':
            w='rsi,'
        if w=='edx,':
            w='rdx,'
        if w=='esp,':
            w='rsp,'
        if w=='eax':
            w='rax'
        if w=='ebx':
            w='rdi'
        if w=='ecx':
            w='rsi'
        if w=='edx':
            w='rdx'
        if w=='esp':
            w='rsp'
        op=op+w+" "
    op=op+'\n'
#print op
f2=open("64_bit.asm","w")
f2.write(op)
f2.close()


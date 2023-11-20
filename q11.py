s_a=float(input('digite seu salario atual'))
s_atual=0.0
d_entre_s=0.0
p_de_a=0.0
if s_a<=280:
    p_de_a=20
elif s_a<=750:
    p_de_a=15
elif s_a<=1500:
    p_de_a=10
else:
    p_de_a=5
d_entre_s=s_a*(p_de_a/100)
s_atual=s_a+d_entre_s*(p_de_a/100)
print('seu salario antes era de',s_a)
print('seu salario foi almentado em',p_de_a)
print('seu salario foi almentado em',d_entre_s)
print('seu salario atual e de',s_atual)
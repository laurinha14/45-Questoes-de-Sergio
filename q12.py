v_da_h=float(input('quanto voce recebe por hora'))
h_t=float(input('digite quantas horas voce trabalhou essse mes'))
s_b=v_da_h*h_t
if s_b <=900:
    desconto_ir=0.0
elif s_b <=1500:
    desconto_ir=5
elif s_b<=2500:
    desconto_ir=10
else:
    desconto_ir=20
IR=s_b*(desconto_ir/100)
INSS=s_b*(10/100)
FGTS=s_b*(11/100)
t_de_d=IR+INSS
s_l=s_b-t_de_d
print('salario bruto',s_b,'IR(5%)',IR,'INSS(10%)',INSS,'FGTS(11%)',FGTS,'total do desconto',t_de_d,'salario liquido',s_l)
    
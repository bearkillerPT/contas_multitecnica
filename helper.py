custos_not_paid = {
    "Gulador SYM Wolf 125":  (1.00, 30.92),
    "Pisca SYM Wolf 125":  (1.00, 27.22),
    "Pedal Travão SYM Wolf 125":  (1.00, 27.45),
    "Serviço Especializado | Técnico: LT (hora)":  (1.50, 17.89),
    "Produtos Diversos":  (2.00, 1.75),
    "Produtos Lavagem":  (1.00, 5.00),
    "Bateria Parts Europe YTX9-BS":  (1.00, 32.00),
}

custos_pagos_mae = {
    "Pneu Moto Mich 110/70-17 54H P STREE":  (1.00, 73.00),
    "Pneu Moto Mich 130/70-17 P Street 62S":  (1.00, 89.30),
    "Sistema Integ pneus usados (DL 111/2001) acess":  (2.00, 0.76),
    "Serviço Especializado | Técnico: L T (hora)":  (0.50, 17.89)
}
total_custos_not_paid = 0
total_custos_pagos_mae = 0
for key, value in custos_not_paid.items():
    total_custos_not_paid += value[0] * value[1]

for key, value in custos_pagos_mae.items():
    total_custos_pagos_mae += value[0] * value[1]


print("Custos não pagos: ", total_custos_not_paid)
print("Custos pagos pela mãe: ", total_custos_pagos_mae)
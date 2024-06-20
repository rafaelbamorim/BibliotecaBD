def validar_ano(ano):
    try:
        ano = int(ano)
        if ano <= 0 or ano > 2024:
            return False
        return True
    except ValueError:
        return False

def validar_num_paginas(num_paginas):
    try:
        num_paginas = int(num_paginas)
        if num_paginas > 0:
            return True
        return False
    except ValueError:
        return False

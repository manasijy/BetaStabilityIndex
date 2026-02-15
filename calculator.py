def calculate_mo_eq(comp):
    return (
        comp.get("Mo", 0)
        + 0.67 * comp.get("V", 0)
        + 0.44 * comp.get("W", 0)
        + 0.28 * comp.get("Nb", 0)
        + 0.22 * comp.get("Ta", 0)
        + 2.9 * comp.get("Fe", 0)
        + 1.6 * comp.get("Cr", 0)
        + 1.25 * comp.get("Ni", 0)
        + 1.7 * (comp.get("Mn", 0) + comp.get("Co", 0))
    )


def calculate_al_eq(comp):
    return (
        comp.get("Al", 0)
        + comp.get("Sn", 0)/3
        + comp.get("Zr", 0)/6
        + 10 * (
            comp.get("C", 0)
            + comp.get("O", 0)
            + 2 * comp.get("N", 0)
        )
    )


def calculate_si_beta(comp):

    mo_eq = calculate_mo_eq(comp)
    al_eq = calculate_al_eq(comp)

    return mo_eq, al_eq, mo_eq - al_eq

import itertools
def get_pins(obs): return [''.join(x) for x in itertools.product(*[{'1':'124','2':'1235','3':'236','4':'1457','5':'24568',
            '6':'3569','7':'478','8':'57890','9':'689','0':'08'}[i] for i in obs])]

def mount_cube_3x3(cube):
    res = ''

    res += f'\n          [{cube["B"][0]}][{cube["B"][1]}][{cube["B"][2]}]          \n'
    res += f'          [{cube["B"][3]}][{cube["B"][4]}][{cube["B"][5]}]          \n'
    res += f'          [{cube["B"][6]}][{cube["B"][7]}][{cube["B"][8]}]          \n'
    
    res += f'\n          [{cube["U"][0]}][{cube["U"][1]}][{cube["U"][2]}]          \n'
    res += f'          [{cube["U"][3]}][{cube["U"][4]}][{cube["U"][5]}]          \n'
    res += f'          [{cube["U"][6]}][{cube["U"][7]}][{cube["U"][8]}]          \n'
    
    res += f'\n[{cube["L"][0]}][{cube["L"][1]}][{cube["L"][2]}] [{cube["F"][0]}][{cube["F"][1]}][{cube["F"][2]}] [{cube["R"][0]}][{cube["R"][1]}][{cube["R"][2]}]\n'
    res += f'[{cube["L"][3]}][{cube["L"][4]}][{cube["L"][5]}] [{cube["F"][3]}][{cube["F"][4]}][{cube["F"][5]}] [{cube["R"][3]}][{cube["R"][4]}][{cube["R"][5]}]\n'
    res += f'[{cube["L"][6]}][{cube["L"][7]}][{cube["L"][8]}] [{cube["F"][6]}][{cube["F"][7]}][{cube["F"][8]}] [{cube["R"][6]}][{cube["R"][7]}][{cube["R"][8]}]\n'
    
    res += f'\n          [{cube["D"][0]}][{cube["D"][1]}][{cube["D"][2]}]          \n'
    res += f'          [{cube["D"][3]}][{cube["D"][4]}][{cube["D"][5]}]          \n'
    res += f'          [{cube["D"][6]}][{cube["D"][7]}][{cube["D"][8]}]          '

    return res
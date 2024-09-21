s = 0
nume = 1
deno = 1

while nume != 39:
    s += nume/deno
    nume+= 2
    deno*=2

print(f'{s:.2f}')

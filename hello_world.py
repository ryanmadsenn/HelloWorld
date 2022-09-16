red = "\033[0;31m"
yellow = "\033[1;33m"
green = "\033[0;32m"
blue = "\033[0;34m"
purple = "\033[0;35m"

colors = [red, yellow, green, blue, purple]

for i in range(100000):
    print(f"{colors[(i%5)]}H{colors[(i%5)-4]}e{colors[(i%5)-3]}l{colors[(i%5)-2]}l{colors[(i%5)-1]}o {colors[(i%5)]}W{colors[(i%5)-4]}o{colors[(i%5)-3]}r{colors[(i%5)-2]}l{colors[(i%5)-1]}d")
    
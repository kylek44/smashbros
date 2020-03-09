import sys
f = open(sys.argv[1], "r")
of = open(sys.argv[2], "w")
for line in f:
    line = line.strip()
    if len(line) == 64:
        for x in range(len(line)):
            if x % 8 == 0:
                of.write(" ")
            of.write(line[x])
        of.write("\n")
f.close()

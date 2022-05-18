# Files

filename = "dataset/mbox-short.txt"

fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:

    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    spacepos = line.find(" ")

    num = float(line[spacepos+1:])
    total = total + num


ave = total / count
print("Average spam confidence:", ave)
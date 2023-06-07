import csv

def process():
    names = ["POGZ.fasta", "H2B.fasta", "H2A.fasta", "H3.fasta", "H4.fasta"]
    namesfiles = ["c.elegans", "ciliate", "drosophila", "e.coli",
                  "human", "methanocaldococcus", "mouse",
                  "thermococcus", "tuberculosis", "yeast", "zebrafish"]
    
    with open('hits.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        writer.writerow([""] + namesfiles)
        
        for name in names:
            row_data = []
            row_data.append(name)
            
            for filename in namesfiles:
                with open("{name}.{filename}.blast".format(name=name, filename=filename)) as file:
                    for i, line in enumerate(file):
                        if i == 4:
                            splitted = line.split(" ")
                            row_data.append(splitted[1])
                            break
            writer.writerow(row_data)

process()

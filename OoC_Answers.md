# OoCA_Motof-mark Written Assignment: 
## Classes Needed: 
**Motif Class**\
- holds the motif and the variations held by regex
``` python
class motif: 
    def __init__(self, motif, variations (REGEX)):
        self.motif = motif
        self.var = [MOTIF REGEX]
```
*METHODS*\
- locate the motif and any variations within the sequence
- 
**FASTA RECORD Class**\
- holds the intron and exon locations 
- hold total length of record
``` python
class record
    def __init__(self, intron_start, intron_end, exon_start, exon_end, total_len):
        self.intron_start = intron_start
        self.intron_end = intron_end
        self.exon_start = exon_start
        self.exon_end = exon_end
        self.total_len = len(self)
```
*METHODS*\
- get length of the record
- get length relative to longest 

## Class interactions 
The motif class must be able to take in a fasta object and scan it for the pattern. It must be able to find and store the nt positions of each motif on an individual record (or start pos + len) 


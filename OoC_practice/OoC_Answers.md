# OoCA_Motof-mark Written Assignment: 
## Classes Needed: 
**Motif SEQ Class**\
*ATTRIBUTES*
- holds the motif and the variations held by regex
- COLOR assigned to the 
``` python
class motif SEQ: 
    def __init__(self, motif, variations (REGEX)):
        self.motif = motif
        self.var = [MOTIF REGEX]
```
*METHODS*\
- locate the motif and any variations within the sequence
- popuilate the motif locus class with nt start and len of motif
**Motif LOCUS Class**\
*ATTRIBUTES*\
- Which fasta seq its on 
- start 
- len
- color
*METHODS*\
- hold individual positions of given motif 
- holds assigned color RGB code 
- MAYBE draw itself (jason suggestion)
**FASTA RECORD Class**\
*ATTRIBUTES*\
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
- MAYBE draw itself (jason suggestion)

## Class interactions 
The motif class must be able to take in a fasta object and scan it for the pattern. It must be able to find and store the nt positions of each motif on an individual record (or start pos + len) 


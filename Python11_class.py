#!/usr/bin/env python3


class DNARecord(object):
#defining class attributes

	def __init__(self, sequence, gene_name, species_name):


		self.sequence=sequence
		self.gene_name=gene_name
		self.species_name=species_name


#adding methods

#1)length method
		self.length=len(sequence)


	


#2) Nucleotide composition method

	def get_ATGC(self):

		a_count = self.sequence.count("A")
		t_count= self.sequence.count("T")
		g_count= self.sequence.count("G")
		c_count=self.sequence.count("C")
		
		

		gc_content=(g_count + c_count)/self.length

		print ("GC content is", gc_content)
		return a_count, t_count, g_count, c_count, gc_content


## Create new DNARecord Objects with user defined data
dna_rec_obj_1 = DNARecord('ACTGATCGTTACGTACGAGT', 'ABC1', 'Drosophila melanogaster')
dna_rec_obj_2 = DNARecord('ATATATTATTATATTATA', 'COX1', 'Homo sapiens')


for x in [ dna_rec_obj_1, dna_rec_obj_2]:

	print("name:", x.gene_name,",", "seq:", x.sequence)

	gc_content = x.get_ATGC()
	print(gc_content)

import pubchempy as pcp
from rdkit.Chem.AllChem import MolFromSmiles
from rdkit.Chem.Draw import MolsToImage
from PIL import Image
from time import sleep

def describe_me(compound):
	mol_formated_molecule = MolFromSmiles(compound.isomeric_smiles)
	legend = compound.to_dict(properties=(
    'molecular_formula', 'molecular_weight', 'isomeric_smiles', 'inchi', 'iupac_name', 'exact_mass'
    ))
	tup_list = [item for item in legend.items()]
	lege = ''
	for tup in tup_list:
		lege += f'{str(tup)}\n'
	print(lege)
	image = MolsToImage([mol_formated_molecule],subImgSize=(1200,800),fitimage=True,legends=[lege])
	image.show()

request = input('Search: molecule\n')
responce = pcp.get_cids(request, 'name')

if len(responce) < 1:
    print("I couldn't find what you were looking for")
elif len(responce) == 1:
    print('Searching')
    compound = pcp.Compound.from_cid(responce[0])
    describe_me(compound)
else:
	print('Compound	:	CID')
	for responces in responce:
		print({pcp.Compound.from_cid(responces).synonyms[0]: responces})
	choice = input('Select a CID to search\n')
	try: 
		int(choice)
		compound = pcp.Compound.from_cid(int(choice))
		describe_me(compound)
	except ValueError:
		if choice == 'all':
			for responces in responce:
				compound = pcp.Compound.from_cid(responces)
				describe_me(compound)
				sleep(12)
		else:
			raise

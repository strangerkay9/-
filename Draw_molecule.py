from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import MolToFile
from subprocess import getoutput

while True:
	molecule = input('Please input the SMILES\n')
	if molecule:
		mol_formated_molecule = AllChem.MolFromSmiles(molecule)
		image = Draw.MolToFile(mol_formated_molecule, 'temp.svg', size=(900, 900))
		getoutput('xdg-open temp.svg')
		getoutput('rm temp.svg')
	else:
		print("it ain't work")


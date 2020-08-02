from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit import Chem
from sys import argv
from subprocess import getoutput

if argv[1].split('.')[1] == "smi" or argv[1].split('.')[1] == "smiles":
	smile_doc = argv[1]
	mols = []
	smile_collection = []
	with open(smile_doc, 'r') as smile_list:
		file_name = smile_doc.split('.')[0]
		for smile in smile_list:
			mols.append(Chem.MolFromSmiles(smile))
			smile_collection.append(smile.split('\n')[0])
		if len(mols) < 250:
			image = Draw.MolsToGridImage(mols,molsPerRow=3,subImgSize=(600,600),legends=[smile for smile in smile_collection])
			image.save('temp_image.png')
		if len(mols) > 13:
			getoutput('rm -rf MultiPNG')
			getoutput('mkdir MultiPNG')
			counter = 0 
			while len(mols) > 13:
				poped_mols = []
				poped_smiles = []
				for number in range(12):
					poped_mols.append(mols.pop(0))
					poped_smiles.append(smile_collection.pop(0))
				image = Draw.MolsToGridImage(poped_mols,molsPerRow=3,subImgSize=(400,400),legends=[smile for smile in poped_smiles])
				ImageTitle = file_name + '(' + str(counter + 1) + ')' + ".png"
				image.save(ImageTitle)
				counter += 1
			if len(mols) <= 13:
				image = Draw.MolsToGridImage(mols,molsPerRow=3,subImgSize=(400,400),legends=[smile for smile in smile_collection])
				ImageTitle = file_name + '(' + str(counter + 1) + ')' + ".png"
				image.save(ImageTitle)
			getoutput('xdg-open temp_image.png')
			getoutput('rm temp_image.png')
			getoutput('mv *.png MultiPNG')
		else:
			image = Draw.MolsToGridImage(mols,molsPerRow=3,subImgSize=(600,600),legends=[smile for smile in smile_collection])
			ImageTitle = file_name +".png"
			image.save(ImageTitle)
			getoutput('xdg-open temp_image.png')
			getoutput('rm temp_image.png')
else:
	print('Try again with a smile file, hey that rymes')

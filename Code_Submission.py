import pubchempy as pcp

def fetch_smiles(compound_name):
    """
    Fetch the SMILES string for a given compound name using PubChem.
    
    Parameters:
        compound_name (str): The name of the compound to search.
    
    Returns:
        dict: A dictionary with the validation result and compound details.
    """
    try:
        # Search PubChem for the compound using its name
        compounds = pcp.get_compounds(compound_name, namespace='name')
        
        if compounds:
            compound = compounds[0]  # Take the first match
            return {
                'valid': True,
                'cid': compound.cid,
                'name': compound.iupac_name,
                'molecular_formula': compound.molecular_formula,
                'molecular_weight': compound.molecular_weight,
                'canonical_smiles': compound.canonical_smiles
            }
        else:
            return {'valid': False, 'error': "No match found in PubChem."}
    except Exception as e:
        return {'valid': False, 'error': str(e)}

def validate_reactant_and_product():
    """
    Take user inputs for reactant and product names, fetch their SMILES,
    and verify if they exist in PubChem.
    """
    # Get user input for reactant and product
    reactant_name = input("Enter the reactant name: ").strip()
    product_name = input("Enter the product name: ").strip()
    
    # Fetch and validate reactant
    reactant = fetch_smiles(reactant_name) 
    if reactant['valid']:
        print(f"Reactant Validated!\n"
              f" - Name: {reactant['name']}\n"
              f" - CID: {reactant['cid']}\n"
              f" - Molecular Formula: {reactant['molecular_formula']}\n"
              f" - Molecular Weight: {reactant['molecular_weight']} g/mol\n"
              f" - Canonical SMILES: {reactant['canonical_smiles']}\n")
    else:
        print(f"Reactant Invalid! Error: {reactant['error']}")
        return
    
    # Fetch and validate product
    product = fetch_smiles(product_name)
    if product['valid']:
        print(f"Product Validated!\n"
              f" - Name: {product['name']}\n"
              f" - CID: {product['cid']}\n"
              f" - Molecular Formula: {product['molecular_formula']}\n"
              f" - Molecular Weight: {product['molecular_weight']} g/mol\n"
              f" - Canonical SMILES: {product['canonical_smiles']}\n")
    else:
        print(f"Product Invalid! Error: {product['error']}")
        return

    print("\nBoth reactant and product are valid. Proceeding with further steps...")

# Example Usage
validate_reactant_and_product()

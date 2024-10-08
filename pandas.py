import pandas as pd
import re

# Sample data
data = [
    "Benzapen 12 Lac Inj 10's",
    "Betaburn Oint 25g",
    "Betameson Crm 20gm",
    "Betameson Oint 20g",
    "Betameson-CL Crm 15g",
    "Betameson-N Crm 15g T",
    "BetriXa 40 Cap 10's",
    "BetriXa 80 Cap 10's",
    "Beviprex HFA MDI 120puffs",
    "Bicozin Syp 200ml",
    "Bicozin Syrup - 100mI",
    "Bicozin Tab 30's SQ",
    "Bicozin-I Syp 100mI",
    "Bilista 20 Tab 20's",
    "Bilista Kids 10 Tab 30's",
    "Bimator E-Drop 3mI",
    "Bioprem 1 Soft Gel Cap 30's",
    "Bioprem 2.5 Soft Gel Cap 30's",
    "Bisocam 2.5/5 Tab",
    "Bisocor 2.5 Tab 50’s SQ",
    "Bisocor S Tab 30's",
    "Bisocor Plus 2.5/6.25 Tablet",
    "Bisocor Plus 5/6.25 Tablet",
    "Bolardi 250 Cap 30's",
    "Bolardi SOO Cap 30's",
    "Bonizol IV infusion",
    "Brofex Syrup",
    "Bromolac Tablet",
    "Bufocort 200 Cozycap 30's",
    "Bufocort 400 Cozy Cap",
    "Burna Cream",
    "Caberol 0.5 Tab 6's SQ",
    "Calbo 500 Tab 100's SQ",
    "Calbo JR Tab 60's",
    "Calbo-C Tab 10's",
    "Calbo-D Tab 30’s SQ",
    "Calbo-D Vita",
    "Calboplex Tab 30's",
    "Calboral -D Tab 30's SQ",
    "Calboral -DX Tab 30’s SQ",
    "Calbostar 400 Tab 30’s",
    "Calbostar 740 Tab 30's",
    "Cal botol Tab 30's",
    "Calcitrol Licap",
    "Caloprid Caloprid 1 Tab 20's",
    "Caloprid 2 Tab 20's",
    "Camlodin S Mg Tablet",
    "Camlodin Plus 35 Tab 30's",
    "Camlodin Plus Tab 56's",
    "Camlosart Camlosart 5/20 Tab 30’s",
    "Camlosart 5/40 Tab 20's",
    "Camlotel 5/40 Tab 30's",
    "Camlotel 5/80 Tab 30's",
    "Canaglif 100 Tablet",
    "Candex Suspension 30 ml",
    "Carbizol 10 Tab 60's",
    "Carbizol S Tab 100’s",
    "Cardi Q 100 Soft Gel Cap 3O's",
    "Cardi Q 50 Soft Gel Cap 30's",
    "Carva Carva 75Tab 200's SQ",
    "Cavir 0.5 Tab 10's",
    "Cavir 1 mg Tablet",
    "Ceevit DS Tablet",
    "Ceevit Forte Effervescent Tab",
    "Ceevit Tablet",
    "Cef-3 Cap 14's",
    "Cef-3 DS Cap 14's",
    "Cef-3 Forte PFS 50mI",
    "Cef-3 F4ax P-Drop 20mI",
    "Cef-3 Paediatric Drop -2 1 ml",
    "Cef-3 PFS 30mI",
    "Cef-3 PFS 75mI",
    "Cef-3 Susp -50 ml",
    "Cefopen 1g IN/IV lnj",
    "Cefopen 2g IN/IV !nj",
    "Cefotil 1.5g IV tnj",
    "Cefotil 250 mg tablet",
    "Cefotil 500 mg tablet",
    "Cefotil 750 mg tnj",
    "Cefotil PFS 70mI",
    "Cefotil Plus 250 Tab 12’s",
    "Cefotil Plus 500 Tab 12's",
    "Cefotil Plus PFS 70mI",
    "Ceftiben 400 Capsule",
    "Ceftron 1Gm Inn Injection",
    "Ceftron 1Gm lv Injection",
    "Ceftron 2 Gm lv Injection",
    "Ceftron 250PIg Im Injection",
    "Ceftron 250Ng Tv Injection",
    "Ceftron Ceftron 500Mg Inn Injection",
    "Ceftron 500Ng 1v Injection",
    "Cerevas Tablet",
    "Cilosta Tablet",
    "Cinaron Plus Tab 140's",
    "Cinaron Tab 200's",
    "Ciprocin 250 Tablet",
    "Ciprocin 500 Tab 30’s SQ",
    "Ciprocin 750 Tab 20’s SQ",
    "Ciproci n Dry Powder for Suspension",
    "Ciprocin Eye/Ear Drop"
]

# Create a DataFrame
df = pd.DataFrame(data, columns=['ProductDetails'])

# Define the mappings
mapping = {
    'tab': 'tablet',
    'inj': 'injection',
    'suss': 'suspension',
    'crm': 'cream',
    'ointment': 'ointment',
    'syp': 'syrup',
    'inf': 'infusion',
    'inh': 'inhaler',
    'cap': 'capsule',
    'oral sol': 'oral solution',
    'HFA MDI': 'MDI',
    'Soft Gel Cap': 'soft gel capsule',
    'Cozycap': 'cozy cap',
    'Effervescent': 'effervescent',
    'Drop': 'drop',
    'Susp': 'suspension',
    'Powder': 'powder',
    'Capsule': 'capsule'
}

# Function to extract and map product type
def map_product_type(description):
    for key in mapping:
        if key.lower() in description.lower():
            return mapping[key]
    return 'Unknown'

# Extract product name and type
def extract_product_info(details):
    parts = details.split()
    name = " ".join(parts[:-1])  # Assume last part is quantity/type
    type_desc = map_product_type(details)
    return pd.Series([name, type_desc], index=['ProductName', 'Description'])

# Apply extraction and mapping
df[['ProductName', 'Description']] = df['ProductDetails'].apply(extract_product_info)

# Display the DataFrame
print(df[['ProductName', 'Description']])

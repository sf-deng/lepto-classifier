# lepto-classifier
A SVM-based binary classifier to detect leptospirosis diseases in dogs. 
See (insert paper link) for more details.

## Example usage
```
from lepto_classifier import LeptoClassifier

data_path = "data/my_data.csv"
clf = LeptoClassifier()
predictions_with_mat = clf.predict(data_path, use_mat=True)
predictions_without_mat = clf.predict(data_path, use_mat=False)
```
The predict method will output a pandas series having the same length as the number of rows in the data csv file. A prediction value 1 means lepto positive, 0 means lepto negative, and -1 means no prediction is made due to missing values.

## How to prepare the data
The data csv file must contain the following columns:
- Weight
- Sex: (male=1, female=0)
- Breed Group: (must be Toy, Herding, Hound, Mix, Non-Sporting, Sporting, Terrier, Working, Foundation Stock Service, or Other)
- Anion Gap
- Sodium 
- Potassium
- Chloride
- Bicarb
- Phosphorus
- Calcium
- BUN
- Creatinine
- Glucose
- Total Protein
- Albumin
- Globulin
- ALT
- AST
- ALP
- GGT
- Cholesterol
- Bilirubin
- Urine Specific Gravity
- Urine
- Urine Glucose
- Hct
- Hgb
- MCV
- WBC
- Bands
- Neut
- Lymph
- Mono
- Eosin
- Plt

If use_mat is set to True (default False) in the LeptoClassifier.predict method. Then the column "MAT" must also be provided in the csv file.
- MAT: (must be 0, 100, 200, 400, ...)

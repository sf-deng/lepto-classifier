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
The data csv file must contain the following columns (case-sensitive)
- Weight (kg)
- Sex (binary encoded, male=1, female=0)
- Breed Group (must be "Toy", "Herding", "Hound", "Mix", "Non-Sporting", "Sporting", "Terrier", "Working", "Foundation Stock Service", or "Other"; case-sensitive)
- Anion Gap (mmol/L)
- Sodium (mmol/L)
- Potassium (mmol/L)
- Chloride (mmol/L)
- Bicarb (mmol/L)
- Phosphorus (mg/dL)
- Calcium (mg/dL)
- BUN (mg/dL)
- Creatinine (mg/dL)
- Glucose (mg/dL)
- Total Protein (g/dL)
- Albumin (g/dL)
- Globulin (g/dL)
- ALT (IU/L)
- AST (IU/L)
- ALP (IU/L)
- GGT (IU/L)
- Cholesterol (mg/dL)
- Bilirubin (mg/dL)
- Urine Specific Gravity (as a number)
- Urine Protein (as a number 0,1,2,3,4)
- Urine Glucose (0-4)
- Hct (%)
- Hgb (g/dL)
- MCV (fL)
- WBC (/mcL)
- Bands (/mcL)
- Neut (/mcL)
- Lymph (/mcL)
- Mono (/mcL)
- Eosin (/mcL)
- Plt (/mcL)

If use_mat is set to True (default False) for the LeptoClassifier.predict method. Then the column "MAT" must also be provided in the csv file.
- MAT: (Use the recipricol titer: 0, 100, 200, 400, ...)

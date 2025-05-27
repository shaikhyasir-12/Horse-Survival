🐎 Horse Survival - Machine Learning Project
This project uses machine learning to predict the survival outcome of horses based on medical data. It includes data preprocessing, exploratory data analysis (EDA), model training, and evaluation.


📁 Project Structure

Horse Survival Project/
│
├── data/                    # Contains the dataset CSV file(s)
├── venv/                   # Python virtual environment (ignored by Git)
├── horse_survival.py       # Main script for data analysis and modeling
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # License file
└── .gitignore              # Git ignored files

📊 Features of the Project
Exploratory Data Analysis (EDA) using Seaborn and Matplotlib

Survival analysis based on:

Surgery status

Pain level

Age of horse

Model training using Scikit-learn

Predictive modeling to determine likelihood of horse survival

Visualization of survival outcome distributions

📦 Installation
1.Clone the repository
git clone https://github.com/shaikhyasir-12/Horse-Survival.git
cd Horse-Survival

2.Create a virtual environment (optional but recommended)
python -m venv venv

3.Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

4.Install dependencies
pip install -r requirements.txt

🚀 How to Run
Run the main Python script:
python horse_survival.py

📈 Visualizations
The project includes visual insights into how different features such as age, pain level, and surgery status affect the survival outcome.

Example plots:

Survival Outcome Distribution

Outcome by Age

Outcome by Surgery

Outcome by Pain Level


🧠 Models Used
Logistic Regression

Decision Tree (optional)

Accuracy metrics (like Confusion Matrix, Classification Report)

📚 Dataset
The dataset is stored in the data/ folder and includes medical information of horses.

🪪 License
This project is licensed under the MIT License. See the LICENSE file for more info.

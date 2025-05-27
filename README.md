
<<<<<<< HEAD
=======
# 🐎 Horse Survival Analysis

This project analyzes and visualizes factors affecting the survival outcomes of horses based on medical data. The analysis includes survival rates and correlations with features like age, surgery, and pain levels.

## 📊 Project Overview

The dataset is used to explore the survival outcomes (`lived`, `died`, `euthanized`) of horses and their relation to multiple clinical variables. Bar plots are generated to understand how each factor (such as age, surgery, and pain level) correlates with the survival outcome.

## 📁 Project Structure

```
horse_survival/
├── data/                 # Contains the dataset (not included in repo)
├── venv/                 # Python virtual environment
├── horse_survival.py     # Main analysis and visualization script
├── LICENSE
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## 🧪 Features Analyzed

- **Age**: Comparison between adults and young horses
- **Surgery**: Impact of whether surgery was performed
- **Pain Level**: Categorized levels such as mild, severe, depressed, alert, and extreme
- **Outcome**: Final status of the horse (`lived`, `died`, `euthanized`)

## 🖼️ Visualizations

Some of the visualizations include:
- Overall survival distribution
- Survival by age group
- Survival with/without surgery
- Survival based on pain levels


## 🛠️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/shaikhyasir-12/Horse-Survival.git
   cd horse_survival
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the analysis script:
   ```bash
   python horse_survival.py
   ```

## 📦 Requirements

All dependencies are listed in `requirements.txt`. Key libraries include:

- pandas
- matplotlib
- seaborn

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
>>>>>>> 5341145 (Update README.md with project details)

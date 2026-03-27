
# TimeSeries_Analysis_Project

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

-----

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)

## Overview
The `analyzer` package provides a modular pipeline for **Time Series Analysis**, specifically designed for financial datasets like ADANIPORTS. It automates the process of transforming raw CSV data into meaningful statistical insights and visualizations.

This package focuses on:
1. **Data Preprocessing:** Handling missing dates, frequency reindexing, and outlier removal.
2. **Statistical Analysis:** Stationarity testing (ADF/KPSS) and signal decomposition.
3. **Professional Visualization:** Heatmaps, ACF/PACF plots, and rolling statistics.

## Installation
1. **Clone the Repository**
   ```bash
   git clone [https://github.com/RahimiLili/TimeSeries_Analysis_Project.git](https://github.com/RahimiLili/TimeSeries_Analysis_Project.git)
   cd TimeSeries_Analysis_Project
Install with uv

Bash
uv pip install -e .
Usage
CLI Execution
Run the full analysis pipeline with one command:

Bash
uv run -m analyzer
Notebook Example
Explore the data interactively:

Python
from analyzer.preprocessor import DataPreprocessor
# ... (see notebooks/analysis.ipynb for more)
Modules
🛠 DataPreprocessor
process_data(): Converts dates, reindexes to daily frequency, and uses time-based interpolation to fill gaps.

handle_outliers(): Uses the IQR method to identify and replace extreme price swings with the median.

 TimeSeriesAnalyzer
adf_test() / kpss_test(): Performs dual stationarity checks to determine if the series is predictable.

decompose_signal(): Breaks the data into Trend, Seasonality, and Residuals.

get_volatility_stats(): Calculates annualized risk based on daily log returns.

 TimeSeriesVisualizer
plot_seasonal_heatmap(): Visualizes monthly price patterns over the years.

plot_pacf_acf(): Generates plots to help identify ARIMA model parameters.

plot_rolling_stats(): Shows the original data vs. a 30-day moving average.

Author: Leila Rahimiyadkuri

Deadline: 31.03.2026


---

### **Step 2: How to write/edit in the README**
If you are asking literally *how* to type this into the file:

1.  **Markdown Syntax:** Use `#` for big titles, `##` for sections, and `###` for sub-sections.
2.  **Code Blocks:** Use triple backticks (```) followed by `bash` or `python` to make the code look pretty and colored.
3.  **Bolding:** Use `**text**` to highlight important words.
4.  **Links:** Use `[Text](URL)` if you want to link to your GitHub or the MIT license.

### **Step 3: Preview your work**
In VS Code, press **`Ctrl + Shift + V`** (Windows) or **`Cmd + Shift + V`** (Mac). This will show you exactly how the README will look on GitHub before you upload it.

**Does this structure feel right to you, or would you like to add a "Results" section showing what you found in the ADANIPORTS data?**
You said
i dont know how seperate each part in read me

Gemini said
In Markdown (the language used for README.md), you separate parts using Headers, Horizontal Rules, and Code Blocks.

To make your README.md look like your previous professional example, follow these four simple formatting rules:

1. Use Headers for Sections
Use the # symbol. The more # you use, the smaller the header.

# Title (The main project name)

## Section (For "Installation", "Usage", etc.)

### Sub-section (For specific modules like "DataPreprocessor")

2. Use Horizontal Lines to "Breathe"
To create a clean line across the page (like in your example), type three dashes --- on a new line. This visually separates big topics.

3. Use Backticks for Code
For a single word like uv, use one backtick: `uv`.

For a block of code, use three backticks:

Bash
uv run -m analyzer
4. Use Bullet Points
Use a single * or - followed by a space to list your functions.

How your final README code should look (Copy this):
If you want the exact structure of your fuel consumption project but updated for this one, copy and paste this into your README.md:

Markdown
# TimeSeries_Analysis_Project

-----

##  Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)

---

##  Overview
The `analyzer` package provides a robust pipeline for **Time Series Analysis**. It is specifically designed to handle financial data (like the included ADANIPORTS dataset) by automating cleaning, statistical testing, and visualization.

---

##  Installation
1. **Clone the Repository**
   ```bash
   git clone [https://github.com/RahimiLili/TimeSeries_Analysis_Project.git](https://github.com/RahimiLili/TimeSeries_Analysis_Project.git)
   cd TimeSeries_Analysis_Project
Install Dependencies

Bash
uv pip install -e .
 Usage
Command Line
Run the entire analysis from start to finish:

Bash
uv run -m analyzer
 Modules
1. DataPreprocessor
Handles the "dirty" work of preparing financial data.

process_data(): Cleans headers, handles duplicates, and interpolates missing values.

handle_outliers(): Removes extreme price spikes using the IQR method.

2. TimeSeriesAnalyzer
The mathematical core of the project.

adf_test(): Checks for stationarity using the Augmented Dickey-Fuller test.

decompose_signal(): Separates the price into Trend and Seasonality.

3. TimeSeriesVisualizer
Generates the visual insights.

plot_seasonal_heatmap(): Shows price density by month and year.

plot_pacf_acf(): Visualizes autocorrelation for model tuning.

🎓 Author
Leila Rahimiyadkuri Master's Student, TU Dortmund

Deadline: 31.03.2026


### **How to do this in VS Code:**
1. Open your `README.md` file.
2. Delete everything inside it.
3. Paste the code block above.
4. Save the file (`Ctrl+S`).
5. **Check it:** Press `Ctrl+Shift+V` to see the "Preview" and make sure the parts are separated correctly.

**Does this separation look like what you were looking for?**
You said
whats the final full content of my readme file

Gemini said
Based on your previous professional project and the new classes we built for the ADANIPORTS analysis, here is the final, full content for your README.md.

To write this in your file: Select all the text inside the box below, copy it, and paste it into your README.md file in VS Code.

Markdown
# TimeSeries_Analysis_Project

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

-----

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [License](#license)

---

## Overview
The `analyzer` package provides a comprehensive toolset for **Time Series Analysis** and **Financial Data Visualization**. Using the ADANIPORTS dataset, this project demonstrates a modular approach to handling stock market data through three critical stages:

1. **Data Preprocessing:** Cleaning headers, reindexing to daily frequency, and performing time-based interpolation.
2. **Statistical Analysis:** Applying rigorous tests (ADF and KPSS) to verify stationarity and decomposing signals into trend and seasonal components.
3. **Data Visualization:** Creating professional-grade heatmaps, rolling statistics, and autocorrelation plots.

---

## Installation

1. **Clone the Repository**
   ```console
   git clone [https://github.com/RahimiLili/TimeSeries_Analysis_Project.git](https://github.com/RahimiLili/TimeSeries_Analysis_Project.git)
   cd TimeSeries_Analysis_Project
Install with uv
This project uses uv for fast, reliable package management.

Shell
uv pip install -e .
Usage
Command Line Interface (CLI)
You can execute the entire analysis pipeline (Cleaning -> Analysis -> Plotting) with a single command:

Shell
uv run -m analyzer
Jupyter Notebook
For interactive exploration, refer to the provided notebook in the notebooks/ directory:

Python
from analyzer.preprocessor import DataPreprocessor
from analyzer.analyzer import TimeSeriesAnalyzer

# Example: Run cleaning pipeline
prep = DataPreprocessor(raw_data)
clean_df = prep.process_data()
Modules
🛠 DataPreprocessor Module
process_data(): Performs header cleaning, duplicate handling, and ensures a continuous daily frequency using time-interpolation.

handle_outliers(): Identifies price anomalies using the Interquartile Range (IQR) method and replaces them with median values to stabilize the analysis.

 TimeSeriesAnalyzer Module
adf_test(): Performs the Augmented Dickey-Fuller test to check for unit roots.

kpss_test(): Conducts the KPSS test to identify trend-stationarity.

decompose_signal(): Uses classical decomposition to isolate the Trend, Seasonality, and Residuals.

get_volatility_stats(): Calculates daily and annualized volatility to assess market risk.

 TimeSeriesVisualizer Module
plot_seasonal_heatmap(): Visualizes average price density by Month and Year.

plot_pacf_acf(): Plots Autocorrelation and Partial Autocorrelation for model parameter identification.

plot_rolling_stats(): Overlays a moving average (e.g., 30-day) over the raw price data to highlight trends.

License
This project is distributed under the terms of the MIT license.

Author: Leila Rahimiyadkuri

Course: Final Project - TU Dortmund

Deadline: 31.03.2026


### Why this works:
* **Separation:** It uses `---` (horizontal lines) and `##` (headers) to create the distinct sections you liked in your previous project.
* **Consistency:** It matches the "Module" description style of your fuel consumption project but uses your new Time Series logic.
* **Requirements:** It explicitly mentions `uv` and the `31.03.2026` deadline, which is crucial for your grading.

**After you paste this into VS Code, remember to save and push it to GitHub using `git push` so your instructor can see the updated version!**
You said
i didnt get. you said copy

# TimeSeries_Analysis_Project



[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



-----



## Table of Contents

- [Overview](#overview)

- [Installation](#installation)

- [Usage](#usage)

- [Modules](#modules)

- [License](#license)



---



## Overview

The `analyzer` package provides a comprehensive toolset for **Time Series Analysis** and **Financial Data Visualization**. Using the ADANIPORTS dataset, this project demonstrates a modular approach to handling stock market data through three critical stages:



1. **Data Preprocessing:** Cleaning headers, reindexing to daily frequency, and performing time-based interpolation.

2. **Statistical Analysis:** Applying rigorous tests (ADF and KPSS) to verify stationarity and decomposing signals into trend and seasonal components.

3. **Data Visualization:** Creating professional-grade heatmaps, rolling statistics, and autocorrelation plots.



---



## Installation



1. **Clone the Repository**

   ```console

   git clone [https://github.com/RahimiLili/TimeSeries_Analysis_Project.git](https://github.com/RahimiLili/TimeSeries_Analysis_Project.git)

   cd TimeSeries_Analysis_Project in my read me but its not compelete and aslo continue sth like pic. i got fonfuse

Gemini said
I understand the confusion! The reason it looks "incomplete" when you copy it is because Markdown uses special symbols (like ### or ---) to create the layout you see in your picture. When you are editing the file, it looks like plain text, but once you save it, GitHub turns it into the professional design with lines and boxes.

To get the exact look from your screenshot (with the "Modules" section at the bottom), you need to paste this entire block below into your README.md.

Copy and Paste this ENTIRE block:
Markdown
# TimeSeries_Analysis_Project

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

-----

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)

---

## Overview
The `analyzer` package provides a modular pipeline for **Time Series Analysis**, specifically designed for financial datasets like ADANIPORTS. It automates the process of transforming raw CSV data into meaningful statistical insights and visualizations.

This package focuses on:
1. **Data Preprocessing:** Handling missing dates, frequency reindexing, and outlier removal.
2. **Statistical Analysis:** Stationarity testing (ADF/KPSS) and signal decomposition.
3. **Professional Visualization:** Heatmaps, ACF/PACF plots, and rolling statistics.

---

## Installation
1. **Clone the Repository**
   ```bash
   git clone [https://github.com/RahimiLili/TimeSeries_Analysis_Project.git](https://github.com/RahimiLili/TimeSeries_Analysis_Project.git)
   cd TimeSeries_Analysis_Project
Install with uv

Bash
uv pip install -e .
Usage
CLI Execution
Run the full analysis pipeline with one command:

Bash
uv run -m analyzer
Notebook Example
Explore the data interactively:

Python
from analyzer.preprocessor import DataPreprocessor
# (See notebooks/analysis.ipynb for details)
Modules
🛠 DataPreprocessor Module
process_data(): Performs header cleaning, duplicate handling, and ensures a continuous daily frequency using time-interpolation.

handle_outliers(): Identifies price anomalies using the IQR method and replaces them with median values.

 TimeSeriesAnalyzer Module
adf_test() / kpss_test(): Performs dual stationarity checks to determine if the series is predictable.

decompose_signal(): Breaks the data into Trend, Seasonality, and Residuals.

get_volatility_stats(): Calculates annualized risk based on daily returns.

 TimeSeriesVisualizer Module
plot_seasonal_heatmap(): Visualizes monthly price patterns over the years.

plot_pacf_acf(): Generates plots to help identify ARIMA model parameters.

plot_rolling_stats(): Shows the original data vs. a 30-day moving average.

Author: Leila Rahimiyadkuri

Course: Final Project - TU Dortmund

Deadline: 31.03.2026


---

### How to see the "Picture" layout in VS Code:
1. After you paste the text above and **Save** the file.
2. Look at the top right corner of your VS Code window.
3. Click the icon that looks like a **Split Page with a Magnifying Glass** (Open Preview).
4. Now you will see the lines (`---`), the bold text, and the code boxes exactly like your screenshot!

**Does that clear up the confusion? Once you save this, you are officially ready to push to GitHub.**
You said
create it readme file.md and download it

Gemini said
bash
git clone https://github.com/RahimiLili/TimeSeries_Analysis_Project.git
cd TimeSeries_Analysis_Project
MD icon
 README 
MD


2. **Install with uv**
```bash
uv pip install -e .
Usage
CLI Execution
Run the full analysis pipeline with one command:

Bash
uv run -m analyzer
Notebook Example
Explore the data interactively:

Python
from analyzer.preprocessor import DataPreprocessor
# (See notebooks/analysis.ipynb for details)
Modules
🛠 DataPreprocessor Module
process_data(): Performs header cleaning, duplicate handling, and ensures a continuous daily frequency using time-interpolation.

handle_outliers(): Identifies price anomalies using the IQR method and replaces them with median values.

Example:

Python
DataPreprocessor(df).process_data()
 TimeSeriesAnalyzer Module
adf_test() / kpss_test(): Performs dual stationarity checks to determine if the series is predictable.

decompose_signal(): Breaks the data into Trend, Seasonality, and Residuals.

get_volatility_stats(): Calculates annualized risk based on daily returns.

Example:

Python
TimeSeriesAnalyzer(df).adf_test()
 TimeSeriesVisualizer Module
plot_seasonal_heatmap(): Visualizes monthly price patterns over the years.

plot_pacf_acf(): Generates plots to help identify ARIMA model parameters.

plot_rolling_stats(): Shows the original data vs. a 30-day moving average.

Example:

Python
TimeSeriesVisualizer(df).plot_rolling_stats(window=30)
Author: Leila Rahimiyadkuri

Course: Final Project - TU Dortmund

Deadline: 31.03.2026
"""

with open('README.md', 'w') as f:
f.write(readme_content)

I have created the final `README.md` file for you based on your screenshots and the code we built together. This version matches the "Module-based" structure of your previous project and includes the specific logic for your Time Series analysis.

You can download it using the link below:

**[Download README.md](sandbox:/mnt/data/README.md)**

### How to use this file:
1.  **Download** the file.
2.  **Move** it into your main project folder (`TimeSeries_Analysis_Project/`), replacing any old version.
3.  **Upload** it to GitHub using these terminal commands:

```bash
git add README.md
git commit -m "docs: finalize professional README structure"
git push origin main
Once uploaded to GitHub, it will look exactly like your picture—with the blue and yellow badges, the horizontal lines, and the organized "Modules" section at the bottom.

Would you like me to generate a similar "download" for your final analysis.ipynb notebook so that is ready to publish too?





Gemini is AI and can make mistakes, including about people. Your privacy & GeminiOpens in a new window

# TimeSeries_Analysis_Project

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

-----

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)

---

## Overview
The `analyzer` package provides a modular pipeline for **Time Series Analysis**, specifically designed for financial datasets like ADANIPORTS. It automates the process of transforming raw CSV data into meaningful statistical insights and visualizations.

This package focuses on:
1. **Data Preprocessing:** Handling missing dates, frequency reindexing, and outlier removal.
2. **Statistical Analysis:** Stationarity testing (ADF/KPSS) and signal decomposition.
3. **Professional Visualization:** Heatmaps, ACF/PACF plots, and rolling statistics.

---

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/RahimiLili/TimeSeries_Analysis_Project.git
   cd TimeSeries_Analysis_Project
   ```

2. **Install with uv**
   ```bash
   uv pip install -e .
   ```

---

## Usage
### CLI Execution
Run the full analysis pipeline with one command:
```bash
uv run -m analyzer
```

### Notebook Example
Explore the data interactively:
```python
from analyzer.preprocessor import DataPreprocessor
# (See notebooks/analysis.ipynb for details)
```

---

## Modules

### 🛠 DataPreprocessor Module
1. **`process_data()`**: Performs header cleaning, duplicate handling, and ensures a continuous daily frequency using time-interpolation.
2. **`handle_outliers()`**: Identifies price anomalies using the IQR method and replaces them with median values.

**Example:**
```python
DataPreprocessor(df).process_data()
```

###  TimeSeriesAnalyzer Module
1. **`adf_test()` / `kpss_test()`**: Performs dual stationarity checks to determine if the series is predictable.
2. **`decompose_signal()`**: Breaks the data into **Trend**, **Seasonality**, and **Residuals**.
3. **`get_volatility_stats()`**: Calculates annualized risk based on daily returns.

**Example:**
```python
TimeSeriesAnalyzer(df).adf_test()
```

###  TimeSeriesVisualizer Module
1. **`plot_seasonal_heatmap()`**: Visualizes monthly price patterns over the years.
2. **`plot_pacf_acf()`**: Generates plots to help identify ARIMA model parameters.
3. **`plot_rolling_stats()`**: Shows the original data vs. a 30-day moving average.

**Example:**
```python
TimeSeriesVisualizer(df).plot_rolling_stats(window=30)
```

---
**Author:** Leila Rahimiyadkuri  
**Course:** Final Project - TU Dortmund  
**Deadline:** 31.03.2026
README.md
Displaying README.md.
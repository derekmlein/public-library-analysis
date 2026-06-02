# Public Libraries: Recovered or Changed?: The Universal Shift and the Locale-Specific Recovery in U.S. Public Libraries After COVID-19
**By Derek Lein** [Portfolio](https://dereklein.carrd.co/) | [LinkedIn](https://www.linkedin.com/in/derek-lein-4171a6291/)

---

## 📚 Project Overview
Libraries were one of the many institutions irrevocably changed by the COVID-19 pandemic. The national circulation rate (materials checked out) suggests a near-full recovery by 2023, but the whole picture tells a different story. Electronic lending exploded during the pandemic and never came back down, masking trailing physical visits, in-person event programming, and physical media circulation recoveries. More importantly, those declines are not uniform across locale types (city, suburban, rural, town).

This project utilizes **Python** for data cleaning and **Tableau** for calculations, visualizations, and analysis to identify which budget class of films is the smartest investment within the current landscape.

---

## 📊 Tableau Dashboard
[![Dashboard](Derek%20Lein%20Public%20Libraries%20Analysis%20Tableau%20Dashboard.png)](https://public.tableau.com/app/profile/derek.lein/viz/PublicLibrary_Draft04/LibrariesRecoveredorChanged)
*> Click the image above to view the interactive dashboard on Tableau Public.*

---

## 🛠️ Tech Stack & Methodology
* **Python:** Data selection, standardization, and cleaning
* **Tableau:** Data aggregation and visualization
  
---

## 📈 Key Strategic Questions
1. **Electronic Circulation:** Are more e-books being checked out post-pandemic?
2. **Locale Recoveries:** Does Locale type dictate the post-pandemic recovery rates of different library functions?

---

## 🎯 Insights & Conclusions
1. **Electronic Circulation Increase:** Every locale type made the same permanent shift to electronic lending after the pandemic. Physical lending remains primary, but electronic lending is now a permanent fixture of how Americans use libraries.
2. **Locale Differences:** City and Suburban libraries show the lowest recovery rates in visits and programming. The data suggests programming recovery correlates with visit recovery, making programming quantity a clear option available to library administrators in those areas to attempt to increase foot traffic. Rural and Town libraries have nearly fully recovered their programming, yet visits remain below 70% of pre-pandemic levels, suggesting a possible ceiling to in-person recovery in sparser communities in regards to programming quantity.
3. **Hypothesis:** My hypothesis is that the barrier in sparse communities is not programming quantity but awareness; residents may simply not know what their library currently offers. If so, the solution differs by locale: more programming in dense communities, better outreach in sparse ones.

---

## 📂 Repository Structure
* `PLS_FY19_AE_pud19i.csv, PLS_FY20_AE_pud20i.csv, PLS_FY21_AE_pud21i.csv, PLS_FY22_AE_pud22i.csv, PLS_FY23_AE_pud23i.csv`: Raw datasets downloaded from imls.gov.
  * [**Institute of Museum and Library Sciences**]([https://www.imls.gov/research-evaluation/surveys/public-libraries-survey-pls])
* `PLS_FY19-23_Data_Dictionary.pdf`: Data dictionary for the Public Library datasets.
* `pls_final.csv`: Cleaned and aggregated dataset following Python script.
* `PLS_Cleaning.py`: Python cleaning script.
  
---

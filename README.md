# Kazakhstan Wages Analysis, 2012–2025

**Live dashboard → https://yernur159.github.io/kazakhstan-wages-analysis/**

An analysis of average monthly wages in Kazakhstan by region and industry, using official data from the Bureau of National Statistics (BNS ASPR RK, [taldau.stat.gov.kz](https://taldau.stat.gov.kz)). It looks at how much wages grew in nominal and real terms, which regions sit above or below the national average, and which industries pay the most.

*Анализ средней зарплаты в Казахстане по регионам и отраслям за 2012–2025 годы по официальным данным БНС. Дашборд на русском языке.*

## Key findings

1. **Nominal wages grew 3.5×** between 2015 and 2025, from 126,021 ₸ to 443,315 ₸ a month. Most of that growth went to inflation.
2. **Real wages fell 1.8% in 2025.** This is the first fall since 2017; prices grew faster than wages. The strongest real growth was in 2019 (+9.1%) and 2021 (+8.8%).
3. **Only 5 of 20 regions earn above the national average:** Mangystau, Atyrau, Astana, Ulytau and Almaty city. Oil regions and the two largest cities pull the average up.
4. **The regional gap is shrinking.** In 2018 the top region earned 2.82× the bottom one; in 2025 the gap was 1.95×. Since 2018, Almaty, Akmola and Turkistan regions roughly tripled their average wage, while oil-rich Atyrau grew by 109%.
5. **Finance and IT pay the most** (921k ₸ and 835k ₸ in 2025). Information & communication grew fastest since 2015 (+362%). Education, arts and agriculture pay the least.

## Dashboard

- KPI tiles: average wage, real growth, regions above average, regional gap
- Wage trend for Kazakhstan vs any region (region selector)
- Real wage index by year (growth vs decline)
- Regional gap over time (max ÷ min region)
- Regions in 2025: deviation from the national average
- Industries: 2025 level and growth since 2015 (sortable)
- Every chart has hover tooltips; regions and industries also have data tables

Built as one self-contained HTML page with Chart.js, light and dark themes, and a mobile layout.

## Data

| File | Description |
|---|---|
| `data/wages_by_region.csv` | Average nominal monthly wage per employee, ₸, by region and year (BNS indicator 702972) |
| `data/wages_by_sector.csv` | The same indicator by industry (economic activity) |
| `data/real_wage_index.csv` | Real wage index, % to previous year (BNS indicator 702976). BNS does not publish the 2020 value in this table |
| `data/dashboard_data.json` | Data prepared for the dashboard |

Notes:
- Shymkent and Turkistan region appear from 2018, after South Kazakhstan region was split. The former South Kazakhstan region is not shown.
- Abai, Zhetysu and Ulytau regions appear from 2022.
- The data was collected from the BNS Taldau portal.

## How to reproduce

```bash
pip install pandas
python build_data.py   # writes the CSV files
python analysis.py     # prints the findings and writes dashboard_data.json
```

## Tools

Python (pandas) · Chart.js · HTML/CSS · GitHub Pages

## Author

**Yernur Yessenkeldi**, Junior Data Analyst, Astana
[LinkedIn](https://www.linkedin.com/in/yernur-yessenkeldi-737437387/) · [GitHub](https://github.com/Yernur159) · esenkeldinov17.06@gmail.com

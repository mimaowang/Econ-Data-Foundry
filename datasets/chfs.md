---
schema_version: 2
catalog_status: ready
id: chfs
name: China Household Finance Survey (CHFS)
aka:
- CHFS
- 中国家庭金融调查
- China Household Finance Survey
- 西南财大CHFS
- 中国家庭金融
provider: Survey and Research Center for China Household Finance (SWUFE), Southwestern University of Finance and Economics
china_related: true
domains:
- finance
- labor
- consumption
- housing
- development
- public
unit_of_observation: Household-Year/Individual-Year (Tracking Panel Design)
structure: longitudinal-panel
geo_granularity:
- personal
- family
- community
- County
- city
- province
geography: 29 provinces/cities/autonomous regions in mainland China
time_span:
  start: 2011
  end: ongoing
  last_confirmed_release: 2021
  coverage_note: Six rounds confirmed for 2011/2013/2015/2017/2019/2021
  last_checked: '2026-07-10'
frequency:
- biennial
sample_size: Approximately 8,438 households/29,324 people in 2011; subsequent rounds expanded to approximately 40,000 households/year
key_variables:
- Household assets (real estate/financial assets/industrial and commercial assets/vehicles/land)
- Household debt (mortgage/consumer loan/business loan/private loan)
- Household income (salary/business/property/transfer)
- Household consumption (eight categories + housing related)
- Real estate information (number of units/area/market value/time of purchase/mortgage)
- Financial assets (deposits/stocks/funds/financial management/insurance)
- Entrepreneurship and small and micro enterprise management
- Credit constraints (application/approval/denial/interest rate)
- Financial literacy (interest rate calculation/inflation understanding/risk diversification)
- Social security (medical insurance/pension/minimum living security)
- Demographics of family members (age/education/marriage/hukou/employment)
research_fit:
  best_for:
  - A balance sheet study of household properties, financial assets, liabilities, credit constraints, and entrepreneurship
  choose_over:
  - Prioritize CFPS in research on housing, wealth and debt
  - Compare CFPS, CHARLS/CHNS, and CGSS respectively when studying child development, in-depth health, or social attitudes
  not_good_for:
  - Corporate level research
  - biomarkers
  - long term annual history
  - precision agricultural production
  needs_join_for:
  - City housing prices, land policies and financial environment need to be joined by city/province and year; fine geographical
    codes may be restricted
  variation_available:
  - Home Biennial Panel
  - Differences in urban housing and credit environments
  - financial policy changes
  topics:
  - household savings
  - household consumption
  - mortgage
  - household debt
  - Minimum wage (requires external policy timing)
  - Education savings (need to check round questionnaire)
good_for:
- Household asset allocation and wealth inequality - real estate vs financial assets, decomposition of wealth gaps between
  urban and rural areas/regions/classes
- Household debt and leverage—the determinants of housing loans/consumer loans/private lending and the implications for macro-financial
  stability
- Entrepreneurship and Financing Constraints—The Impact of Financial Accessibility and Credit Constraints of Small and Micro
  Business Owners on Entrepreneurial Behavior
- Housing market - the causal effects of multiple units/vacancy rate/mortgage burden on household consumption and labor supply
- Financial Literacy and Financial Inclusion – How financial literacy affects household participation in stock market/insurance
  and borrowing behavior
- Social Security and Household Behavior - The Causal Effects of Medical Insurance/Pension on Household Savings, Consumption
  and Risk-taking
identification:
- Panel fixed effects (household/individual)
- DID (Policy/City Difference)
- IV (policy/system exogenous impact)
- RD
linkable_keys:
- Provincial code
- City code
- Community code (authorization required)
- Family ID
access_routes:
- route: chfs-data-center
  access_status: available-with-application
  direct_url: https://chfs.swufe.edu.cn/sjzx.htm
  requirements: Registration, study description, and data use agreement.
  steps:
  - Enter the CHFS data center.
  - Register and submit a research proposal.
  - Download the approved round and documents after review.
  deliverable: Family/personal data on public application version; sensitive fields provided by permissions.
  cost: free
  last_checked: '2026-07-10'
access:
  url: 'https://chfs.swufe.edu.cn (CHFS official website); Data application: https://chfs.swufe.edu.cn/sjzx.htm'
  cost: free
  license: Academic research only, registration + signing of data use agreement required
  format:
  - dta
  - csv
  api: false
  how_to_get: 1) Visit https://chfs.swufe.edu.cn and register; 2) submit an application and research plan and sign the data-use agreement; 3) after approval, download the available waves. Access is free but application-controlled.
caveats: The core strength of CHFS lies in the detailed measurement of assets/liabilities/properties - this is the weakness
  of CFPS/CHARLS. However, CHFS has limited coverage in areas such as health, cognition, and attitude. Some sensitive financial
  variables (accurate property market value, private lending) may be underreported. The baseline sample size in 2011 was relatively
  small (~8,000 households) and expanded significantly after 2013.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: Yu, Tang & Huang (2023), Does the Business Environment Promote Entrepreneurship? Evidence from the China Household
    Finance Survey
  journal: CER
  year: 2023
  dataset_role: Main results of family entrepreneurship and financing constraints; joined with the business environment
  data_note: Using CHFS family entrepreneurship + business environment data, we found that optimizing the business environment
    significantly increases the probability of family entrepreneurship - especially for families with strong financial constraints,
    the effect is greater
- cite: 'Bu & Liao (2022), Land Property Rights and Rural Enterprise Growth: Evidence from Land Titling Reform in China'
  journal: JDE
  year: 2022
  dataset_role: Key household micro-outcomes; joined with land title confirmation and business registration data
  data_note: 'Using CHFS micro household survey + Ministry of Agriculture land rights confirmation data + enterprise registration
    data, and using land rights confirmation reform as DID, we found that clear land property rights significantly promote
    rural entrepreneurship through four channels: financial capital (rental income), land transfer, human capital and social
    trust.'
provenance:
- source: CHFS official site https://chfs.swufe.edu.cn (supports survey design, waves, variable coverage, and access conditions)
  added: '2026-07-08'
  confidence: high
  verified: true
- source: Crossref abstract for Yu et al., https://doi.org/10.1016/j.chieco.2023.101977 (supports use of CHFS)
  added: '2026-07-08'
  confidence: high
  verified: true
related_datasets:
- cfps
- charls
- cgss
- chns
---

## Positioning in one sentence
CHFS (China Household Finance Survey) is China’s most specialized **household finance** tracking survey conducted by Southwestern University of Finance and Economics since 2011——
Taking household assets (real estate/finance/industrial and commercial), liabilities (mortgage/consumer loan/private lending) and financial behavior as core variables,
Fills the in-depth gap of CFPS/CHARLS/CGSS in household wealth and financial behavior.
Free and open to the public every two years, covering about 40,000 households - it is the preferred micro-data for research on household wealth inequality and real estate in China.

## Research questions suitable for answering/Typical identification strategies
- **The "balance sheet" of Chinese households**: The unique value of CHFS is that it simultaneously measures assets (number of real estate units/market value/financial assets) and liabilities (amounts of various loans/interest rates/terms), and can completely depict the distribution of net worth of households.
- **Housing and Household Behavior**: Proportion of multiple suites, vacancy rate, mortgage-to-income ratio—this information that is not available in other surveys makes CHFS the core data for Chinese real estate research.
- **Entrepreneurship and Financial Constraints**: CHFS has detailed entrepreneurial behavior (industrial and commercial operations) + credit application and approval records → directly measures the causal effect of financial constraints on entrepreneurship.
- **Not suitable for**: health/biomarker research (please use CHARLS), cognition/child development (please use CFPS), social attitudes/values (please use CGSS), agricultural production details (please use RHS).

## Key variables/modules
- **Asset module** (core value): real estate (number of units/area/market value/year of purchase), financial assets (deposits/stocks/funds/financial management/gold/loans), industrial and commercial assets, vehicles, land
- **Liability module** (core value): housing loan (commercial loan/provident fund/interest rate), consumer loan, business loan, credit card, private loan (amount/interest rate/source)
- **Income and Consumption**: wages/business/property/transfer income, eight categories of consumer expenditures
- **Entrepreneurship Module**: Whether to operate industry and commerce, industry, employees, income, source of start-up capital
- **Financial Literacy**: Interest rate calculation, understanding of inflation, understanding of risk diversification
- **Social Security**: Medical insurance type, pension type and amount, minimum living security

## How to get
1. Visit https://chfs.swufe.edu.cn → Register an account.
2. Submit a data use application (research purpose + sign a data use agreement) in the "Data Center".
3. After approval, download all round data in Stata/CSV format. Free.

## Connections to other data
- **CFPS**: Cross-validation of household income/consumption/demographic variables; CFPS covers all ages + education/health depth is better, CHFS asset/liability depth is better → the two complement each other.
- **CHARLS**: CHARLS contains asset/pension information for middle-aged and elderly people 45+, complementary to CHARLS health/biomarkers.
- **Statistical Yearbook**: Use "province/city code" to connect macro indicators such as housing prices, GDP, and financial development.

## Remarks / Pitfalls
- **House market values are self-reported**: Respondents may overestimate or underestimate property market values – be aware of measurement error when doing wealth distribution analyses.
- **Private loans are underreported**: Private loans with high sensitivity (especially loan sharks) may be underreported or refused to answer.
- **The baseline sample size in 2011 was small** (~8,000 households) - in 2013 and subsequent rounds, it was expanded to about 40,000 households, and the early sample loss was large when doing the panel.

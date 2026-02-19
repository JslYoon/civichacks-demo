# Exercise 4: Apply Your Skills (20 minutes)

## Objective

This is a quick creative challenge where you apply what you learned in Exercises 1-3. You have **20 minutes** to customize one of the existing scripts to solve a specific civic problem.

---

## The Challenge

Pick ONE of the four tracks below and complete the corresponding task. All the data you need is already in the `data/` directory.

---

## Track 1: EcoHack - Environment & Climate

**Your Task:** Create an air quality alert system

**What to do:**
1. Modify `exercise2/civic_rag.py` to focus on the EcoHack data
2. Add a function that identifies neighborhoods with dangerous air quality (AQI > 100)
3. Make it output a simple alert message listing affected neighborhoods

**Data source:** `data/ecohack_boston_environment.txt`

**Success looks like:**
```
⚠️  AIR QUALITY ALERT
Neighborhoods with unhealthy air (AQI > 100):
- East Boston: AQI 128 (near airport, high NO2)
- Roxbury: AQI 115 (industrial area)
Recommendation: Limit outdoor activity
```

**In the template:**
1. Set `TRACK = "eco"`
2. Set `QUERY = "Which neighborhoods have the worst air quality and what are the AQI levels?"`
3. Set `REPORT_TITLE = "AIR QUALITY ALERT"`

---

## Track 2: CityHack - Civic Services

**Your Task:** Create an equity report for 311 services

**What to do:**
1. Modify `exercise2/civic_rag.py` to focus on CityHack data
2. Query for neighborhoods with longest response times
3. Compare response times between high-income and low-income neighborhoods
4. Output a simple equity report

**Data source:** `data/cityhack_boston_311.txt`

**Success looks like:**
```
311 SERVICE EQUITY REPORT

Slowest Response Times:
- Roxbury: 8.2 days average
- Mattapan: 7.9 days average

Fastest Response Times:
- Back Bay: 3.1 days average
- Beacon Hill: 2.8 days average

Equity Gap: 2.9x difference between slowest and fastest neighborhoods
Income correlation: Lower-income areas wait 2.5x longer
```

**In the template:**
1. Set `TRACK = "city"`
2. Set `QUERY = "Compare 311 response times between neighborhoods..."`
3. Set `REPORT_TITLE = "311 SERVICE EQUITY REPORT"`

---

## Track 3: EduHack - Education Equity

**Your Task:** Create a student support recommender

**What to do:**
1. Modify `exercise2/civic_rag.py` to focus on EduHack data
2. Identify students at highest risk (chronic absenteeism + low test scores)
3. Suggest specific interventions based on the data
4. Output a support plan

**Data source:** `data/eduhack_boston_schools.txt`

**Success looks like:**
```
STUDENT SUPPORT RECOMMENDATIONS

High-Risk Factors Identified:
- Chronic absenteeism: 18% of students
- Transportation barriers correlate with 2.3x higher absence rates
- Technology access gap: 22% lack home internet

Recommended Interventions:
1. Transportation support for neighborhoods with >15% absenteeism
2. Hotspot distribution for families without home internet
3. Early warning system for students missing 10% of school days
```

**In the template:**
1. Set `TRACK = "edu"`
2. Set `QUERY = "What are the biggest risk factors for student failure..."`
3. Set `REPORT_TITLE = "STUDENT SUPPORT RECOMMENDATIONS"`

---

## Track 4: JusticeHack - Criminal Justice Reform

**Your Task:** Create a bail reform analysis

**What to do:**
1. Modify `exercise2/civic_rag.py` to focus on JusticeHack data
2. Identify racial disparities in pretrial detention and bail amounts
3. Calculate the impact of bail reform on detention rates
4. Output a reform recommendation

**Data source:** `data/justicehack_ma_justice.txt`

**Success looks like:**
```
BAIL REFORM ANALYSIS

Current Disparities:
- Black defendants: $15,000 average bail
- White defendants: $8,500 average bail
- 1.76x disparity ratio

Pretrial Detention:
- 62% of Black defendants held pretrial
- 38% of White defendants held pretrial

Reform Impact:
Eliminating cash bail for non-violent offenses would:
- Reduce pretrial detention by 40%
- Save $12M annually in detention costs
- Reduce racial disparity ratio to 1.1x
```

**In the template:**
1. Set `TRACK = "justice"`
2. Set `QUERY = "What racial disparities exist in bail and pretrial detention..."`
3. Set `REPORT_TITLE = "BAIL REFORM ANALYSIS"`

---

## Instructions

### Step 1: Copy the Template (1 minute)
```bash
cd exercises/exercise4
cp template.py my_civic_tool.py
```

### Step 2: Choose Your Track (2 minutes)
1. Open `my_civic_tool.py` in your editor
2. Find the "STEP 1: CHOOSE YOUR TRACK" section
3. Uncomment your chosen track (eco, city, edu, or justice)

### Step 3: Set Your Query (2 minutes)
1. Find the "STEP 2: SET YOUR CUSTOM QUERY" section
2. Copy the query from your chosen track above
3. Paste it and customize if desired

### Step 4: Run It (10 minutes)
```bash
python my_civic_tool.py
```

Watch the AI analyze your civic data and generate insights!

### Step 5: Customize (5 minutes - optional)
If you finish early:
- Change the `REPORT_TITLE` to customize the output header
- Add follow-up queries in the "STEP 4" section of the template
- Format the output differently

**Optional:** If you finish early:
- Add follow-up queries in the template (see "STEP 4" section)
- Customize the output formatting
- Add multiple queries to get different insights

---

## Tips for Success

**Keep it simple:** The goal is to apply what you learned, not build something complex.

**Focus on one insight:** Don't try to analyze everything. Pick one specific question.

**Use the data:** All the information you need is already in the data files.

**Copy and modify:** Start with working code from Exercise 2, then customize it.

---

## After the Workshop

**This was just practice.** Now you have the skills to build your real hackathon project:

**Next steps for the hackathon:**
1. Find or create data about YOUR community
2. Identify a specific problem to solve
3. Build a solution using the techniques from Exercises 1-4
4. Create a shareable demo (web app or public URL)

**Resources for your hackathon project:**
- [Main README](../../README.md)
- [Presenter Guide](../../USER_GUIDE.md)

---

## Evaluation Criteria (for this exercise)

During the workshop, we'll look for:
- Does it run without errors?
- Does it query the correct dataset?
- Does the output make sense?
- Did you customize it (not just copy-paste)?

**This is practice, not graded.** The goal is learning!

---

## Questions?

- Check [Exercise 2 README](../exercise2/README.md) for RAG reference
- Check [Exercise 3 README](../exercise3/README.md) for web UI reference
- Ask a mentor or teammate
- Review the main [README](../../README.md)

# ==============================
# Agentic AI Data Analysis Assistant
# ==============================

import pandas as pd
import matplotlib.pyplot as plt
import openai
import json

# 🔑 SET YOUR API KEY
openai.api_key = "OPENAI_API_KEY"
# ==============================
# LLM CALL FUNCTION
# ==============================
def llm(prompt):
    # Mock response for testing
    return "Mock analysis plan: run basic stats and plot histograms."

# def llm(prompt):
#     response = openai.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": prompt}],
#     temperature=0.3
# )

    return response.choices[0].message["content"]

# ==============================
# TOOL 1: Inspect Dataset
# ==============================
def inspect_data(df):
    metadata = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict()
    }
    return metadata

# ==============================
# TOOL 2: Agent Planning
# ==============================
def decide_analysis(metadata):
    prompt = f"""
    You are a data analyst agent.
    Based on this dataset metadata, decide what analysis steps should be performed.

    Metadata:
    {json.dumps(metadata, indent=2)}

    Return steps in bullet points.
    """
    return llm(prompt)

# ==============================
# TOOL 3: Statistical Analysis
# ==============================
def run_analysis(df):
    numeric_df = df.select_dtypes(include="number")
    return numeric_df.describe()

# ==============================
# TOOL 4: Visualization
# ==============================
def generate_plots(df):
    numeric_df = df.select_dtypes(include="number")

    for column in numeric_df.columns:
        plt.figure()
        numeric_df[column].hist()
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

# ==============================
# TOOL 5: Insight Generation
# ==============================
def generate_insights(stats):
    prompt = f"""
    Generate clear and meaningful insights from the following statistics.
    Write insights in simple language.

    Statistics:
    {stats.to_string()}
    """
    return llm(prompt)

# ==============================
# TOOL 6: Self-Review (Agent Reflection)
# ==============================
def self_review(insights):
    prompt = f"""
    Review the following insights.
    Are they actionable and useful?
    If not, suggest improvements.

    Insights:
    {insights}
    """
    return llm(prompt)

# ==============================
# AGENT ORCHESTRATION
# ==============================
def data_analysis_agent(csv_path):
    print("\n📥 Loading dataset...")
    df = pd.read_csv(r"C:\Users\Owner\Documents\data engineer\exam-scores.csv")

    print("\n🔍 Inspecting dataset...")
    metadata = inspect_data(df)

    print("\n🧠 Agent planning analysis...")
    plan = decide_analysis(metadata)
    print("\n📌 Agent Plan:\n", plan)

    print("\n📊 Running statistical analysis...")
    stats = run_analysis(df)
    print(stats)

    print("\n📈 Generating plots...")
    generate_plots(df)

    print("\n💡 Generating insights...")
    insights = generate_insights(stats)
    print("\nInsights:\n", insights)

    print("\n🔁 Agent self-review...")
    review = self_review(insights)
    print("\nSelf Review:\n", review)

    print("\n✅ Analysis completed.")

# ==============================
# RUN THE AGENT
# ==============================
if __name__ == "__main__":
    # Replace with your dataset path
    csv_file_path = r"C:\Users\Owner\Documents\data engineer\exam-scores.csv"
    data_analysis_agent(r"C:\Users\Owner\Documents\data engineer\exam-scores.csv")

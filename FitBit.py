import streamlit as st

def progress_bar(metric_name, current_value, goal_value):
    units = {
        "Steps Taken": "steps",
        "Distance Traveled": "miles",
        "Calories Burned": "calories",
        "Minutes Active": "minutes",
        "Sleep Tracking": "hours",
        "Floors Climbed": "floors",
    }
    unit = units[metric_name]
    progress_percent = min(100, (current_value / goal_value) * 100)
    st.write(f"{metric_name}: {current_value} out of {goal_value} {unit}")
    st.progress(progress_percent / 100)

def main():
    st.title(f"Fitness Tracker Progress")
    
    metrics = {
        "Steps Taken": (3000, 10000),
        "Distance Traveled": (2, 6),
        "Calories Burned": (1500, 2000),
        "Minutes Active": (60, 120),
        "Sleep Tracking": (6, 8),
        "Floors Climbed": (10, 20),
    }

    for metric_name, (current_value, goal_value) in metrics.items():
        progress_bar(metric_name, current_value, goal_value)

if __name__ == "__main__":
    main()
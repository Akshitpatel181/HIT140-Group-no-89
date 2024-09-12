import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files into data frames for daily screen time and well-being indicators
daily_digital_screen_time_df = pd.read_csv("dataset2.csv")
well_being_indicators = pd.read_csv("dataset3.csv")

# Aggregate screen time across different activities (communication, gaming, social media, TV)
# Adding up both weekday (wk) and weekend (we) screen time for each respondent
daily_digital_screen_time_df["Total_Screen_Time"] = (
    daily_digital_screen_time_df["C_we"]    # Communication (weekend)
    + daily_digital_screen_time_df["C_wk"]  # Communication (weekday)
    + daily_digital_screen_time_df["G_we"]  # Gaming (weekend)
    + daily_digital_screen_time_df["G_wk"]  # Gaming (weekday)
    + daily_digital_screen_time_df["S_we"]  # Social Media (weekend)
    + daily_digital_screen_time_df["S_wk"]  # Social Media (weekday)
    + daily_digital_screen_time_df["T_we"]  # TV/Streaming (weekend)
    + daily_digital_screen_time_df["T_wk"]  # TV/Streaming (weekday)
)

# Merging the screen time data with well-being data using the 'ID' as the key
# This combines each respondent's screen time with their self-reported well-being
merged_df = pd.merge(
    daily_digital_screen_time_df, well_being_indicators, how="left", on="ID"
)

# Create screen time categories based on the total screen time using predefined bins
# Categories: Very Low (0-1 hours), Low (1-2 hours), Moderate (2-4 hours), High (4-5 hours), Very High (5+ hours)
bins = [0, 1, 2, 4, 5, float("inf")]
labels = ["Very Low", "Low", "Moderate", "High", "Very High"]

# Assigning each respondent to a screen time category based on their total screen time
merged_df["Screen_Time_Category"] = pd.cut(
    merged_df["Total_Screen_Time"], bins=bins, labels=labels
)

# Calculate the mode (most common value) of well-being scores for each screen time category
# Mode is calculated across all the well-being indicators
df_mode_wellbeing = merged_df.groupby("Screen_Time_Category").agg(lambda x: x.mode()[0])

# Selecting the well-being indicators to be used for plotting
columns = [
    "Optm", "Usef", "Relx", "Intp", "Engs", "Dealpr", "Thcklr", "Goodme", 
    "Clsep", "Conf", "Mkmind", "Loved", "Intthg", "Cheer"
]

# Resetting index for easier plotting
df_mode_wellbeing_plot = df_mode_wellbeing.reset_index()[columns]

# Define custom labels for the x-axis to better represent screen time categories
custom_labels = ["Below 1 Hour", "1-2 Hours", "2-4 Hours", "4-5 Hours", "Above 5 Hrs"]

# Create a figure and axis for the bar plot
plt.figure(figsize=(14, 10))
ax = plt.gca()

# Plot the mode well-being responses for each screen time category as a bar graph
df_mode_wellbeing_plot.plot(kind="bar", ax=ax, legend=False)

# Set titles and labels for the plot
plt.title("Mode Well-Being Response by Screen Time Category")
plt.xlabel("Screen Time Category")
plt.ylabel("Self-Reported Well-Being (Mode)")

# Customize the x-axis labels with more descriptive names for the screen time categories
plt.xticks(ticks=range(len(custom_labels)), labels=custom_labels, rotation=0)

# Add a legend to the plot that explains the well-being indicators
# Legend is placed below the plot and divided into four columns for clarity
legend_label = [
    "Optimistic", "Useful", "Feeling Relaxed", "Feeling Interested in Other People",
    "Energy to Spare", "Dealing with Problems Well", "Thinking Clearly", 
    "Feeling Good About Myself", "Feeling Close to Other People", 
    "Feeling Confident", "Making Up My Own Mind About Things", "Feeling Loved", 
    "Interested in New Things", "Feeling Cheerful"
]

plt.legend(legend_label, title="Well-Being Indicators", loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=4)

# Adjust the layout to ensure that everything fits nicely and doesn't overlap
plt.tight_layout()

# Display the plot
plt.show()

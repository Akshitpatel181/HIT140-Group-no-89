import pandas as pd
import matplotlib.pyplot as plt

try:
    divide_by_cohorts = str(
        input("Which cohort you want to analyse among gender, minority and deprived : ")
    )
    if divide_by_cohorts not in ["gender", "minority", "deprived"]:
        raise Exception("You can only enter gender, minority and deprived")

    # Read files and convert them to data frames
    demography_df = pd.read_csv("dataset1.csv")
    daily_digital_screen_time_df = pd.read_csv("dataset2.csv")
    well_being_indicators_df = pd.read_csv("dataset3.csv")

    # Aggregate screen time for each respondent (Weekdays + Weekends)
    daily_digital_screen_time_df["Total_Screen_Time"] = (
        daily_digital_screen_time_df["C_we"]
        + daily_digital_screen_time_df["C_wk"]
        + daily_digital_screen_time_df["G_we"]
        + daily_digital_screen_time_df["G_wk"]
        + daily_digital_screen_time_df["S_we"]
        + daily_digital_screen_time_df["S_wk"]
        + daily_digital_screen_time_df["T_we"]
        + daily_digital_screen_time_df["T_wk"]
    )

    # Merge dataframes
    merged_df = pd.merge(
        demography_df,
        pd.merge(
            daily_digital_screen_time_df, well_being_indicators_df, how="left", on="ID"
        ),
        how="left",
        on="ID",
    )

    cohorts = merged_df[divide_by_cohorts].unique().tolist()

    # Define a figure before the loop to use a single plot
    plt.figure(figsize=(14, 10))
    ax = plt.gca()

    custom_labels = [
        "Below 1 Hour",
        "1-2 Hours",
        "2-4 Hours",
        "4-5 Hours",
        "Above 5 Hrs",
    ]

    # Define fixed colors for each cohort to ensure consistency
    cohort_alpha = {
        0: 0.3,  # cohort 0
        1: 1,  # cohort 1
        # Add more colors if there are more cohorts
    }

    # Loop through the cohorts to plot them
    for cohort in cohorts:
        query_string = f"{divide_by_cohorts} == {cohort}"
        cohort_df = merged_df.query(query_string)

        # Categorize total screen time into groups (Very Low, Low, Moderate, High, Very High)
        bins = [0, 1, 2, 4, 5, float("inf")]
        labels = ["Very Low", "Low", "Moderate", "High", "Very High"]

        cohort_df = cohort_df.copy()
        cohort_df.loc[:, "Screen_Time_Category"] = pd.cut(
            cohort_df["Total_Screen_Time"], bins=bins, labels=labels
        )

        # Calculate the average well-being score for each screen time category
        df_avg_wellbeing = cohort_df.groupby(
            "Screen_Time_Category", observed=False
        ).mean()

        # Select all well-being indicators for plotting
        columns = [
            "Feeling optimistic",
            "Feeling useful",
            "Feeling relaxed",
            "Interested in other people",
            "Had energy to spare",
            "Dealing with problems well",
            "Thinking clearly",
            "Feeling good about myself",
            "Feeling close to other people",
            "Feeling confident",
            "Able to make up my mind about things",
            "Feeling loved",
            "Interested in new things",
            "Feeling cheerful",
        ]
        df_avg_wellbeing_plot = df_avg_wellbeing.reset_index()[columns]

        # Plot the bar graph for well-being indicators for both cohorts
        df_avg_wellbeing_plot.plot(
            kind="bar",
            ax=ax,
            alpha=cohort_alpha[cohort],
            label=f"Cohort: {str(cohort)}",
            legend=True,
        )

    # Add custom labels for the x-axis
    plt.xticks(ticks=range(len(custom_labels)), labels=custom_labels, rotation=0)

    # Set title, xlabel, and ylabel
    plt.title(
        f"Comparison of Well-Being Indicators by Screen Time Category Across {divide_by_cohorts.capitalize()} by using mean"
    )
    plt.xlabel("Screen Time Category")
    plt.ylabel("Self-Reported Well-Being")

    # Set legend to display both the cohort (gender in this case) and well-being indicators
    plt.legend(
        title="Cohort (light-0, dark-1) and Well-Being Indicators",
        loc="upper center",
        bbox_to_anchor=(0.5, -0.15),
        ncol=2,
    )

    # Ensure everything fits well on the plot
    plt.tight_layout()

    # Display the plot
    plt.show()


except Exception as e:
    print(e)
import matplotlib.pyplot as plt
import pandas

# Create dataframe from csv file
honey_df = pandas.read_csv("honey.csv")

# Remove commas
honey_df["Value"] = honey_df["Value"].str.replace(",", "")
# Convert strings in Value column to numbers
honey_df["Value"] = pandas.to_numeric(honey_df["Value"], errors="coerce")
# Drop NaN values
honey_df.dropna(subset=["Value"], inplace=True)

def graph_by_state():
    unique_states = honey_df["State"].unique()

    # Initialize dataframe to represent total honey production for each state
    state_honey_df = pandas.DataFrame(columns=["State", "Total Honey Production"])

    fig, axs = plt.subplots(3, sharex=True)
    fig.suptitle("Honey production by production bracket")

    brackets = [0, 1000000, 4500000]

    all_honey = {}
    
    # all_honey = []
    # all_states = []
    # # without grouping
    # for state in unique_states:
    #     # Get honey data for one state grouped by the year
    #     honey_data = honey_df[honey_df["State"] == state]["Value"]

    #     # Print the state and sum of honey values
    #     print(state, honey_data.sum())
    #     # Add total honey value to the list of values
    #     all_honey.append(honey_data.sum())
    #     # Add state to the list of states
    #     all_states.append(state)

    # with grouping
    for state in unique_states:
        # Get honey data for one state grouped by the year
        honey_data = honey_df[honey_df["State"] == state].groupby("Year")["Value"].sum()
        # Get the list of years
        honey_years = honey_df[honey_df["State"] == state]["Year"].unique()

        # Calculate the total production
        total_production = honey_data.sum()

        # Print the state and sum of honey values
        # print(state, total_production)

        # Add data to the states dataframe
        state_honey_df = pandas.concat([state_honey_df, pandas.DataFrame([state, total_production])])
        
        bracket = -1
        for i in range(len(brackets)):
            if total_production < brackets[i]: break
            bracket += 1

        # Plot the honey data vs the years for the state
        axs[bracket].plot(honey_years, honey_data, label=state)
            
        # Add the total production to the dictionary
        all_honey[state] = total_production

    # Print out a sorted list of total honey productions by state (used to calculate brackets)
    # all_honey = {state : honey for state, honey in sorted(all_honey.items(), key=lambda item: item[1])}
    # for k, v in all_honey.items():
    #     print(f"{k}: {v}")

    plt.ylabel("Annual honey production")
    plt.xlabel("Year")
    for i in range(3):
        axs[i].legend(loc="upper left", bbox_to_anchor=(1, 1))
    plt.show()

def graph_by_years():
    unique_years = honey_df["Year"].unique()

    year_honey_df = pandas.DataFrame(columns=["Year", "Total"])

    for year in unique_years:
        yearly_sum = honey_df[honey_df["Year"] == year].groupby("Year")["Value"].sum().sum()
        sum = pandas.DataFrame({"Year" : year, "Total" : yearly_sum}, index=[0])
        year_honey_df = pandas.concat([year_honey_df, sum])
    
    plt.bar(year_honey_df["Year"], year_honey_df["Total"])
    plt.xlabel("Year")
    plt.ylabel("Annual Honey Production")
    plt.show()

def validate_year(year: int):
    values = honey_df[honey_df["Year"] == year]["Value"]
    sum = 0
    for value in values:
        sum += value
    print(f"{year} sum: {sum}")

# graph_by_years()
# validate_year(2012)
graph_by_state()
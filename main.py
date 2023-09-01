import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    return pd.read_csv(file_path)


def get_job_satisfaction_counts(data_frame):
    return data_frame['JobSatisfaction'].value_counts()


def get_job_satisfaction_counts_by_country(data_frame, country_name):
    country_name = country_name.lower()
    matching_rows = data_frame[data_frame['Country'].str.lower() == country_name]
    satisfaction_counts = matching_rows['JobSatisfaction'].value_counts()
    years_of_experience_counts = matching_rows['YearsCoding'].value_counts()
    return satisfaction_counts, years_of_experience_counts


def plot_satisfaction_and_experience(satisfaction_counts, years_of_experience_counts, country_name):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.bar(satisfaction_counts.index, satisfaction_counts.values, alpha=0.7, color='b', label='Job Satisfaction')
    ax1.set_xlabel('Satisfaction Level')
    ax1.set_ylabel('Count (Job Satisfaction)', color='b')
    ax1.tick_params('y', colors='b')
    plt.xticks(rotation=45)
    ax1.legend(loc='upper left')

    ax2 = ax1.twinx()
    ax2.plot(years_of_experience_counts.index, years_of_experience_counts.values, 'ro-', label='Years of Experience')
    ax2.set_ylabel('Count (Years of Experience)', color='r')
    ax2.tick_params('y', colors='r')
    ax2.legend(loc='upper right')

    plt.title(f'Job Satisfaction and Years of Experience for {country_name.capitalize()}')
    plt.tight_layout()
    plt.show()


def main():
    data_file = 'data3.csv'
    df = load_data(data_file)

    while True:
        print("\nMenu:")
        print("1. View job satisfaction distribution")
        print("2. Search job satisfaction by country name")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            satisfaction_counts = get_job_satisfaction_counts(df)
            print("Job Satisfaction distribution:")
            for satisfaction, count in satisfaction_counts.items():
                print(f'{satisfaction}: {count} people')
            plt.figure(figsize=(10, 6))
            plt.bar(satisfaction_counts.index, satisfaction_counts.values)
            plt.xlabel("Satisfaction Level")
            plt.ylabel("Count")
            plt.title("Job Satisfaction Distribution")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        elif choice == '2':
            country_name = input("Enter the country name to search: ")
            satisfaction_counts, years_of_experience_counts = get_job_satisfaction_counts_by_country(df, country_name)
            if not satisfaction_counts.empty:
                print(f'Data for {country_name.capitalize()}:')
                print("Job Satisfaction distribution:")
                for satisfaction, count in satisfaction_counts.items():
                    print(f'{satisfaction}: {count} people')
                if not years_of_experience_counts.empty:
                    print("Years of Experience distribution:")
                    for experience, count in years_of_experience_counts.items():
                        print(f'{experience}: {count} people')
                    # Plot satisfaction and experience
                    plot_satisfaction_and_experience(satisfaction_counts, years_of_experience_counts, country_name)
                else:
                    print("No data found for Years of Experience.")
            else:
                print(f'No data found for {country_name.capitalize()}')

        elif choice == '3':
            print('Exiting...')
            break

        else:
            print('Invalid choice. Please enter a valid option.')


if __name__ == "__main__":
    main()

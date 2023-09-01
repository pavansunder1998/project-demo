import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    return pd.read_csv(file_path)


def get_job_satisfaction_counts(data_frame):
    return data_frame['JobSatisfaction'].value_counts()


def get_job_satisfaction_counts_by_country(data_frame, country_name):
    # Convert the user input to lowercase for case-insensitive comparison
    country_name = country_name.lower()
    matching_rows = data_frame[data_frame['Country'].str.lower() == country_name]
    satisfaction_counts = matching_rows['JobSatisfaction'].value_counts()
    return satisfaction_counts


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
            plt.bar(satisfaction_counts.index, satisfaction_counts.values)
            plt.xlabel("Job Satisfaction")
            plt.ylabel("Count")
            plt.title("Job Satisfaction Distribution")
            plt.show()

        elif choice == '2':
            country_name = input("Enter the country name to search: ")
            satisfaction_counts = get_job_satisfaction_counts_by_country(df, country_name)
            if not satisfaction_counts.empty:
                print(f'Job Satisfaction distribution for {country_name.capitalize()}:')
                for satisfaction, count in satisfaction_counts.items():
                    print(f'{satisfaction}: {count} people')
            else:
                print(f'No data found for {country_name.capitalize()}')

        elif choice == '3':
            print('Exiting...')
            break

        else:
            print('Invalid choice. Please enter a valid option.')


if __name__ == "__main__":
    main()

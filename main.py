import pandas as pd


def load_data(file_path):
    return pd.read_csv(file_path)


def get_job_satisfaction_counts(data_frame, country_name):
    matching_rows = data_frame[data_frame['Country'] == country_name]
    satisfaction_counts = matching_rows['JobSatisfaction'].value_counts()
    return satisfaction_counts


def main():
    data_file = 'data3.csv'
    df = load_data(data_file)

    while True:
        country_name = input('Enter the country name (or type "exit" to quit): ')

        if country_name.lower() == 'exit':
            print('Exiting...')
            break

        satisfaction_counts = get_job_satisfaction_counts(df, country_name)

        if not satisfaction_counts.empty:
            print(f'Job Satisfaction distribution for {country_name}:')
            for satisfaction, count in satisfaction_counts.items():
                print(f'{satisfaction}: {count} people')
        else:
            print(f'No data found for {country_name}')


if __name__ == "__main__":
    main()

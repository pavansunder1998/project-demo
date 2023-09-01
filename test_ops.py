import pytest
import pandas as pd
from main import load_data, get_job_satisfaction_counts

# Sample data for testing
sample_data = pd.DataFrame({
    'Country': ['Country1', 'Country2', 'Country1', 'Country3'],
    'JobSatisfaction': ['Satisfied', 'Extremely dissatisfied', 'Satisfied', 'Moderately dissatisfied'],
    'YearsCoding': ['3-5 years', '0-2 years', '6-8 years', '3-5 years']
})

def test_load_data(tmp_path):
    # Create a temporary CSV file with test data
    test_data = tmp_path / "test_data.csv"
    sample_data.to_csv(test_data, index=False)

    # Test loading data from the temporary CSV file
    data_frame = load_data(test_data)
    assert isinstance(data_frame, pd.DataFrame)
    assert data_frame.shape == sample_data.shape

def test_get_job_satisfaction_counts():
    satisfaction_counts = get_job_satisfaction_counts(sample_data)
    assert isinstance(satisfaction_counts, pd.Series)
    assert satisfaction_counts['Satisfied'] == 2
    assert satisfaction_counts['Extremely dissatisfied'] == 1
    assert satisfaction_counts['Moderately dissatisfied'] == 1
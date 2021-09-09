# This script provides the formal specification of the study data that will be
# extracted from the Opensafely database

from cohortextractor import (
    StudyDefinition,
    patients,
    codelist,
    codelist_from_csv,
    filter_codes_by_category,
    combine_codelists,
    Measure
)
# NOQA

# Import codelists from codelist.py folder
from codelists import SSRI_codes, LD_codes, Autism_codes

# Define Study time variables
from datetime import datetime
end_date = datetime.today().strftime('%Y-%m-%d')

# Define Study population and variables

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "2019-01-01", "latest": end_date},
        "rate": "uniform",
        "incidence": 0.5,
    },
    population=patients.registered_with_one_practice_between(
        "2019-02-01", end_date
    ),
)
# Set index date
index_date = "2019-01-01"

# Define Medication variables

# Patients who are taking SSRIs
SSRI_cohort = patients.with_these_medications(
    SSRI_codes,
    on_or_before=index_date,
    returning="binary_flag",
    return_expectations={"incidence": 0.5}
)

# Define patient populations

# Patients with a learning disability
learning_disability = patients.with_these_clinical_events(
    LD_codes,
    on_or_before=index_date,
    returning="binary_flag",
    return_expectations={"incidence": 0.5}
)

# Patients with Autism
autism = patients.with_these_clinical_events(
    Autism_codes,
    on_or_before=index_date,
    returning="binary_flag",
    return_expectations={"incidence": 0.5},
)

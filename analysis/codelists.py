# This script fetches all of the codelists identified in codelists.txt

# --- IMPORT STATEMENTS ---

# Import code building blocks from cohort extractor package
from cohortextractor import (codelist, codelist_from_csv, combine_codelists)

# --- CODELISTS ---


# Medication DM&D

# SSRIs
SSRI_codes = codelist_from_csv(
    "codelists/opensafely-selective-serotonin-reuptake-inhibitors-dmd.csv",
    system="snomed",
    column="dmd_id",
    )


# Groups

# Learning disabilities
learning_disability_codes = codelist_from_csv(
  "codelists/nhsd-primary-care-domain-refsets-ld_cod.csv",
  system="snomed",
  column="code",
)

# Autism
autism_codes = codelist_from_csv(
  "codelists/nhsd-primary-care-domain-refsets-autism_cod.csv",
  system="snomed",
  column="code",
)
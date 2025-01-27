import pandas as pd
import pandera as pa
from pandera.typing import Series


class WayneResaGSRP(pa.DataFrameModel):
    license_number: str = pa.Field(nullable=True)
    street_address: str = pa.Field(nullable=True)
    city: str = pa.Field(nullable=True)
    state: str = pa.Field(nullable=True)
    zip_code: str = pa.Field(nullable=True)
    phone_number: str = pa.Field(nullable=True)
    name_on_license: str = pa.Field(nullable=True)
    classrooms: pd.Int64Dtype = pa.Field(nullable=True)
    classrooms_mistar: pd.Int64Dtype = pa.Field(nullable=True)
    seats_mistar: pd.Int64Dtype = pa.Field(nullable=True)
    provider_type: str = pa.Field(nullable=True)
    subrecipient_name: str = pa.Field(nullable=True)
    hub_contact: str = pa.Field(nullable=True)
    cecc: str = pa.Field(nullable=True) # I don't know what this is
    pecc: str = pa.Field(nullable=True) # Same with this
    four_or_five_day_pgrm: str = pa.Field(nullable=True) # This should be int, but failing
    application_type: str = pa.Field(nullable=True)
    transportation_available: str = pa.Field(nullable=True)
    curriculum: str = pa.Field(nullable=True)
    gsrp_quality: str = pa.Field(nullable=True)
    website: str = pa.Field(nullable=True)
    completed_google_form: str = pa.Field(nullable=True)

    class Config:  # type: ignore
        strict = True
        coerce = True


rename = {
    "Completed Google Form 23/24 for MISTAR ": "completed_google_form",
    "# of Classrooms in MISTAR": "classrooms_mistar",
    "# GSRP seats in MISTAR": "seats_mistar",
    "Provider Type\n(TO BE HIDDEN)": "provider_type",
    "Subrecipient Name": "subrecipient_name",
    "Name on License": "name_on_license",
    "Street Address": "street_address",
    "City": "city",
    "State": "state",
    "Zip Code": "zip_code",
    "Phone Number": "phone_number",
    "Hub Contact Name": "hub_contact",
    "CECC": "cecc",
    "PECC": "pecc",
    "# of Classrooms": "classrooms",
    "4 or 5 Day Program ": "four_or_five_day_pgrm",
    "Availability for 23-24SY": "availability_23_24",
    "Application Type\n(Direct to Provider or MISTAR)": "application_type",
    "Transportation Available": "transportation_available",
    "License #": "license_number",
    "Curriculum": "curriculum",
    "Quality Levels: Great Start  to Quality": "gsrp_quality",
    "Website": "website",
}

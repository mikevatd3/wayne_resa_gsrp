import pandera as pa
from pandera.typing import Series


class WayneResaGSRP(pa.DataFrameModel):
    license_number: str = pa.Field()
    street_address: str = pa.Field()
    city: str = pa.Field()
    state: str = pa.Field()
    zip_code: str = pa.Field()
    phone_number: str = pa.Field()
    name_on_license: str = pa.Field()
    classrooms: str = pa.Field()
    classrooms_mistar: str = pa.Field()
    seats_mistar: str = pa.Field()
    provider_type: str = pa.Field()
    subrecipient_name: str = pa.Field()
    hub_contact: str = pa.Field()
    cecc: str = pa.Field() # I don't know what this is
    pecc: str = pa.Field() # Same with this
    four_or_five_day_pgrm: str = pa.Field()
    application_type: str = pa.Field()
    transportation_available: str = pa.Field()
    curriculum: str = pa.Field()
    gsrp_quality: str = pa.Field()
    website: str = pa.Field()
    completed_google_form: str = pa.Field()

    class Config:  # type: ignore
        strict = True
        coerce = True

    @pa.check("description")
    def max_nulls(cls, description: Series[str]) -> bool:
        """
        It's okay for some of these to be null, but if there are too many
        it could indicate a problem.
        """
        return description.isna().sum() < 200


rename = {
    "Completed Google Form 23/24 for MISTAR": "completed_google_gorm",
    "# of Classrooms in MISTAR": "classrooms_mistar",
    "# GSRP seats in MISTAR": "seats_mistar",
    "Provider Typ (TO BE HIDDEN)": "provider_type",
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
    "Application Typ": "application_type",
    "Transportation Available": "transportation_available",
    "License #": "license_number",
    "Curriculum": "curriculum",
    "Quality Levels: Great Start  to Quality": "gsrp_quality",
    "Website": "website",
}

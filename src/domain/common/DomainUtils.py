import re


class DomainUtils:

    DNI_PATTERN = re.compile(r"^\d{8,10}$")
    EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9+_.-]+@(.+)$")
    PHONE_NUMBER_PATTERN = re.compile(r"^\d{10}$")
    LICENCE_PLATE_FORMAT = re.compile(r"^[A-Z]{3}\d{3}$")


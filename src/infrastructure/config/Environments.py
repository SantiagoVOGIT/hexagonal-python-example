from src.common.decorators.UtilityClass import utilityClass


@utilityClass
class Environments:

    __PRODUCTION: str = "production"
    __TESTING: str = "testing"
    __DEVELOPMENT: str = "development"
    __PRODUCTION_URL_FR: str = "https://example.com"
    __TESTING_URL_FR: str = "https://example.com"
    __DEVELOPMENT_URL_FR: str = "http://localhost:4200"

    @staticmethod
    def getCurrentEnvironment():
        return Environments.__PRODUCTION

    @staticmethod
    def getCurrentUrlFr():
        return Environments.__PRODUCTION_URL_FR

from typing import List, Dict, Any, Optional

from src.common.decorators.UtilityClass import utilityClass


@utilityClass
class StringUtils:

    @staticmethod
    def capitalizeFirstLetter(text: str) -> str:
        if not text:
            return ""
        return text[0].upper() + text[1:]

    @staticmethod
    def reverseString(text: str) -> str:
        if not text:
            return ""
        return text[::-1]

    @staticmethod
    def countOccurrences(text: str, substring: str) -> int:
        if not text or not substring:
            return 0
        return text.count(substring)

    @staticmethod
    def removeWhitespace(text: str) -> str:
        if not text:
            return ""
        return ''.join(text.split())

    @staticmethod
    def splitStringToList(text: str, delimiter: str = ',') -> List[str]:
        if not text:
            return []
        return text.split(delimiter)

    @staticmethod
    def joinListToString(strList: List[str], delimiter: str = ',') -> str:
        return delimiter.join(strList)

    @staticmethod
    def replaceSubstring(text: str, oldSubstring: str, newSubstring: str) -> str:
        if not text or not oldSubstring:
            return text
        return text.replace(oldSubstring, newSubstring)

    @staticmethod
    def isPalindrome(text: str) -> bool:
        if not text:
            return False
        cleanText: str = ''.join(char.lower() for char in text if char.isalnum())
        return cleanText == cleanText[::-1]

    @staticmethod
    def extractDictionary(text: str) -> Dict[str, Any]:
        if not text:
            return {}

        result: Dict[str, Any] = {}
        pairs: List[str] = text.split(',')

        for pair in pairs:
            if ':' not in pair:
                continue
            key, value = pair.split(':')
            result[key.strip()] = value.strip()

        return result

    @staticmethod
    def formatString(template: str, **kwargs: Any) -> str:
        if not template:
            return ""
        return template.format(**kwargs)

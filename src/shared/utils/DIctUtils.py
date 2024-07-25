from typing import Dict, Any, List, Union


class DictUtils:

    __EMPTY_DICT: Dict[Any, Any] = {}
    __originalDict: Dict[Any, Any] = None
    __modifiedDict: Dict[Any, Any] = None

    def __init__(self, inputDict: Dict[Any, Any]):
        self.__originalDict = inputDict.copy()
        self.__modifiedDict = inputDict.copy()

    def getOriginalDict(self) -> Dict[Any, Any]:
        return self.__originalDict.copy()

    def getModifiedDict(self) -> Dict[Any, Any]:
        return self.__modifiedDict.copy()

    def setModifiedDict(self, newDict: Dict[Any, Any]) -> None:
        self.__modifiedDict = newDict.copy()

    def mergeDict(self, otherDict: Dict[Any, Any]) -> None:
        self.__modifiedDict.update(otherDict)

    def removeKey(self, key: Any) -> None:
        if key not in self.__modifiedDict:
            return
        del self.__modifiedDict[key]

    def getNestedValue(self, keys: List[Any]) -> Union[Any, None]:
        currentDict = self.__modifiedDict
        for key in keys:
            if not isinstance(currentDict, dict) or key not in currentDict:
                return None
            currentDict = currentDict[key]
        return currentDict

    def setNestedValue(self, keys: List[Any], value: Any) -> None:
        currentDict = self.__modifiedDict
        for key in keys[:-1]:
            if key not in currentDict:
                currentDict[key] = {}
            currentDict = currentDict[key]
        currentDict[keys[-1]] = value

    def flattenDict(self) -> Dict[str, Any]:
        return self.__flattenDictRecursive(self.__modifiedDict)

    def __flattenDictRecursive(self, inputDict: Dict[Any, Any], prefix: str = '') -> Dict[str, Any]:
        result = {}
        for key, value in inputDict.items():
            newKey = f"{prefix}.{key}" if prefix else str(key)
            if isinstance(value, dict):
                result.update(self.__flattenDictRecursive(value, newKey))
            else:
                result[newKey] = value
        return result

    @staticmethod
    def isEmptyDict(inputDict: Dict[Any, Any]) -> bool:
        return inputDict == DictUtils.__EMPTY_DICT

    @staticmethod
    def getDictKeys(inputDict: Dict[Any, Any]) -> List[Any]:
        return list(inputDict.keys())

    @staticmethod
    def getDictValues(inputDict: Dict[Any, Any]) -> List[Any]:
        return list(inputDict.values())

    @staticmethod
    def buildExtensiveDict(keys: List[Any], values: List[Any]) -> Dict[Any, Any]:
        return dict(zip(keys, values))

    @staticmethod
    def buildDict(key: Any, value: Any) -> Dict[Any, Any]:
        return {key: value}

    @staticmethod
    def buildSimpleDict(value):
        return {"message": value}

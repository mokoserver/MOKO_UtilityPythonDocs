import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO


# EN: Here are the SET commands for the CSMInfo utility
# RU: Тут собраны SET команды для утилиты CSMInfo
# 1) EN: Command initialization APPA207 driver
#    RU: Команда инициализации драйвера APPA207

MOKO.Utility("CSMInfo", "set", "Settings")
MOKO.Utility("CSMInfo", "set", "info")


# EN: Here are the GET commands for the APPA207 driver
# RU: Тут собраны GET команды для драйвера APPA207
# 1) EN: This command reads the value from the APPA207 and returns it as a string
#    RU: Данная команда считывает значение из прибора APPA207 и возвращает его в строчном виде

################################### INFO ##############################################################

RegistrationID = MOKO.Utility("CSMInfo", "get", "RegistrationID", "string")
cipher = MOKO.Utility("CSMInfo", "get", "cipher", "string")
IMEI = MOKO.Utility("CSMInfo", "get", "IMEI", "string")
ND = MOKO.Utility("CSMInfo", "get", "ND", "string")
methods = MOKO.Utility("CSMInfo", "get", "methods", "string")
start_test_date = MOKO.Utility("CSMInfo", "get", "start_test_date", "string")
completion_test_date = MOKO.Utility("CSMInfo", "get", "completion_test_date", "string")
T_nom = MOKO.Utility("CSMInfo", "get", "T_nom", "string")
fi_nom = MOKO.Utility("CSMInfo", "get", "fi_nom", "string")
P_nom = MOKO.Utility("CSMInfo", "get", "P_nom", "string")

############################### SETTINGS ##############################################################

SampleNumber = MOKO.Utility("CSMInfo", "get", "SampleNumber", "string")
TestNumber = MOKO.Utility("CSMInfo", "get", "TestNumber", "string")
EnvironmentalConditions = MOKO.Utility("CSMInfo", "get", "EnvironmentalConditions", "string")
PowerSupply = MOKO.Utility("CSMInfo", "get", "PowerSupply", "string")
SourceVoltage = MOKO.Utility("CSMInfo", "get", "SourceVoltage", "string")
CallModeSignal = MOKO.Utility("CSMInfo", "get", "CallModeSignal", "string")
authentication = MOKO.Utility("CSMInfo", "get", "authentication", "string")
SimCard = MOKO.Utility("CSMInfo", "get", "SimCard", "string")
NumberOfMeasurements = MOKO.Utility("CSMInfo", "get", "NumberOfMeasurements", "string")
CallModeToneModem = MOKO.Utility("CSMInfo", "get", "CallModeToneModem", "string")
ToneModemIterations = MOKO.Utility("CSMInfo", "get", "ToneModemIterations", "string")
VISAadress = MOKO.Utility("CSMInfo", "get", "VISAadress", "string") # аналогичный результат при отправке комманд adress или VISA
InputAttenuation = MOKO.Utility("CSMInfo", "get", "InputAttenuation", "string") # аналогичный результат при отправке комманды InputAtt
OutputAttenuation = MOKO.Utility("CSMInfo", "get", "OutputAttenuation", "string") # аналогичный результат при отправке комманды OutputAtt
CallReleaseType = MOKO.Utility("CSMInfo", "get", "CallReleaseType", "string")
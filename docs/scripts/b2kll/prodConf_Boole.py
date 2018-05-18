from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/Boole/Default.py')
importOptions('$APPCONFIGOPTS/Boole/DataType-2012.py')
importOptions('$APPCONFIGOPTS/Boole/Boole-SiG4EnergyDeposit.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20130929-1',
    InputFiles=['00012345_00006789_1.sim'],
    AppVersion='v26r3',
    XMLSummaryFile='summaryGauss.xml',
    Application='Boole',
    OutputFilePrefix='00012345_00006789_1',
    RunNumber=5678,
    XMLFileCatalog='pool_xml_catalogBoole.xml',
    FirstEventNumber=1234,
    CondDBTag='sim-20130522-1-vc-mu100',
    OutputFileTypes=['digi']
)

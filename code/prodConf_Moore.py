from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/Moore/MooreSimProductionWithL0Emulation.py')
importOptions('$APPCONFIGOPTS/Conditions/TCK-0x409f0045.py')
importOptions('$APPCONFIGOPTS/Moore/DataType-2012.py')
importOptions('$APPCONFIGOPTS/L0/L0TCK-0x0045.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20130929-1',
    InputFiles=['00012345_00006789_1-1ev.digi'],
    AppVersion='v14r8p1',
    XMLSummaryFile='summaryMoore.xml',
    Application='Moore',
    OutputFilePrefix='00012345_00006789_2',
    XMLFileCatalog='pool_xml_catalogBoole.xml',
    CondDBTag='sim-20130522-1-vc-mu100',
    OutputFileTypes=['digi']
)

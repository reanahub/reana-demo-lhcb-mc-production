from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/DaVinci/DV-Stripping20-Stripping-MC-NoPrescaling.py')
importOptions('$APPCONFIGOPTS/DaVinci/DataType-2012.py')
importOptions('$APPCONFIGOPTS/DaVinci/InputType-DST.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py') 

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20130929-1',
    InputFiles=['00012345_00006789_2.dst'],
    AppVersion='v32r2p1',
    XMLSummaryFile='summaryBrunel.xml',
    Application='DaVinci',
    OutputFilePrefix='ALLSTREAMS',
    XMLFileCatalog='pool_xml_catalogBrunel.xml',
    CondDBTag='sim-20130522-1-vc-mu100',
    OutputFileTypes=['dst']
)

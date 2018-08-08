from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/Brunel/DataType-2012.py')
importOptions('$APPCONFIGOPTS/Brunel/MC-WithTruth.py')
importOptions('$APPCONFIGOPTS/Persistency/DST-multipleTCK-2012.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20130929-1',
    InputFiles=['00012345_00006789_2.digi'],
    AppVersion='v43r2p11',
    XMLSummaryFile='summaryBrunel.xml',
    Application='Brunel',
    OutputFilePrefix='00012345_00006789_2',
    XMLFileCatalog='pool_xml_catalogBrunel.xml',
    CondDBTag='sim-20130522-1-vc-mu100',
    OutputFileTypes=['dst']
)

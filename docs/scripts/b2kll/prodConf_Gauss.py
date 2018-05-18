from Gaudi.Configuration import importOptions

eventType = 12125101

importOptions('$APPCONFIGOPTS/Gauss/Sim08-Beam4000GeV-mu100-2012-nu2.5.py')
importOptions('$DECFILESROOT/options/12125101.py')
importOptions('$LBPYTHIA8ROOT/options/Pythia8.py')
importOptions('$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20130929-1',
    AppVersion='v45r10p1',
    XMLSummaryFile='summaryGauss.xml',
    Application='Gauss',
    OutputFilePrefix='00012345_00006789_1',
    RunNumber=5678,
    XMLFileCatalog='pool_xml_catalogGaussv.xml',
    FirstEventNumber=1234,
    CondDBTag='sim-20130522-1-vc-mu100',
    OutputFileTypes=['sim']
)

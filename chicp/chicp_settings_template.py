from collections import OrderedDict

''' details of all snp tracks and configuration for elastic indicies for snp track '''
CHICP_IDX = OrderedDict([
    ('userdata', {'NAME': 'User Data', 'INDEX': 'cp:hg19_userdata_bed', 'DATA_TYPE': 'log10p', 'TRACKS':
                  OrderedDict([
                               ])
                  }
     ),
    ('ic', {'NAME': 'ImmunoChip', 'INDEX': 'idx_name', 'DATA_TYPE': 'log10p', 'TRACKS':
            OrderedDict([
                         ])
            }
     ),
    ('gwas', {'NAME': 'GWAS Statistics', 'INDEX': 'cp:hg19_gwas_bed', 'DATA_TYPE': 'log10p', 'TRACKS':
              OrderedDict([
                           ('gwas-barrett', {'NAME': 'T1D - Barrett et al.', 'TYPE': 't1d_barrett'}),
                         ])
              }
     ),
    ('pmi', {'NAME': 'PMI Data', 'INDEX': 'idx_name', 'DATA_TYPE': 'ppi', 'TRACKS':
             OrderedDict([
                          ])
             }
     )
    ])

sampleLookup = {}

stateLookup = {}

DEFAULT_TARGET = 'cp:hg19_mifsud_chicago_pm'
DEFAULT_TISSUE = 'CD34'
DEFAULT_TRACK = 'gwas-barrett'
DEFAULT_FRAG = 'hg19_restriction_sites/hindiii'
CP_GENE_IDX = 'cp:hg19_gene_details'

TARGET_IDXS = {'cp:hg19_mifsud_chicago_pm': 'Mifsud'}

STUDY_DEFAULTS = {'log10p': {'min': 1, 'snpCutoff': 7.03, 'score_text': "P Value (-log10)"},
                  'ppi': {'min': 0.001, 'snpCutoff': 0.1, 'score_text': "PPI Score"}}

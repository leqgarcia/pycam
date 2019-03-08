#!/bin/env python

import genClasses
from pprint import pprint as pp

# import genClasses
# import os
# from genClasses import g
# from pprint import pprint as pp
#
#
# class di_interface(object):
#     def __init__(self):
#         if os.environ.has_key('JOB'):
#             self.job = genClasses.Job(os.environ['JOB'])
#         else:
#             g.PAUSE('You need to open a job first')
#             print g.STATUS
#             exit(0)
#
#     def layer_list(self):
#
#         matrix = self.job.matrix.info
#
#         gROWcontext = matrix['gROWcontext']
#         gROWlayer_type = matrix['gROWlayer_type']
#         gROWname = matrix['gROWname']
#
#         work_list = []
#         reqd_types = ['drill',
#                       'solder_mask',
#                       'mixed', 'power_ground', 'signal']
#
#         for i in range(len(gROWname)):
#             if gROWcontext[i] == 'board':
#                 if gROWlayer_type[i] in reqd_types:
#                     color = self.job.colors['hex'][gROWlayer_type[i]]
#                     work_list.append(
#                         [gROWname[i],
#                          gROWlayer_type[i],
#                          color]
#                     )
#         return work_list


class DiInterface(object):
    def __init__(self, gen_job):
        self.job = genClasses.Job
        if True:
            self.job = gen_job

        self.get_rows = [
            ['drill', 'drill', '9BB4BF'],
            ['csm', 'solder_mask', '00A57C'],
            ['l1comp', 'mixed', 'F2E086'],
            ['l2pp', 'power_ground', 'DBAD00'],
            ['l3sig', 'signal', 'FCC64D'],
            ['l4pp', 'power_ground', 'DBAD00'],
            ['l5sig', 'signal', 'FCC64D'],
            ['l6pp', 'power_ground', 'DBAD00'],
            ['l7sig', 'signal', 'FCC64D'],
            ['l8pp', 'power_ground', 'DBAD00'],
            ['l9sig', 'signal', 'FCC64D'],
            ['l10pp', 'power_ground', 'DBAD00'],
            ['l11pp', 'power_ground', 'DBAD00'],
            ['l12pp', 'power_ground', 'DBAD00'],
            ['l13pp', 'power_ground', 'DBAD00'],
            ['l14pp', 'power_ground', 'DBAD00'],
            ['l15pp', 'power_ground', 'DBAD00'],
            ['l16sig', 'signal', 'FCC64D'],
            ['l17pp', 'power_ground', 'DBAD00'],
            ['l18sig', 'signal', 'FCC64D'],
            ['l19pp', 'power_ground', 'DBAD00'],
            ['l20sold', 'mixed', 'F2E086'],
            ['ssm', 'solder_mask', '00A57C'],
            ['drill20-19', 'drill', '9BB4BF'],
            ['drill19-16', 'drill', '9BB4BF'],
            ['drill19-18', 'drill', '9BB4BF'],
            ['drill19-17', 'drill', '9BB4BF'],
            ['d60mb16-19', 'drill', '9BB4BF'],
            ['mvonly1-20', 'drill', '9BB4BF'],
            ['csink-bot', 'drill', '9BB4BF']
        ]
        self.cases = [
            "0. N/A",
            "1. Inner Layer DI Fiducial Targets",
            "2. Outer Layer DI Targets",
            "3. Sub-Outer Layer DI Targets for Laser/CDD stacked vias",
            "4. Outer Layers DI Targets for COMBO: drill + drill vf",
            "5. Outer Layers DI Targets for COMBO: drill + Laser",
            "6. Outer Layers DI Tgs for triple COMBO: drill + vf + Laser",
            "7. Solder Msk / Sel Gold DI Targets",
            "8. Jobs with no targets or DI targets"
        ]

    def get_di_layers(self):

        matrix = self.job.matrix.info

        gROWcontext = matrix['gROWcontext']
        gROWlayer_type = matrix['gROWlayer_type']
        gROWname = matrix['gROWname']

        work_list = []
        reqd_types = ['drill',
                      'solder_mask',
                      'mixed', 'power_ground', 'signal']

        for i in range(len(gROWname)):
            if gROWcontext[i] == 'board':
                if gROWlayer_type[i] in reqd_types:
                    color = self.job.colors['hex'][gROWlayer_type[i]]
                    work_list.append(
                        [gROWname[i],
                         gROWlayer_type[i],
                         color]
                    )
        return work_list

    def read_di_trg_params(self):
        data = self.job.bucket.get("app_6_1_data")

        if type(data) is not dict:
            print "Not A Dict"
            return None

        return data

    def save_di_trg_params(self, di_params):

        # pp(di_params)
        self.job.bucket.put(di_params, "app_6_1_data", True)

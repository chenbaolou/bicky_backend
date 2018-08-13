# -*- coding: utf-8 -*-

import math
import psutil

# Define the history items list
# All items in this list will be historised if the --enable-history tag is set
items_history_list = [{'name': 'percent',
                       'description': 'RAM memory usage',
                       'y_unit': '%'}]


class GlancesMem(object):

    def get(self):
        vm_stats = psutil.virtual_memory()
        stats = {}
        for mem in ['total', 'available', 'percent', 'used', 'free',
                    'active', 'inactive', 'buffers', 'cached',
                    'wired', 'shared']:
            if hasattr(vm_stats, mem):
                stats[mem] = getattr(vm_stats, mem)

        # Use the 'free'/htop calculation
        # free=available+buffer+cached
        stats['free'] = stats['available']
        if hasattr(stats, 'buffers'):
            stats['free'] += stats['buffers']
        if hasattr(stats, 'cached'):
            stats['free'] += stats['cached']
        # used=total-free
        stats['used'] = stats['total'] - stats['free']

        total = stats['total']
        # M
        total = math.ceil(total / 1024 / 1024)
        stats['totalFormat'] = '%sM' % (total)

        # G
        if total > 1024:
            total = total / 1024
            total = round(total)
            stats['totalFormat'] = '%sG' % (total)

        return stats

glances_mem = GlancesMem()

from powerline_shell.utils import BasicSegment
from kubernetes import K8sConfig
import os

_KUBE_SYMBOL = u'\U00002388 '

## Set the following environment variables to configure:
## K8S_ALERT_NAMESPACES:
##  - comma-separated list of namespaces to highlight if we are using them

ALERT_FG = 9
ALERT_BG = 235

SAFE_FG = 10
SAFE_BG = 235

NORMAL_FG = 69
NORMAL_BG = 237

CLUSTER_FG = 117
CLUSTER_BG = 235

class Segment(BasicSegment):
    def add_to_powerline(self):
        if not os.getenv('KUBECONFIG'):
            return

        try:
            alert_clusters = os.getenv("K8S_ALERT_CLUSTERS").split(',')
        except:
            alert_clusters = []

        try:
            safe_clusters = os.getenv("K8S_SAFE_CLUSTERS").split(',')
        except:
            safe_clusters = []

        context = K8sConfig().current_context_dict

        # user = context.get('user')
        # seg = f'{_KUBE_SYMBOL}{user}@'
        # seg = f'{_KUBE_SYMBOL}'
        # self.powerline.append(seg, NORMAL_FG, NORMAL_BG, separator='')

        cluster = context.get('cluster')
        namespace = context.get('namespace')
        if not namespace:
            namespace = 'default'

        ns = f'({namespace})'

        if cluster in alert_clusters:
            fg = ALERT_FG
            bg = ALERT_BG
        elif cluster in safe_clusters:
            fg = SAFE_FG
            bg = SAFE_BG
        else:
            fg = CLUSTER_FG
            bg = CLUSTER_BG

        self.powerline.append(cluster, fg, bg)
        self.powerline.append(ns, fg, bg)


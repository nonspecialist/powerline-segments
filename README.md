# powerline-segments

## kubernetes.py

Add a segment to reveal current kubernetes user, cluster and namespace; highlight clusters
and namespaces that are "important" through colour

### Configuration

Set the following environment variables:

* `KUBECONFIG` -- define the file (usually under `$HOME/.kube`) which holds the config for the kubernetes
  cluster that this shell will reference
* `K8S_ALERT_CLUSTERS` -- comma-separated list of cluster names to highlight in the segment (using `ALERT_FG` and
  `ALERT_BG` colours)


# logging_graylog

An example logs delivery to _Graylog_.

Usage:
------

Create input _Raw/Plaintext TCP_ and extractors on _Graylog_ server.

Replace _Host_ and _Port_ parameters to your _Graylog_ server in _helm/values.yaml_

    $ minikube start -p gray
    $ kubectl create ns gray
    $ cd docker
    $ ./build_minikube
    $ cd ../helm
    $ helm dependencies build gray
    $ helm install gray gray --namespace gray

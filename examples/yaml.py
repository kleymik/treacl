from treacl import Treacl as tcl
import utils.util as ut

# random snippet of YAML - equivalent representation using treacl

def sample_kub():

    # treacl version of the above snippet:
    kubConfig = tcl()
    kubConfig.apiVersion = "apps/v1"
    kubConfig.kind       = "Deployment"
    kubConfig.metadata.name = "rss-site"
    kubConfig.metadata.labels.app = "web"
    kubConfig.spec.replicas = 2
    kubConfig.spec.selector.matchLabels.app = "web"
    kubConfig.spec.template.metadata.labels.app = "web"
    kubConfig.spec.template.spec.containers = [tcl(), tcl()]
    kubConfig.spec.template.spec.containers[0].name  = "front-end"
    kubConfig.spec.template.spec.containers[0].image = "nginx"
    kubConfig.spec.template.spec.containers[0].ports.containerPort = 80
    kubConfig.spec.template.spec.containers[1].name  = "rss-reader"
    kubConfig.spec.template.spec.containers[1].image = "johnsmith/rss-php-nginx:v1"
    kubConfig.spec.template.spec.containers[1].ports.containerPort = 88

    return kubConfig


if __name__ == '__main__':

    # random snippet of YAML - to illustrate conversion to treacl

    yaml_kub = '''
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rss-site
  labels:
    app: web
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: front-end
          image: nginx
          ports:
            - containerPort: 80
        - name: rss-reader
          image: johnsmith/rss-php-nginx:v1
          ports:
            - containerPort: 88
'''

    print("Sample person in YAML:")
    print(yaml_kub)

    treacl_kub = sample_kub()
    print("Sample person from TREACL:")
    print()
    treacl_kub.pptree()

    with open("./tests/yaml.gml",'w') as f:
        asGml = ut.paths_to_gml(treacl_kub.tree_nodes_to_list())
        for l in asGml: print(l, file=f)

    print("Done")











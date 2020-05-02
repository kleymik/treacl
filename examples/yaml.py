from treacl import Treacl as tcl

# for testing

def test_2_yaml():

    # random snippet of YAML - to illustrate conversion to treacl:
    #
    #   apiVersion: apps/v1
    #   kind: Deployment
    #   metadata:
    #     name: rss-site
    #     labels:
    #       app: web
    #   spec:
    #     replicas: 2
    #     selector:
    #       matchLabels:
    #         app: web
    #     template:
    #       metadata:
    #         labels:
    #           app: web
    #       spec:
    #         containers:
    #           - name: front-end
    #             image: nginx
    #             ports:
    #               - containerPort: 80
    #           - name: rss-reader
    #             image: nickchase/rss-php-nginx:v1
    #             ports:
    #               - containerPort: 88

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
    kubConfig.spec.template.spec.containers[1].image = "nickchase/rss-php-nginx:v1"
    kubConfig.spec.template.spec.containers[1].ports.containerPort = 88


if __name__ == '__main__':

    test_1_config()

    test_2_universe()

    test_eg_3()

    print("test: find Paths")
    for p in univ.findPaths("lead"): print(p)

    if False:
        # path expressions
        config.findPaths("*")                    ## all paths
        config.findPaths("config*")              ## all paths starting "config"
        config.findPaths("*config")              ## all paths ending "config"
        config.findPaths("*config*")             ## all paths containing "config"
        config.findPaths("*config*bar*")         ## all paths containing "config" followed by "bar"
        config.findPaths("*[[A-Z]]*")            ## all paths containing regexp "[A-Z]"
        config.findPaths("*[[A-Z]]*")            ## all paths containing regexp "[A-Z]*"
        config.findPaths("*a:=config*a*")        ## all paths containing regexp "[A-Z]*"
        config.findPaths("*.config.*")           ## all paths with a branch exactly "config"
        config.findPaths("*ForAll().Exists*a*")  ## all paths containing regexp "[A-Z]*"

    print("Done")


    # univ.addProp('role','The Big One')






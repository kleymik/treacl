
# Table of Contents

-   [introduction](#org85f1c15)
    -   [yaml markdown equivalence example](#org84b0b1f)
-   [the gist](#orgba25810)
-   [examples](#org50ccbd0)
-   [acknowledgements / related](#org5ac9db4)
    -   [see also](#orgb085b91)
-   [Requires](#orgae81aab)
-   [Notes](#orge71c885)
-   [TBD](#orgf225bdf)

(the README.org best viewed raw or in org-mode)

Treacl - simple examples which exploit making class instances' attributes dynamic


<a id="org85f1c15"></a>

# introduction

Treacl is a versatile but very simple Python class which supports exploiting dynamic attributes for
creating trees and directed graphs.

In regular Python, though a *first* level attribute will be dynamically added to an instance of a
class (e.g. "foo.aa = 1"), it will fail when attempting more than one level ("foo.aa.bb.cc = 1").
Treacl enables this by defaulting to automatically assign the intermediate attributes with a new empty
Treacl class instance as value:

    from treacl import Treacl

    foo = Treacl()                # an instance of the class Treacl
    foo.xx = 1                    # nothing new, just default Python class instance behaviour
    foo.aa.bb.cc.dd.ee = 1        # for each attribute down the dot-path expression chain except the last (".ee"),
                                  # an instance of the Treacl class is dynamically created
    foo.aa.qq.rr = "Hello World"

    foo.pptree()                  # pretty print the tree
    foo.tree_paths_to_list()      # return all paths in the tree

By a simple tweak of one of the class' dunder methods, it's possible to make object attributes
on-the-fly. This enables tree creation that is declarative, dynamic, and concise.

The ability to write such declarative code segments can often be preferable to the use of markdown
variants such as YAML (= Yaml Ain't Markdown Language), if only because having yet another
declarative language is unwarranted, Python will do fine. Sometimes it's even better: YAML doesn't
admit comments, Python does.

Though the same could be implemented in a class with an attribute containing a dict, the advantage
of the approach here is that the natural and readable Python "."  dot operator for attributes is
kept pre-eminent.


<a id="org84b0b1f"></a>

## yaml markdown equivalence example


          YAML                                          Python- Treacl
          ====                                          ==============

                                                        kubConfig = Treacl()
          apiVersion: apps/v1                           kubConfig.apiVersion = "apps/v1"
          kind: Deployment                              kubConfig.kind       = "Deployment"
          metadata:                                     kubConfig.metadata.name = "rss-site"
            name: rss-site                              kubConfig.metadata.labels.app = "web"
            labels:                                     kubConfig.spec.replicas = 2
              app: web                                  kubConfig.spec.selector.matchLabels.app = "web"
          spec:                                         kubConfig.spec.template.metadata.labels.app = "web"
            replicas: 2                                 kubConfig.spec.template.spec.containers = [Treacl()]
            selector:                                   kubConfig.spec.template.spec.containers[0].name  = "front-end"
              matchLabels:                              kubConfig.spec.template.spec.containers[0].image = "nginx"
                app: web                                kubConfig.spec.template.spec.containers[0].ports.containerPort = 80
            template:                                   kubConfig.spec.template.spec.containers += [Treacl()]
              metadata:                                 kubConfig.spec.template.spec.containers[1].name  = "rss-reader"
                labels:                                 kubConfig.spec.template.spec.containers[1].image = "nickchase/rss-php-nginx:v1"
                  app: web                              kubConfig.spec.template.spec.containers[1].ports.containerPort = 88
              spec:
                containers:
                  - name: front-end
                    image: nginx
                    ports:
                      - containerPort: 80
                  - name: rss-reader
                    image: nickchase/rss-php-nginx:v1
                    ports:
                      - containerPort: 88

    >>> kubConfig.pptree()

    apiVersion: 'apps/v1'
    kind: 'Deployment'
    metadata:
        name: 'rss-site'
        labels:
            app: 'web'
    spec:
        replicas: 2
        selector:
            matchLabels:
                app: 'web'
        template:
            metadata:
                labels:
                    app: 'web'
            spec:
                containers:
                    name: 'front-end'
                    image: 'nginx'
                    ports:
                        containerPort: 80

                    name: 'rss-reader'
                    image: 'johnsmith/rss-php-nginx:v1'
                    ports:
                        containerPort: 88


<a id="orgba25810"></a>

# the gist

Treacl is a one-liner - implemented by overriding the <span class="underline"><span class="underline">getattr</span></span> class method in Python so that it
defaults to initialising a new attribute in the instance of the class (i.e. self) with a value that
is a new empty instance of *this same class*.  In this sense, Treacl is "dynamically recursive".

    class Treacl(object):
        "Treacl: a tree class"

       def __getattr__(self, name):
            "only called for undefined attributes"
            setattr(self, name, t := Treacl())             # I am the walrus
            return t

That's it.


<a id="org50ccbd0"></a>

# examples

./treacl/examples:

-   `configuration.py`  - just a simple sample configuration expressed using treacl
-   `yaml.py`           - sample yaml converted to equivalent treacl
-   `xml.py`            - sample xml converted to equivalent treacl
-   `json.py`           - sample json converted to equivalent treacl
-   `ssl_x509_cert.py`  - deconstruction of a TLS certificate

-   `divide_by_7.py`    - traversal of small graph to determine if divisible by 7
-   `table.py`          - quirky representation of a table/matrix as a DAG using treacl

-   `standard_model.py` - particle physics, gluons, leptons, etc, a graph of how they group and interact
    illustrates using getProp and addProp so that attributes
    can be reserved to emphasize the main tree/graph structure
-   `universe.py`       - a start at spatial hierarchy of like, everything


<a id="org5ac9db4"></a>

# acknowledgements / related

This idiom/construct isn't new. Getting new behaviour using the dunder methods setattr, getattr, or
delattr is widespread.  Other dynamic languages may or may not support such dynamic attributes by
default.

-   namedtuples: access is similar to creating the attributes but is not dynamically recursive by default

-   defaultdict: automatically intialises new key values in dicts, rather than instance attributes

-   autodict:    very similar, but for dict&key instead of instance & attribute.
    <https://gist.github.com/sebclaeys/1227566>

-   Javascript:  Yes, In Javascript dot-path expressions are already used to access attributes,
    From <https://rosettacode.org/wiki/Add_a_variable_to_a_class_instance_at_runtime>
    This kind of thing is fundamental to JavaScript, as it's a
    prototype-based language rather than a class-based one.

    e = {}          // generic object
    e.foo = 1
    e["bar"] = 2    // name specified at runtime"

-   Matlab:     Yes, In Matlab "structs" (and hence its weird cousin "struct Array"), and the effectively
    "evaluating parentheses" (e.g. "foo.(bar)") provide dyanmic attributes.

    e  = struct();
    e.aa.bb.cc.dd = 1;

-   Perl:  Yes, works out of the box with hashes, but does anyone still care?


<a id="orgb085b91"></a>

## see also

-   autodata <https://pypi.org/project/autodata/>
-   descriptors: <https://stackoverflow.com/questions/1325673/how-to-add-property-to-a-class-dynamically>
-   long discussion on nested dicts: <https://stackoverflow.com/questions/635483/what-is-the-best-way-to-implement-nested-dictionaries/19829714#19829714>
-   getattr-setattr <https://chase-seibert.github.io/blog/2013/04/12/getattr-setattr.html>
-   other xmls <https://insights.dice.com/2018/01/05/5-xml-alternatives-to-consider/>


<a id="orgae81aab"></a>

# Requires

Python 3.8 - for the walrus operator


<a id="orge71c885"></a>

# Notes

Treacl, pronounced as in "treacle pudding". "Tree Class" is a slight misnomer, in that it works fine for making directed graphs as well as trees.

Access to methods by the dot operator is unaffected, but it is sometimes preferable to have a
separate set of attributes (called, say, "properties") maintained in a separate dict (as illustrated
in the code) to keep properties associated with the nodes or links in the graph.

-   2020-06-03 tweaked/condensed recursive functions
-   2020-05-18 published to github as a work in progress
-   2018-06-02 Treacl - yet another variation on similar datatypes in various interpreted languages.
-   2010-02-01 tdict.py python2 tree dict


<a id="orgf225bdf"></a>

# TBD

possible improvements:

-   pass in props via constructor
-   a more cute/declarative way to do attributes values which are lists of treacl instances,
    i.e. a one-statement way to do "foo = [t(), t()]; foo[0].bar = 1"
-   option for automatically including backpointers
-   export to standard (nestable?) graph format like .gml (see "Yed")
-   table elements swap using some kind of higher-order function?
-   link node-ifier: turn links into bin-ary nodes


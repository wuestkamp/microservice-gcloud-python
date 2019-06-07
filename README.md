Gcloud Kubernetes Cluster Manager
==========

Create and download a Gcloud auth json with permissions Kubernetes Engine Admin and Service Account User.


```
AUTH_JSON=$(cat auth/project-243019–557b3191e5bc.json)

docker built -t factory .

docker run -it -e AUTH_JSON=$AUTH_JSON factory create myclustername europe-west3-a

docker run -it -e AUTH_JSON=$AUTH_JSON factory delete myclustername europe-west3-a
```

Described in this medium article:
COMING

www.wuestkamp.com

# InsightAI_Minions

Project Name: **InsightAI**

Group Name: **Minions**

Main Participant Name: **Denis Shleifman**

Team Participant Names: 
* Morteza Mirzaei
* Dorian Gerdes
* Manav Isrrani
* Sachin Kumar

-----------------------------------------------------

## Github Actions

* Pipeline is located in .github/workflows/redeploy.yaml
* When a change is made in the repo the pipeline will redeploy the llm defined ./lab/docker-compose-llm.yaml file
* This can be manually achieved:

```
docker compose -f docker-compose-llm.yaml up -d --build
```


## Observability

* The observabilility should be run on a separate device so that it does not interfere with any collected metrics
* Deployment is defined in ./lab/docker-compose.yaml
To deploy:
```
docker compose -f docker-compose.yaml up -d --build
```

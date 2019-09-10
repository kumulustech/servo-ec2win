# Optune Servo with ec2win (adjust) and apache benchmark (measure) drivers

1. Echo optune token into docker secret: `echo -n 'YOUR AUTH TOKEN' | docker secret create optune_auth_token -`
1. Run `docker build servo/ -t example.com/servo-ec2win-ab`
1. Referring to `config.yaml.example` create file `config.yaml` in driver's folder. It will contain settings you'd want to make adjustable on your Windows Server instance.
1. Create `.aws` folder with needed credential and permission
1. Create a docker service:

```
docker service create -t
    --name DOCKER_SERVICE_NAME \
    --secret optune_auth_token \
    --env AB_TEST_URL= APACHED_BENCHMARK_URL \
    --mount type=bind,source=/PATH/TO/config.yaml,destination=/servo/config.yaml \
    --mount type=bind,source=/PATH/TO/.aws/,destination=/root/.aws/ \
    example.com/servo-ec2win-ab \
    APP_NAME  \
    --account USER_ACCOUNT \
```

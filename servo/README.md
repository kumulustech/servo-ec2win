# Optune Servo with ec2win (adjust) and apache benchmark (measure) drivers

## Build servo container (from project top dir)
```
docker build servo/ -t example.com/servo-ec2win-ab
```

<!-- ## Running servo as a Docker service

### Create a docker secret with your authentication token
```
echo -n 'myToken'|docker secret create optune_auth_token -
``` -->

### Run Servo (as a docker service)
**@@TBD**:  create/mount secrets for `newrelic_account_id`, `newrelic_apm_api_key`, `newrelic_apm_app_id`, `newrelic_insights_query_key`, and the servo `config.yaml`.  

**IMPORTANT** Update the example commands below as needed, e.g., to bind mount config.yaml:  `--mount type=bind,source=/path/to/config.yaml,destination=/servo/config.yaml`

<!-- ```
docker service create -t --name optune-servo \
    --secret optune_auth_token \
    example.com/servo-ec2asg-newrelic \
    app1 --account myAccount
```

If you named your docker secret anything other than `optune_auth_token`, then specify the path to it:
```
docker service create -t --name optune-servo \
    --secret acme-app1-auth \
    example.com/servo-ec2asg-newrelic \
    app1 --account myAccount  --auth-token /run/secrets/acme-app1-auth
``` -->

**DEV**
When from a local machine instead of an ec2 instance, the simplest way to provide credentials is via local environment variables using `--env` flags like such:
```
docker service create -t --name optune-servo \
    example.com/servo-ec2win-ab \
    --env "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}" \
    --env "AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}" \
    --env "AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}" \
    app1 --account myAccount
```
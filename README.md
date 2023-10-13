Deploy using AWS Cloudformation

- Edit the [deploy.yaml](./deploy.yaml) to update the schedule CRON to run it once. For example `cron(0 19 13 10 ? 2023)` means the CodeBuild project will be triggered to build at 19:00 UTC on Oct 13th, 2023.
- Add the [deploy.yaml](./deploy.yaml) using a Cloudformation Stack and deploy.
  
---

From Cloud Shell 

Upgrade CDK CLI

```
sudo npm install -g aws-cdk
```

clone this repo

```
git clone <this repo>
cd idp-cdk-layout-stack
```

Install dependencies

```
pip3 install -r requirements.txt
```

Install docker

```
sudo yum update -y
sudo amazon-linux-extras install docker
```

Start dockerd

```
sudo dockerd
```

Bootstrap cdk

```
cdk bootstrap
```

Deploy stack

```
cdk deploy SimpleAsyncWorkflow --outputs-file simple_async_workflow.json --require-approval never
```




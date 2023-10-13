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




import argparse

from newsroom.applications.generate import ApplicationsGenerator
from newsroom.codedeploy.generate import CodeDeployAppsGenerator
from newsroom.common.generate import CommonGenerator
from newsroom.iam.generate import IamGenerator
from newsroom.routes.generate import RoutesGenerator
from newsroom.run.deploy import run_deploy
from newsroom.run.ingest import IngestorHelper
from newsroom.run.stack_finder import StackFinder


def generate(stage, env, region):
    if stage == 'securitygroups':
        generator = CommonGenerator()
    elif stage == 'applications':
        generator = ApplicationsGenerator()
    elif stage == 'routes':
        generator = RoutesGenerator()
    elif stage == 'codedeploy':
        generator = CodeDeployAppsGenerator()
    elif stage == 'iam':
        generator = IamGenerator()
    else:
        raise ValueError(f"Unknown stage: {stage}")

    generator.generate(env, region)


def ingest(stage, env, region):
    ingestor = IngestorHelper()
    ingestor.ingest(stage, env, region)
    print("RFCs successfully submitted, please go to aws console for status", end='')


def deploy(env, apps, region, bootstrap, es_url):
    run_deploy(env, apps, region, bootstrap, es_url)


def find_stack(resource_id: str):
    finder = StackFinder()
    finder.find_stack(resource_id)


def run(command, stage, env, apps, region, bootstrap, es_url, resource_id):
    if command == 'generate':
        generate(stage, env, region)
    elif command == 'ingest':
        ingest(stage, env, region)
    elif command == 'deploy':
        deploy(env, apps, region, bootstrap, es_url)
    elif command == 'findstack':
        find_stack(resource_id)
    else:
        raise ValueError(f"Unknown command: {command}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str)
    parser.add_argument('--env', type=str)
    parser.add_argument('--stage', default="custom")
    parser.add_argument('--region', type=str, default='us-east-1')

    # optional (for deploy only)
    parser.add_argument('--apps', type=str, nargs='+', required=False)
    parser.add_argument('--bootstrap', type=str, default=False)
    parser.add_argument('--es-url', type=str, required=False)

    # optional (for find stack only)
    parser.add_argument('--resource-id', type=str, required=False)
    args = parser.parse_args()

    run(args.command, args.stage, args.env.upper(), args.apps, args.region, args.bootstrap, args.es_url, args.resource_id)


if __name__ == '__main__':
    main()

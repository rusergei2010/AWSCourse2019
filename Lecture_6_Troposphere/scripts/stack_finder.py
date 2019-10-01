import boto3
import argparse


class StackFinder:
    def find_stack(self, physical_id: str):
        cf = boto3.client('cloudformation')
        stack = cf.describe_stack_resources(PhysicalResourceId=physical_id)
        print(stack["StackResources"][0]["StackName"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--resource-id', required=True)
    args = parser.parse_args()

    finder = StackFinder()
    finder.find_stack(args.id)


if __name__ == '__main__':
    main()

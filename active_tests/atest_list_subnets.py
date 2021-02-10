from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers
import boto3
import os

args = DcgsPythonHelpers().command_line_argument_names(
    'profile', 'p',
    'region', 'r',
    'vpc', 'v'
)

if not args.profile:
    print("You must specify a profile name with --profile or -p argument in command line.")
    exit()

if not args.region:
    print("You must specify a region name with --region or -r argument in commando line.")
    exit()

if not args.vpc:
    print("You must specify a vpc name with --vpc or -v argument in commando line.")
    exit()

os.environ['AWS_PROFILE'] = args.profile
ec2_client = boto3.client('ec2', region_name=args.region)
# os.environ['AWS_DEFAULT_REGION'] = args.region

subnets = ec2_client.describe_subnets(
    Filters=[{
        "Name": "vpc-id",
        "Values": [args.vpc]
    }]
)

print(subnets)

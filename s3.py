import boto3
import configparser


# read s3 configurations
config = configparser.ConfigParser()
config.read('config.ini')

# get user inputs
words = []
while True:
    if len(words) is not 0:
        end = input('Weitere Eingaben? (y/n) ')
        if end is 'n':
            break
    word = input('Eingabe, die gespeichert werden soll: ')
    words.append(word)

# store in s3 as text file
s3 = boto3.resource('s3',
                    region_name=config['S3']['region_name'],
                    aws_access_key_id=config['S3']['aws_access_key_id'],
                    aws_secret_access_key=config['S3']['aws_secret_access_key'])
s3.Object(config['S3']['bucket'], 'sid-demo.txt').put(Body=str(words))

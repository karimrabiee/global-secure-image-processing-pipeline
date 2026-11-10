{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "PutUploadObjects",
			"Effect": "Allow",
			"Action": [
				"s3:PutObject"
			],
			"Resource": "arn:aws:s3:::kareem-img-proc-upload-${AWS_ACCOUNT_ID}-us-east-1-an/*"
		},
		{
			"Sid": "Logs",
			"Effect": "Allow",
			"Action": [
				"logs:CreateLogGroup",
				"logs:CreateLogStream",
				"logs:PutLogEvents"
			],
			"Resource": "arn:aws:logs:us-east-1:${AWS_ACCOUNT_ID}:*"
		}
	]
}

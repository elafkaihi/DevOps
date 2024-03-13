#!/bin/bash 

# Setup authentification AWS
aws configure set aws_access_key_id xxxxxxxxxxxxxx
aws configure set aws_secret_access_key xxxxxxxxxxxxxxxxx
aws configure set default_region xxxxxxxxxxxxxxx
aws configure set output json 

echo " AWS CLI configured successfully."


S3_BUCKET="xxxxxxxxxxxxx"

#Check for the number of arguments
if [ $# -lt 1 ]; then 
	echo "$0 needs at least one argument"
	exit 1 
fi

#Iterate through provided file paths 
for LOCAL_PATH in "$@"; do
	if [ -z "$LOCAL_PATH" ]; then
		echo " empty file "
		continue
	fi 
	if [ -d "$LOCAL_PATH" ]; then 
		aws s3 sync "$LOCAL_PATH" "s3://$S3_BUCKET/" 2>&1 | {
		while IFS= read -r uploaded_file; do 
			OBJECT_KEY=$(basename "$uploaded_file")
			SHAREABLE_LINK=$(aws s3 presign "s3://$S3_BUCKET/$OBJECT_KEY")
			echo "Shareable link for $OBJECT_KEY: $SHAREABLE_LINK"
		done
		IFS= read -r error_message && echo "$error_message" || echo "succes";}
	elif [ -f "$LOCAL_PATH" ]; then 
		aws s3 cp "$LOCAL_PATH" "s3://$S3_BUCKET/" 2>&1 | { IFS= read  -r error_message && echo "$error_message" || echo "succes";}
		OBJECT_KEY=$(basename "$LOCAL_PATH")
		SHAREABLE_LINK=$(aws s3 presign "s3://$S3_BUCKET/$OBJECT_KEY")
		echo "Shareable link for $OBJECT_KEY: $SHAREABLE_LINK"
	else 
		echo "Error: the path is invalid" 
	fi
done 

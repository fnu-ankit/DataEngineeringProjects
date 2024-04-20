from googleapiclient.discovery import build


def cricbuzz_batsman_ranking_odi_trigger(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "lunar-reef-420701"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "cricbuzz_batsman_ranking_bq_load", 
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://cricbuzz-metadata/udf_cricbuzz_batsman_ranking.js",
        "JSONPath": "gs://cricbuzz-metadata/cricbuzz_batsman_ranking.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "lunar-reef-420701.cricbuzz_dataset.icc_odi_empty_table",
        "inputFilePattern": "gs://cricbuzz_batsman_ranking_bucket/batsman_ranking.csv",
        "bigQueryLoadingTemporaryDirectory": "cricbuzz_batsman_ranking_bucket",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
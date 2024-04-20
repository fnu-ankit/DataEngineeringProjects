from airflow.decorators import dag, task
from datetime import datetime
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from astro import sql as aql
from astro.files import File
from astro.sql.table import Table, Metadata
from astro.constants import FileType


@dag(
    start_date=datetime(2024,1,1)
    ,schedule=None
    ,catchup=False
    ,tags=['retail']
)

def retail():
    upload_csv_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs',
        src='/usr/local/airflow/include/dataset/Online_Retail.csv',
        dst='raw/Online_Retail.csv',
        bucket='gcp_batch_online_retail',
        gcp_conn_id="gcp-batch-processing",
        mime_type="text/csv"
    )

    create_retail_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create_retail_dataset',
        dataset_id="retail",
        gcp_conn_id="gcp-batch-processing"
    )

    gcs_to_raw = aql.load_file(
        task_id='gcs_to_raw'
        ,input_file=File(
            'gs://gcp_batch_online_retail/raw/Online_Retail.csv'
            ,conn_id='gcp-batch-processing'
            ,filetype=FileType.CSV
            )
        ,output_table=Table(
            name='raw_invoices'
            ,conn_id='gcp-batch-processing'
            ,metadata=Metadata(schema='retail')
        )
        ,use_native_support=False
    )

retail()
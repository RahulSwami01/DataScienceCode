import time
start_time = time.perf_counter()
from llama_cpp import Llama

# 1. Download the GGUF model file:
#    You need to download the .gguf file for sqlcoder-7b-2. 
#    For example, from Hugging Face: TheBloke/sqlcoder-7B-GGUF or DevQuasar/defog.sqlcoder-7b-2-GGUF.
#    Place the downloaded file in a location accessible by your script.

model_name ="/Users/sqlcoder-7b-2.Q4_0.gguf" # Adjust the filename and path as needed

# Initialize the Llama model
llm = Llama(
    model_path=model_name,
    n_ctx=4096,  # Max sequence length, adjust based on your needs and model capabilities
    n_threads=8,  # Number of CPU threads to use
    n_gpu_layers=32,  # Number of layers to offload to GPU if you have one, 0 for CPU only
    chat_format="llama-2", # Set chat_format according to the model you are using
    verbose=False
)

# Define the database schema and the natural language question
database_schema = """
USE [Clarity]

GO

/****** Object:  Table [dbo].[PAT_PCP]    Script Date: 8/19/2025 1:38:30 PM ******/

SET ANSI_NULLS ON

GO

SET QUOTED_IDENTIFIER ON

GO

CREATE TABLE [dbo].[PAT_PCP](

              [PAT_ID] [varchar](18) NOT NULL,

              [LINE] [int] NOT NULL,

              [CHANGE_DATE] [datetime] NULL,

              [PCP_PROV_ID] [varchar](18) NULL,

              [EFF_DATE] [datetime] NULL,

              [TERM_DATE] [datetime] NULL,

              [USER_ID] [varchar](18) NULL,

              [CHANGE_REQ_BY_C] [int] NULL,

              [SWITCH_REASON_C] [int] NULL,

              [PCP_TYPE_C] [int] NULL,

              [CM_PHY_OWNER_ID] [varchar](25) NULL,

              [CM_LOG_OWNER_ID] [varchar](25) NULL,

              [DELETED_YN] [varchar](1) NULL,

              [SPECIALTY_C] [varchar](66) NULL,

              [RESULTS_C] [int] NULL,

              [ADMIT_NOTIFY_YN] [varchar](1) NULL,

              [PCP_MESSAGE_YN] [varchar](1) NULL,

              [RELATIONSHIP_C] [varchar](66) NULL,

              [OTHER_NAME] [varchar](254) NULL,

              [OTHER_ADDRESS] [varchar](4000) NULL,

              [OTHER_PHONE] [varchar](508) NULL,

              [OTHER_PAGER] [varchar](508) NULL,

              [OTHER_FAX] [varchar](508) NULL,

              [OTHER_EMAIL] [varchar](508) NULL,

              [PCP_HX_COMMENTS] [varchar](4000) NULL,

              [PCP_ADDRESS_ID] [varchar](508) NULL,

CONSTRAINT [PK_PAT_PCP] PRIMARY KEY CLUSTERED

(

              [PAT_ID] ASC,

              [LINE] ASC

)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, FILLFACTOR = 85) ON [PRIMARY]

) ON [PRIMARY]

GO

/****** Object:  Table [dbo].[PATIENT_2]    Script Date: 8/19/2025 1:38:31 PM ******/

SET ANSI_NULLS ON

GO

SET QUOTED_IDENTIFIER ON

GO

CREATE TABLE [dbo].[PATIENT_2](

              [PAT_ID] [varchar](18) NOT NULL,

              [CM_PHY_OWNER_ID] [varchar](25) NULL,

              [CM_LOG_OWNER_ID] [varchar](25) NULL,

              [RECORD_TYPE_6_C] [int] NULL,

              [BIRTH_TM] [datetime] NULL,

              [DEATH_TM] [datetime] NULL,

              [FAX] [varchar](254) NULL,

              [CITIZENSHIP_C] [varchar](66) NULL,

              [MED_HX_NOTE_ID] [varchar](254) NULL,

              [IS_ADOPTED_YN] [varchar](1) NULL,

              [HEARING_IMPAIRED_YN] [varchar](1) NULL,

              [VISUALLY_IMPAIRE_YN] [varchar](1) NULL,

              [BIRTH_HOSPITAL] [varchar](254) NULL,

              [ALRGY_UPD_INST] [datetime] NULL,

              [BIRTH_CITY] [varchar](254) NULL,

              [BIRTH_ST_C] [varchar](66) NULL,

              [OB_CONVERSION_YN] [varchar](1) NULL,

              [SCHOOL_C] [int] NULL,

              [REFERRAL_SOURCE_ID] [varchar](18) NULL,

              [AMBRX_DOSING_WEIGHT] [float] NULL,

              [AMBRX_DOSE_WT_INST] [datetime] NULL,

              [PAT_NAME_RECORD_ID] [varchar](50) NULL,

              [TMP_HOUSE_NUM] [varchar](254) NULL,

              [TMP_DISTRICT_C] [int] NULL,

              [COMM_METHOD_C] [int] NULL,

              [FOSTER_CHILD_YN] [varchar](1) NULL,

              [CONF_PAT_REAL_NAME] [varchar](192) NULL,

              [PAT_CONF_NM_REC_ID] [varchar](50) NULL,

              [ACTIVE_IER_ID] [varchar](18) NULL,

              [OTH_CITY] [varchar](254) NULL,

              [OTH_ZIP] [varchar](192) NULL,

              [OTH_PHONE] [varchar](254) NULL,

              [OTH_EMAIL] [varchar](254) NULL,

              [OTH_CONTACT_PERSON] [varchar](254) NULL,

              [OTH_HOUSE_NUMBER] [varchar](254) NULL,

              [OTH_DISTRICT_C] [int] NULL,

              [OTH_COUNTY_C] [varchar](66) NULL,

              [OTH_COUNTRY_C] [varchar](66) NULL,

              [OTH_START_DATE] [datetime] NULL,

              [OTH_END_DATE] [datetime] NULL,

              [DEF_ADDRESS_C] [varchar](66) NULL,

              [OTH_STATE_C] [varchar](66) NULL,

              [MAIDEN_NAME] [varchar](254) NULL,

              [EMPR_CITY] [varchar](254) NULL,

              [EMPR_STATE_C] [varchar](66) NULL,

              [EMPR_ZIP] [varchar](254) NULL,

              [EMPR_COUNTRY_C] [varchar](66) NULL,

              [EMPR_PHONE] [varchar](254) NULL,

              [BILL_INSTRUCT_C] [int] NULL,

              [PAT_ASSIST_C] [int] NULL,

              [BILL_COMMENT] [varchar](254) NULL,

              [TEMP_PAT_FLAG_C] [int] NULL,

              [EOB_ADDRESS_C] [int] NULL,

              [TEMP_NAME_YN] [varchar](1) NULL,

              [EMPR_HOUSE_NUM] [varchar](20) NULL,

              [EMPR_DISTRICT_C] [int] NULL,

              [CHART_ABSTD_YN] [varchar](1) NULL,

              [MOTHER_HEIGHT] [numeric](18, 2) NULL,

              [FATHER_HEIGHT] [numeric](18, 2) NULL,

              [PAT_VERIFICATION_ID] [numeric](18, 0) NULL,

              [ALRGY_REV_STAT_C] [int] NULL,

              [ALRGY_REV_CMT] [varchar](300) NULL,

              [REVERSE_NATL_ID] [varchar](50) NULL,

              [ADV_DIR_REV_DT] [datetime] NULL,

              [ADV_DIR_REV_USER_ID] [varchar](18) NULL,

              [LIVING_ARRANGE_C] [int] NULL,

              [DRIVER_LIC_EXP_DATE] [datetime] NULL,

              [LAST_ACCESS_DATE] [datetime] NULL,

              [PED_COMMENT] [varchar](max) NULL,

CONSTRAINT [PK_PATIENT_2] PRIMARY KEY CLUSTERED

(

              [PAT_ID] ASC

)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, FILLFACTOR = 85) ON [PRIMARY]

) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

/****** Object:  Table [dbo].[PATIENT_RACE]    Script Date: 8/19/2025 1:38:31 PM ******/

SET ANSI_NULLS ON

GO

SET QUOTED_IDENTIFIER ON

GO

CREATE TABLE [dbo].[PATIENT_RACE](

              [PAT_ID] [varchar](18) NOT NULL,

              [LINE] [int] NOT NULL,

              [PATIENT_RACE_C] [int] NULL,

              [CM_PHY_OWNER_ID] [varchar](25) NULL,

              [CM_LOG_OWNER_ID] [varchar](25) NULL,

CONSTRAINT [PK_PATIENT_RACE] PRIMARY KEY CLUSTERED

(

              [PAT_ID] ASC,

              [LINE] ASC

)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, FILLFACTOR = 85) ON [PRIMARY]

) ON [PRIMARY]

GO

/****** Object:  Table [dbo].[PATIENT_TYPE]    Script Date: 8/19/2025 1:38:31 PM ******/

SET ANSI_NULLS ON

GO

SET QUOTED_IDENTIFIER ON

GO

CREATE TABLE [dbo].[PATIENT_TYPE](

              [PAT_ID] [varchar](18) NOT NULL,

              [LINE] [int] NOT NULL,

              [PATIENT_TYPE_C] [varchar](66) NULL,

              [CM_PHY_OWNER_ID] [varchar](25) NULL,

              [CM_LOG_OWNER_ID] [varchar](25) NULL,

CONSTRAINT [PK_PATIENT_TYPE] PRIMARY KEY CLUSTERED

(

              [PAT_ID] ASC,

              [LINE] ASC

)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, FILLFACTOR = 85) ON [PRIMARY]

) ON [PRIMARY]

GO

 
"""
question = "What is the total revenue from orders for each product?"

# Construct the prompt for SQL generation
# The prompt format is crucial for SQLCoder models. Refer to the model's Hugging Face page for specifics.
prompt = f"""### Task.
Generate a SQL query to answer [QUESTION]{question}[/QUESTION]

### Database Schema.
The query will run on a database with the following schema:
{database_schema}

### Answer.
Given the database schema, here is the SQL query that [QUESTION]{question}[/QUESTION]
[SQL]
"""
prompt=f"""
### Task
Generate a MSSQL query to answer the following question: What is the age of Smith?

### Database Schema.
The query will run on a database with the following schema:
{database_schema}

### SQL
Given the database schema, here is the SQL query that answers What is the race of patients ID 110010 who has Birth City Boston?:
```sql
"""
# Generate the SQL query
output = llm(
    prompt,
    max_tokens=512,  # Max tokens to generate for the SQL query
    stop=["[/SQL]", "###"],  # Stop tokens indicating the end of the SQL query or prompt sections
    echo=False  # Do not echo the prompt in the output
)

# Extract and print the generated SQL query
generated_sql = output["choices"][0]["text"].strip()
from sqlglot import parse_one, exp

parsed_query = parse_one(generated_sql, read="postgres")
mysql_query = parsed_query.sql(dialect="mysql")
print(f"Generated SQL Query:\n{mysql_query}")

end_time = time.perf_counter()
# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.6f} seconds")

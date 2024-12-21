# NYC-TAXI-DE-Project

**Executive Summary**

This project is an end-to-end implementation of a modern data engineering pipeline, showcasing advanced skills in data ingestion, transformation, modeling, and delivery. Using the NYC Taxi dataset, it demonstrates the application of industry best practices, scalable architecture, and cutting-edge technologies. The project follows the Medallion Architecture and integrates tools like Azure, Databricks, and Delta Lake to process and deliver high-quality, analysis-ready data. This work is designed to highlight proficiency in building robust, automated data solutions tailored to real-world business scenarios.
________________________________________
**Objectives**

•	Automate Data Ingestion: Dynamically fetch data from APIs, eliminating manual intervention.

•	Implement Medallion Architecture: Organize data into Bronze, Silver, and Gold layers for structured processing.

•	Optimize Data Processing: Leverage PySpark and Databricks for efficient large-scale transformations.

•	Ensure Data Quality and Reliability: Utilize Delta Lake features like ACID transactions, data versioning, and time travel.

•	Deliver Business Value: Enable seamless data access for analytics and visualization using Power BI.

________________________________________
**Tools and Technologies**

•	Azure Data Factory: Orchestrates data pipelines with parameterization and dynamic configurations.

•	Azure Data Lake Storage (Gen2): Provides hierarchical storage for big data, optimized for scalability.

•	Databricks: Facilitates distributed data processing using PySpark.

•	Delta Lake: Enhances data management with features like schema enforcement, versioning, and transactional integrity.

•	Parquet File Format: Stores data in a columnar format, improving query performance and storage efficiency.

•	Power BI: Connects to the Gold layer for real-time reporting and analytics.

•	GitHub: Hosts project documentation, scripts, and datasets for version control.
________________________________________
**Architecture and Methodology**

**Medallion Architecture**

•	Bronze Layer: Ingests raw data directly from APIs, storing it in Parquet format.

•	Silver Layer: Cleans and standardizes data to ensure consistency and usability.

•	Gold Layer: Models data for specific business use cases, making it ready for analytics.

**Security and Reliability**

•	Data Redundancy: Configured Local (LRS) redundancy for high availability.

•	Managed Identities: Implemented to secure resource access and automate authentication processes.
________________________________________
**Implementation Details**

**1. Dynamic Data Ingestion with Azure Data Factory**

Azure Data Factory (ADF) was used as the primary orchestration tool for automating the data ingestion process. Each step of the pipeline is explained in detail below:

**Step 1: Create a Linked Service**

Purpose: Establish a connection between ADF and the data source (NYC Taxi API) as well as the data storage (Azure Data Lake).

Process:

Navigate to the Azure Data Factory interface and select "Linked Services."

Create a new linked service for the API by providing the API URL and authentication details.

Create another linked service for Azure Data Lake, specifying the storage account and authentication method(managed identity).

Outcome: Secure and reusable connections to both the data source and storage.

**Step 2: Create Datasets**

Purpose: Define the data structures for both the source (API) and the sink (Azure Data Lake).

Process:

Define a source dataset to represent the API response. Configure the dataset to handle JSON format if the API returns JSON data.

Define a sink dataset for the Bronze layer, pointing to the desired location in Azure Data Lake with a Parquet file format.

Outcome: Data is structured and ready for dynamic parameterization.

**Step 3: Build a Pipeline**

Purpose: Automate the extraction and loading process using a sequence of activities.

Process:

Add an HTTP Activity: Configure an HTTP activity to make GET requests to the NYC Taxi API. Use parameters to dynamically fetch data for each month.

ForEach Activity: Add a ForEach loop to iterate over a list of months. Pass the current iteration value as a parameter to the HTTP activity.

Copy Activity: Link the HTTP activity to a Copy activity that transfers the API response data into the Azure Data Lake.

Error Handling: Add conditional checks and failover logic to manage errors during API calls or data transfer.

Outcome: A fully automated pipeline capable of fetching monthly data dynamically.

**Step 4: Parameterize the Pipeline**

Purpose: Enable the pipeline to handle different configurations without hardcoding values.

Process:

Define parameters for the API URL, month, and target file path.

Pass these parameters dynamically at runtime, ensuring the pipeline remains flexible and reusable.

Outcome: Scalability and adaptability for handling different datasets or time periods.

**Step 5: Test and Debug**

Purpose: Ensure the pipeline works as expected under various scenarios.

Process:

Test the pipeline with a small subset of data.

Validate the output files in the Bronze layer to confirm successful ingestion.

Debug any errors using ADF’s monitoring and logging tools.

Outcome: A robust and error-free data ingestion pipeline.

**2. Raw Data Storage (Bronze Layer)**
   
•	Objective: Efficiently store raw data for processing.

•	Approach: Used Azure Data Lake with hierarchical namespaces enabled for structured storage. Data was stored in Parquet format for performance optimization.

•	Outcome: Enabled organized and efficient storage of high-volume data.

**3. Data Transformation (Silver Layer)**
   
•	Objective: Standardize and clean data for usability.

•	Approach: Applied PySpark in Databricks to remove null values, enforce schema consistency, and integrate lookup data.
•	Outcome: Generated clean, structured data ready for aggregation and modeling.

**4. Data Modeling and Aggregation (Gold Layer)**
   
•	Objective: Prepare data for business insights.

•	Approach: Aggregated and modeled data into Delta Lake tables, leveraging features like time travel and ACID compliance.

•	Outcome: Produced analysis-ready data optimized for querying and reporting.

**5. Data Delivery for Analytics**
    
•	Objective: Enable data visualization and reporting.

•	Approach: Established a direct connection between Azure Data Lake and Power BI. Ensured optimal data access for dashboards and analytics.

•	Outcome: Delivered high-quality data to stakeholders for actionable insights.

________________________________________
**Key Features and Innovations**

•	Dynamic Pipelines: Automated data ingestion with reusability and scalability.

•	Advanced Data Management: Leveraged Delta Lake for schema evolution, version control, and transaction logs.

•	Performance Optimization: Used Parquet format and distributed computing for efficient processing.

•	Real-World Architecture: Implemented Medallion Architecture to mirror industry standards.

•	Secure and Reliable: Ensured data security through managed identities and redundancy configurations.

________________________________________
**Business Impact**

•	Efficiency Gains: Automation reduced manual effort, increasing productivity.

•	Scalability: Designed to handle large datasets and growing business needs.

•	Improved Decision-Making: Delivered high-quality, analysis-ready data to Power BI, supporting strategic decisions.

•	Industry Relevance: Demonstrated expertise in real-world tools and architectures, adding value to data engineering teams.

________________________________________
**Lessons Learned**

•	Developed proficiency in building scalable, production-grade data pipelines.

•	Gained in-depth understanding of Azure’s ecosystem and big data processing.

•	Enhanced problem-solving skills by addressing real-world data challenges.

•	Strengthened knowledge of distributed systems and cloud technologies.
________________________________________
**Next Steps**

•	Real-Time Processing: Incorporate streaming data pipelines for real-time analytics.

•	Cost Optimization: Analyze and optimize Azure resource usage for cost-effectiveness.

•	Enhanced Analytics: Integrate additional visualization tools like Tableau to broaden reporting capabilities.

________________________________________
**Repository and Resources**

•	NYC Taxi Dataset: [NYC Open Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

•	Project Repository: https://github.com/Baggio17/NYC-TAXI-DE-Project
________________________________________

This project underscores my expertise in designing and implementing scalable, reliable, and impactful data engineering solutions, showcasing my readiness to contribute to enterprise-level data initiatives.


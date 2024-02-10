# SPI Technical Design Specification

### Purpose:
Primary purpose of this document is to gather Functional and Non Functional Requirements as well as prepare Technical Design Specification.
SPI (Stock Performance Index)

#### Technology Selection
Frontend: HTML, React JS, NodeJS, Azure Storage Account, Ignaite.com/demo/spi
Backend: MongoDB, API, Vector DB
Analytics: Databricks ML, Dashboard
Intelligence: Databricks AI, Models

#### SPI Functional Requirement (Frontend - Shreyas Raut)
1. Login Page: As an Investor, I would like to login to my SPI Account
2. Dashboard Page: As an Investor, I would like to see distribution of my Investment among various Startups
3. Question from Investor: What is my top 3 risky Investments.

#### SPI Non-Functional Requirement (Backend - Parth Burde)
1. Login Page: Create database table and API to maintain User details to enable Authentication
2. Dashboard Page: Create database table and API to maintain Individual Investor portfoli

#### SPI Data Analytics Requirement (Analytics - Vishakha Sharma & Aayush Dalal)
1. Data Sourcing: Acquire relevant data from Backend Database into Databricks
2. Dashboard Content: Create Pichart (based on req) and share it as Dashboard to Frontend

#### SPI Artificial Inteligence Requirement Requirement (Intelligence - Harsh Kalbande & Vaibhav Gomkar)
1. Vector Indexing: Prepare Embedding Index (MogoDB/Databricks)
2. Candidate Selection: Allow Investor ask Question and perform Similarity Search from Index
3. Prompt Engg: Prepare Prompt LangChain Format (Question + Vector Search Result + Context( Investor XYZ))
4. LLM Request: Send all information to LLM like GPT or Lamma andget response.

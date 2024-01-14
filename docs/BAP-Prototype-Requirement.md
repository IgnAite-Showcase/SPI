# BAP (Business Analysis Platform) Requirement Analysis
### Purpose/Background
1. Purpose of this document is to build Practice Application for the IgnAite interns to get familiar with the Low Code and No Code Web Development technology such as Oracle Apex.
2. Additionally this will also enable team to practice Design Thinking Methodologies and come up with the alternative solutions for final prototyping idea. 
3. Hence BAP (Business Analysis Platform) will enable us define various components to perform end to end Business Analysis and related documentation. 
4. Business Analysis is the critical step in any SDLC (Software) or PDLC(Product), which yields important direction for project to be successful.
5. During Business Analysis a lot of steps needed to follow in certain order with certain prerequisits.
6. Various sections of the BRD often referred repetatively in many other documentations. Maintanance of these content at various documents is ofen challenging.
7. The moto of the BAP is to "maintain content at one place and reuse to generate multiple documentations"
8. At the same time BAP will promote and help team practice Design Thinking Methodologies.

### Development Process SOP - Standard Operating Procedure
1. Identify Features/Component
2. Define Navigation Menu
3. Define Breadcrumb Menu (Indicates how Page Organized)
4. Data Structure Modeling Scripts (Tables, Sequences, Triggers, Views, Initial Inserts)
5. Define the Report (Suggession: Do not mention word _Report in name)
6. Define the Data Entry Form (Suggession: Do not mention word _Form in name)
7. Link Report with the Navigation and Breadcrumb Menu
8. Define Dashboard

### Application -> Login
- User Authentication
- Users Authorization (User, Group Role, Acccess Level, Provisioning, Privacy Policy)

### Application -> Logout
- Navigation Bar Loout Link
- Session Close
- Security requirement for Back Button

### Maintenance --> LOV
- List of Values (Form + Report)
- E.g. Y/N, Active/Inactive, Usecase_Persona_Type, Application_User_Type
- Database Table Structure ()

### Maintenance -> Users
- User Demographics, user type, encrypted password
- Database Table Structure ()

### Maintenance -> Upload Images
Utility to Upload images related to Solution Sketch and Product Infographics
- Diagrams (Upload and Maintain)
- Database Table Structure ()

### Maintenance -> Upload Docs
Utility to Upload documents related to the reference materials/approvals which can not be simply feed to BAP via screens.
- Documents (Upload and Maintain)
- Database Table Structure ()

### Application -> Business Workflow 
Business Rules (Review/Approval/API/Database Action/Pages)
Ensure that certain steps follows during BAP and make sure that previous process completed (Reviewed/Approved) successfully. Sometime confitional approval is needed.
- Start (param)
- Logic
- Stop
- Action
- Database Table Structure ()

### Application -> Landing Page (Opportunity)
Consolidated View of Lead/Prospect/Opportunity. Depend on the phase of application and business workflow, application should display related sections within the application.
- Parameter (Lead Number)
- Design Thinking (E, D, I, P, T)
- Demographics
- Charter -> Links
- Requirements

### Home -> Design:
Define pages displaying educational materials to bring team up to the speed in Design Thinking
1. **Empathise:** Persona and Domain Knowledge
   The first stage of the Design Thinking process is to getting to know your user and understanding their wants, needs and objectives.
3. **Define:** Problem Statement
   Defining the problem for potential Solution. You’ll gather all of your findings from the empathise phase and start to make sense of them: what difficulties and barriers are your users coming up against
4. **Ideation:** Register an Idea
   In the ideation phase, you’ll explore and come up with as many ideas as possible. Some of these ideas will go on to be potential solutions to your design challenge; some will end up on the reject pile. <p>
   Alternativee Idea Generation Methods (Brainstorm, Braindump, Brainwrite, Brainwalk, Challenge Assumptions, SCAMPER, Mindmap, Sketch or Sketchstorm, Storyboard, Analogies, Provocation, Movement, Bodystorm, Gamestorming, Cheatstorm, Crowdstorm, Co-Creation Workshops, Prototype, Creative Pause) <p>
   Selection methods (Post-it Voting or Dot Voting, Four Categories Method, Bingo Selection, Idea Affinity Maps, 
Now Wow How Matrix, Six Thinking Hats, Lean Startup Machine Idea Validation Board, Idea Selection Criteria)
6. **Prototype:** Working Model
  Typically done by (POC, POT, PILOT, MVP)
7. **Test:** Demo and Feedback
  Purpose of this phase is to develop a Prototypy by (Implemention, Demo, Retro, Feedback, Analyze, Propose Enhancement)

### Design -> Empathise
- Persona (E.g. Admin, Business Analyst, Data Analyst, Project Manager, UI/UX Designer, Developer)
- Roles
- Accountability
- Responsibilities
- Challenges
- Innovation Opportunities
- Voting/Rating
- Database Table Structure ()

### Design -> Idea
- Idead Demographics,
- Background Purpose - Hypothesis
- Problem Statement
- Table Structure: IDEA_PK, IDEA_TYPE, IDEA_NAME, IDEA_OBJECTIVE, IDEA_HYPOTHESIS, IDEA_PROBLEM, IDEA_PRIORITY, IDEA_OWNER, IDEA_STATUS, IDEA_USER, IDEA_JUSTIFICATION, IDEA_LOGISTIC, IDEA_SOLUTION, IDEA_ASSUMPTION, IDEA_CHALLENGES, IDEA_FEASIBILITY, IDEA_PROPOSAL, IDEA_BENIFITS, IDEA_SUCCESS_CRITERIA

### Design -> Prototype
- Prototype Category: Typically done by (POC, POT, PILOT, MVP)
- Database Table Structure ()
  
### Design -> Test:
- Demo
- Retro
- Feedback
- Analysis
- Enhancement Plan
- Database Table Structure ()

### Design -> Business Charter
- Demogrphics: Idea Name, Description, Success Criteria
- Team: Customer, Application users, Investor, Project Manager, Stakeholder, Tech Lead
- Budget: Capital and Expense, Return on Investment
- Milestones: Deliverable timelines
- Potential Risks: Subject Area, Risk, Level, Mitigation, Remediation 
- Approvals: Approver Name, Title, Approval, Conditional Comments and Date Time

### Opportunity -> Demographics
1. Background Purpose:
   Provide background information on project idea
3. Executive Summary: To begin, you’ll need to create an executive summary that provides an overview of the organization and the challenges facing the business. You’ll explain the issues and what the organization is trying to achieve to ensure everyone is on the same page. This section should be short, like an elevator pitch, summarizing the rest of the business requirements document.
4. Project Description/Objectives:
After summarizing the issue you plan to address in the project, you’ll want to clearly define the project’s objective. This helps define the project phases, creates a way to identify solutions for the requirements of the business and the customer, gains consensus from stakeholders and the project team and describes how you arrived at the objectives.

### Use Case: Follow SIPOC Model (Suppliers, Inputs, Process, Outputs and Customers)
- Description
- S: Actor/Persona
- I: Action
- P: Application/System/Process
- O: Result
- C: End User

### Blueprint
It serves as a high-level representation of software designthat supports the development process in several ways
- Current ASIS State
- Proposed Future State
- Alternative Solution
- Final Solution Sketch
  
### Analysis
- SWOT Analysis - SWOT is an acronym for Strengths, Weaknesses, Opportunities, and Threats. The analysis utilizes these headings in a quadrant format (Fig. 1) to list core competencies and other relevant company traits and characteristics. It’s a visual tool to help you see how the company is currently positioned and provides insight on what areas the company should be addressing in the near the future.
- Business Driver: 
- Business Justification: 
- Cost-Benefit Analysis: You’ll also want to do a cost-benefit analysis to determine if the costs associated with the project are worth the benefits you’ll get. This requires first determining the associated costs of the project, such as upfront development costs, unexpected costs, future operating costs and tangible and intangible costs. You’ll also need to figure out what benefits derive from the project.
- ROI Analysis : Return on Investment
- Data Analysis:
- USP (Unique Selling Proposition) : Unique selling points for startup which makes them stand out from other players in business
- Feasibility Analysis

### Project Scope
- Assumptions:
- Constraints: At this point, you’ll want to explore the project constraints. Define the limitations of the project and share those with the project team so they know of any obstacles earlier than later. In order for them to clear those hurdles, you’ll want to provide any necessary training or allocate resources to help the project stay on track.
- In Scope:The project scope should define in detail what is covered in the project and what would make it run out of scope. This creates a clear boundary for the project and allows stakeholders and teams to agree on the business goals and high-level outcomes. Note what problems are being addressed, the boundaries for implementing the project and the expected return on investment (ROI).
- Out of Scope: The project scope should define in detail what is not covered in the project

### Requirement Analysis
- Epic Stories
- Application Features:
- Functional Requirements/User Stories: List the business requirements or critical activities that must be completed to meet the organization’s objectives. These business requirements should meet both stakeholder and customer needs. This can include a process that must be completed, a piece of data that is needed for the process or a business rule that governs that process and data.
- Non-Functional Requirements/Tasks:
- Testing
- Issues and resolutions
- Treaceability Matrix: of all above

### Team:
- Team Type
- Key Stakeholders: Now you’ll want to identify and list the key stakeholders in the project. Once you have that list, assign roles and responsibilities to each. These might be people outside of your department so you should define their role in the success of the project. This information needs to be distributed in order for everyone to know what’s expected of them in the project. You can even use this section to assign tasks.

### Organization Chart:

### RACI Matrix: 
A RACI chart is a tool that clarifies who does what in a project. It specifies the roles of responsible, accountable, consulted, and informed (RACI) for each task.
- Development Roles RACI
- Oppertional Support RACI

### Knowledgebase
- Business Terms
- Technical Terms
- Domain Knowledge
- Ontology
- Taxonomy

### Estimated Planning
Project Deliverable Schedule and Timelines and estimated costs

### Product Roadmap
- Current Feature Timelines (Quaterly)
- Potential Feature Timeline (Quaterly)

### Technology Selection
- Strengths and Weakness
- Strategy: Short term(Prototyping), Long term (Production use)
- Evaluation Criteria
- Request for Proposal
- Product Scoring
- Vendor Selection
- License (PayGo, Subscription, Purchase)
- Cost mangement
- TCO (Total Cost of Ownership)

### Appendix
- Research References
- Citations
- Other Contents

### Reference Material
- Design Thinking: https://careerfoundry.com/en/blog/ux-design/what-is-design-thinking-everything-you-need-to-know-to-get-started/

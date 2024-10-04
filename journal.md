### Journal.md

#### Cocktail Database Setup

The initial goal was to create a SQL-based cocktail database for submitting cocktail recipes. I set up an Aurora MySQL instance on AWS, thinking it would be a good foundation for storing everything from cocktail names to ingredients, glassware, and preparation steps.

- **Schema Design:**  
  I designed the schema in MySQL Workbench, building tables for **Cocktails**, **Ingredients**, and **Cocktail_Ingredients** (a many-to-many relationship), as well as **Users**, **Ratings**, and **Reviews**. This structure covers the relational data model, but things got tricky when it came to importing real-world data.

- **Data Import Problems:**  
  I pulled a dataset of cocktails from Kaggle, but the data didn't align perfectly with the schema I had in place. Specifically, ingredient quantities didn’t map well into the schema. When I tried importing directly into MySQL via Workbench, I ran into truncation errors on the **Cocktail_Ingredients** table. That forced me to reconsider the data import strategy, and I decided to handle the processing externally using Python.


At some point, I realized this project needed more than just a database. I started expanding it into a full-stack web app using AWS.

- **S3 Bucket for Static Hosting:**  
  To get the front-end up and running, I hosted the basic HTML, CSS, and JavaScript files on an S3 bucket configured for static website hosting. At first, I tried to automate deployments using **CodePipeline**, but ran into multiple permission issues. These took quite a bit of time to troubleshoot.

- **CodePipeline & Permissions Problems:**  
  The biggest challenge here was setting the correct permissions for S3. I kept getting permission errors during deployment, particularly related to ACL restrictions. After fighting with it for a while, I eventually switched to manually deploying my front-end files to S3 since it was simpler and avoided the issues I faced with CodePipeline.

- **Lambda and API Gateway:**  
  To allow users to interact with the site (e.g., submitting cocktail recipes), I set up **AWS Lambda** functions for backend logic and linked them to **API Gateway** to handle HTTP requests. This will let users submit data through the web interface, but I’m still figuring out how to get everything integrated with the Aurora database smoothly.

There’s still a lot to do, especially with integrating the serverless components and managing the database operations, but the core structure is starting to take shape.

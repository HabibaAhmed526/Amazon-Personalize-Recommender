# Amazon Personalize Recommender System 

The project involves building a simple recommendation system using **Amazon Personalize** with a real dataset, and generating recommendations for sample users.

---

## Objective

- Prepare and upload a dataset of user-item interactions.
- Train a recommender model using **Amazon Personalize**.
- Generate personalized recommendations for selected users.
- Document all steps, decisions, and results.
- Provide a deployment plan to integrate recommendations into an application.

---

## Tools & Technologies Used

- **Amazon Personalize (Video On Demand domain)**
- **Amazon S3**
- **IAM Roles & Policies**
- **MovieLens 100K Dataset**

---

## Dataset Preparation

- Dataset used: **MovieLens 100K**
- I extracted a sample of **1,000 rows** from the original dataset to simplify processing and reduce training time.
- The `u.data` file was converted into a CSV named `interactions.csv`.
- A new column `event_type` with the value `"watch"` was added to each row to comply with schema requirements.

**Final CSV Columns:**

```text
user_id,item_id,timestamp,event_type
```

---

## Amazon Personalize Setup

1. **Created a Dataset Group**:
   - Name:`movie-recommender-habiba`
   - Domain: `Video On Demand (VOD)`
     (Choosing VOD allowed me to use Amazon's pre-optimized recommender for movie-watching behavior)
2. **Used Built-in Schema**:
   The VOD domain automatically provides a compatible schema:

```json
{
  "type": "record",
  "name": "Interactions",
  "namespace": "com.amazonaws.personalize.schema",
  "fields": [
    { "name": "user_id", "type": "string" },
    { "name": "item_id", "type": "string" },
    { "name": "timestamp", "type": "long" },
    { "name": "event_type", "type": "string" }
  ],
  "version": "1.0"
}
```

3. **Uploaded the CSV to S3** and configured:
   - IAM Role with `AmazonPersonalizeFullAccess`
   - S3 bucket policy to allow access

4. **Imported the dataset** into Amazon Personalize successfully.

---

## Recommender Setup & Recommendations

- **Used Built-in Recommender**: `Top Picks for You` (automatically trained under VOD)
- No need to manually choose a recipe or train a custom solution
- Amazon handled training and tuning automatically based on the uploaded interactions

### Sample Output for `user_id = 102`:

| Item ID | Score     |
|---------|-----------|
| 234     | 0.00861   |
| 274     | 0.00647   |
| 25      | 0.00642   |
| ...     | ...       |

> Scores reflect the relevance of each item to the specific user.

---

## Deployment Plan

If deployed in a real-world application:

- Build a backend using **FastAPI** or **Flask** to call the Personalize `GetRecommendations` API using **boto3**.
- Display recommended items in a web interface (e.g., Streamlit or React).
- Update real-time interaction data via **Event Trackers**.
- Schedule regular retraining pipelines using **AWS Lambda** or **Step Functions**.
- Monitor usage and performance using **CloudWatch**.
- Secure with appropriate **IAM roles** and **policies**.


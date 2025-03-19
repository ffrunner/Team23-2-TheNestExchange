import json
import redis
from database_connect import connect_database

# Configure Redis client
redis_client = redis.Redis(host='database-1.cjm0e6m6u6vm.us-east-2.rds.amazonaws.com', port=5432, decode_responses=True)
CACHE_EXPIRATION = 600  # Cache expiration time

# Define the listing categories
ALLOWED_CATEGORIES = ['Academic Materials', 'Textbooks', 'Technology', 'Furniture'] # We may add more

# Show the listings for a given category using Redis caching
def get_listings_by_category(category):

    # Throw error if a category doesn't exist
    if category not in ALLOWED_CATEGORIES:
        raise ValueError("Invalid category")

    cache_key = f"listings:{category}"
    cached = redis_client.get(cache_key)
    if cached:
        # Return cached listings as a Python list
        return json.loads(cached)

    # Get a new database connection
    conn = connect_database()
    try:
        # Use a context manager to automatically close the cursor
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, user_id, category, description, image_url FROM listings WHERE category = %s",
                (category,)
            )
            rows = cur.fetchall()
    finally:
        # Always close the connection after use
        conn.close()

    # Convert rows from the database into a list of dictionaries
    listings = [
        {
            "id": row[0],
            "user_id": row[1],
            "category": row[2],
            "description": row[3],
            "image_url": row[4]
        }
        for row in rows
    ]

    # Cache the listings result in Redis
    redis_client.setex(cache_key, CACHE_EXPIRATION, json.dumps(listings))
    return listings

# Report a given listing
def report_listing(listing_id, reason, reported_by):

    conn = connect_database()
    try:
        with conn.cursor() as cur:
            # Check if the listing exists in the database
            cur.execute("SELECT id FROM listings WHERE id = %s", (listing_id,))
            if not cur.fetchone():
                raise ValueError("Listing not found")

            # Insert the report record into the reports table
            cur.execute(
                "INSERT INTO reports (listing_id, reason, reported_by) VALUES (%s, %s, %s)",
                (listing_id, reason, reported_by)
            )
            conn.commit()
            return {"message": "Report submitted"}
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

# Add a claim to a listing
def add_claim(listing_id, claimed_by, message=""):

    conn = connect_database()
    try:
        with conn.cursor() as cur:
            # Check if the listing exists and retrieve its owner
            cur.execute("SELECT user_id FROM listings WHERE id = %s", (listing_id,))
            row = cur.fetchone()
            if not row:
                raise ValueError("Listing not found")
            listing_owner = row[0]
            
            # Insert the claim record
            cur.execute(
                "INSERT INTO claims (listing_id, claimed_by, message) VALUES (%s, %s, %s)",
                (listing_id, claimer_id, message)
            )
            conn.commit()
            """
            A notification will need to be sent to the listing owner for the claim
            """
            return {"message": "Claim submitted"}
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

# Allow user to view all claims made
def get_claims_for_user(user_id):

    conn = connect_database()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT listing_id, message FROM claims WHERE claimed_by = %s",
                (user_id,)
            )
            rows = cur.fetchall()
            claims = [
                {"listing_id": row[0], "message": row[1]}
                for row in rows
            ]
        return {"claimer_id": user_id, "claims": claims}
    finally:
        conn.close()

# Allow item owner to view all claims for a listing
def get_claims_for_listing(listing_id):

    conn = connect_database()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT claimed_by, message FROM claims WHERE listing_id = %s",
                (listing_id,)
            )
            rows = cur.fetchall()
            claims = [
                {"claimed_by": row[0], "message": row[1]}
                for row in rows
            ]
        return {"listing_id": listing_id, "claims": claims}
    finally:
        conn.close()
